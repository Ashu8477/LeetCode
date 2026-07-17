"""Shared helpers for the LinkedIn automation scripts."""
import json
from pathlib import Path
from typing import Optional

from bs4 import BeautifulSoup

DIFFICULTY_EMOJI = {
    "easy": "🟢",
    "medium": "🟡",
    "hard": "🔴",
}


def parse_readme(folder: Path) -> dict:
    """Extract title, LeetCode URL, difficulty and a plain-text description
    from a LeetHub-style README.md inside `folder`.
    """
    readme_path = folder / "README.md"
    html = readme_path.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html, "html.parser")

    h2 = soup.find("h2")
    link = h2.find("a") if h2 else None
    title = link.get_text(strip=True) if link else folder.name
    url = link.get("href", "") if link else ""

    h3 = soup.find("h3")
    difficulty = h3.get_text(strip=True).lower() if h3 else "unknown"

    # Strip headings/rules before pulling the plain-text problem description
    for tag in soup.find_all(["h2", "h3", "hr"]):
        tag.decompose()

    description = soup.get_text("\n").strip()

    return {
        "title": title,
        "url": url,
        "difficulty": difficulty,
        "description": description,
    }


def get_difficulty_from_stats(stats_path: Path, folder_name: str) -> Optional[str]:
    """Fallback lookup of difficulty from stats.json (maintained by LeetHub)."""
    if not stats_path.exists():
        return None
    try:
        data = json.loads(stats_path.read_text(encoding="utf-8"))
        shas = data.get("leetcode", {}).get("shas", {})
        return shas.get(folder_name, {}).get("difficulty")
    except (json.JSONDecodeError, AttributeError):
        return None


def difficulty_emoji(difficulty: str) -> str:
    return DIFFICULTY_EMOJI.get((difficulty or "").lower(), "⚪")
