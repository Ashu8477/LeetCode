"""Upload the generated slide images (cover + code_*) for a problem folder
to Cloudinary and store the resulting URLs alongside the images.

Note: this upload is kept as a public archive/backup of the slides. The
actual image attached to the LinkedIn post is uploaded separately straight
to LinkedIn's own Images API in post_to_linkedin.py, because LinkedIn does
not accept arbitrary external image URLs as post media.

Usage:
    python upload_to_cloudinary.py <problem-folder>
"""
import json
import os
import sys
from pathlib import Path
from typing import List

import cloudinary
import cloudinary.uploader


def configure_cloudinary() -> None:
    cloudinary.config(
        cloud_name=os.environ["CLOUDINARY_CLOUD_NAME"],
        api_key=os.environ["CLOUDINARY_API_KEY"],
        api_secret=os.environ["CLOUDINARY_API_SECRET"],
        secure=True,
    )


def collect_images(folder: Path) -> List[Path]:
    cover = folder / "cover.png"
    images = ([cover] if cover.exists() else []) + sorted(folder.glob("code_*.png"))
    return images


def main(folder_arg: str) -> None:
    folder = Path(folder_arg)
    images = collect_images(folder)

    if not images:
        print(f"::warning::No images found in {folder} to upload.")
        (folder / "image_urls.json").write_text("[]", encoding="utf-8")
        return

    configure_cloudinary()

    uploaded = []
    for image in images:
        try:
            result = cloudinary.uploader.upload(
                str(image),
                folder=f"leetcode-linkedin/{folder.name}",
                overwrite=True,
            )
            uploaded.append({"file": image.name, "url": result["secure_url"]})
            print(f"Uploaded {image.name} -> {result['secure_url']}")
        except Exception as exc:  # noqa: BLE001 -- one failed image shouldn't kill the run
            print(f"::warning::Failed to upload {image.name}: {exc}")

    (folder / "image_urls.json").write_text(
        json.dumps(uploaded, indent=2), encoding="utf-8"
    )
    print(f"Saved {len(uploaded)} URL(s) to {folder / 'image_urls.json'}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python upload_to_cloudinary.py <folder>")
        sys.exit(1)
    main(sys.argv[1])
