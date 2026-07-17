"""Build a caption from the problem's README and publish an image
(or multi-image) post to LinkedIn using the solved LeetCode problem's
slides.

Images must be uploaded through LinkedIn's own Images API to get an
`urn:li:image:...`, external URLs (e.g. Cloudinary) cannot be attached
directly to a post -- that's the bug this version fixes.

Usage:
    python post_to_linkedin.py <problem-folder>
"""
import os
import sys
import time
from pathlib import Path
from typing import List, Optional

import requests

from utils import parse_readme, get_difficulty_from_stats, difficulty_emoji

API_BASE = "https://api.linkedin.com/rest"
LINKEDIN_VERSION = "202507"
MAX_RETRIES = 3
CAPTION_LIMIT = 2900  # stay safely under LinkedIn's ~3000 char commentary limit


def auth_headers() -> dict:
    return {
        "Authorization": f"Bearer {os.environ['LINKEDIN_ACCESS_TOKEN']}",
        "LinkedIn-Version": LINKEDIN_VERSION,
        "X-Restli-Protocol-Version": "2.0.0",
    }


def request_with_retry(method: str, url: str, **kwargs) -> requests.Response:
    response = None
    for attempt in range(1, MAX_RETRIES + 1):
        response = requests.request(method, url, timeout=30, **kwargs)
        if response.status_code < 500 and response.status_code != 429:
            return response
        wait = 2 ** attempt
        print(f"::warning::{method} {url} returned {response.status_code}, retrying in {wait}s")
        time.sleep(wait)
    return response


def initialize_upload(author_urn: str) -> dict:
    resp = request_with_retry(
        "POST",
        f"{API_BASE}/images?action=initializeUpload",
        headers={**auth_headers(), "Content-Type": "application/json"},
        json={"initializeUploadRequest": {"owner": author_urn}},
    )
    resp.raise_for_status()
    return resp.json()["value"]


def upload_image(image_path: Path, author_urn: str) -> str:
    """Upload one local image straight to LinkedIn and return its image URN."""
    init = initialize_upload(author_urn)
    upload_url = init["uploadUrl"]
    image_urn = init["image"]

    with open(image_path, "rb") as f:
        put_resp = request_with_retry(
            "PUT",
            upload_url,
            headers={"Authorization": f"Bearer {os.environ['LINKEDIN_ACCESS_TOKEN']}"},
            data=f.read(),
        )
    put_resp.raise_for_status()
    return image_urn


def build_caption(folder: Path, meta: dict) -> str:
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    repo_url = f"https://github.com/{repo}/tree/main/{folder.name}" if repo else ""
    emoji = difficulty_emoji(meta["difficulty"])
    diff_label = meta["difficulty"].capitalize() if meta["difficulty"] != "unknown" else ""
    description = " ".join(meta["description"].split())[:600]

    lines = [f"🚀 Solved: {meta['title']}"]
    if diff_label:
        lines.append(f"{emoji} Difficulty: {diff_label}")
    if meta["url"]:
        lines.append(f"🔗 Problem: {meta['url']}")
    lines += ["", description, ""]
    if repo_url:
        lines.append(f"💻 Full solution: {repo_url}")
    lines += ["", "#leetcode #dsa #python #coding #softwareengineering #100daysofcode"]

    return "\n".join(lines)[:CAPTION_LIMIT]


def build_content(image_urns: List[str]) -> Optional[dict]:
    if not image_urns:
        return None
    if len(image_urns) == 1:
        return {"media": {"id": image_urns[0]}}
    return {"multiImage": {"images": [{"id": urn} for urn in image_urns[:20]]}}


def main(folder_arg: str) -> None:
    folder = Path(folder_arg)
    author_urn = f"urn:li:person:{os.environ['LINKEDIN_PERSON_ID']}"

    meta = parse_readme(folder)
    if meta["difficulty"] == "unknown":
        fallback = get_difficulty_from_stats(Path("stats.json"), folder.name)
        if fallback:
            meta["difficulty"] = fallback

    images = ([folder / "cover.png"] if (folder / "cover.png").exists() else [])
    images += sorted(folder.glob("code_*.png"))
    images = [p for p in images if p.exists()]

    if not images:
        print(f"::error::No images found in {folder}; run generate_images.py first.")
        sys.exit(1)

    image_urns = []
    for image in images:
        try:
            urn = upload_image(image, author_urn)
            image_urns.append(urn)
            print(f"Uploaded {image.name} to LinkedIn -> {urn}")
        except requests.HTTPError as exc:
            print(f"::warning::Skipping {image.name}, LinkedIn upload failed: {exc}")

    if not image_urns:
        print("::error::All image uploads failed, aborting post.")
        sys.exit(1)

    payload = {
        "author": author_urn,
        "commentary": build_caption(folder, meta),
        "visibility": "PUBLIC",
        "distribution": {
            "feedDistribution": "MAIN_FEED",
            "targetEntities": [],
            "thirdPartyDistributionChannels": [],
        },
        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": False,
    }

    content = build_content(image_urns)
    if content:
        payload["content"] = content

    response = request_with_retry(
        "POST",
        f"{API_BASE}/posts",
        headers={**auth_headers(), "Content-Type": "application/json"},
        json=payload,
    )
    response.raise_for_status()

    post_id = response.headers.get("x-restli-id", "unknown")
    print(f"Posted to LinkedIn successfully: {post_id}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python post_to_linkedin.py <folder>")
        sys.exit(1)
    main(sys.argv[1])
