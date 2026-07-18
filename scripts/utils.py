"""Shared helpers for the LinkedIn automation scripts."""

import json
import re
from pathlib import Path
from typing import Optional

from bs4 import BeautifulSoup

DIFFICULTY_EMOJI = {
    "easy": "🟢",
    "medium": "🟡",
    "hard": "🔴",
}


def extract_complexity(text: str, keyword: str, default: str):
    pattern = rf"{keyword}.*?(O\([^)]+\))"

    match = re.search(
        pattern,
        text,
        re.IGNORECASE | re.DOTALL,
    )

    if match:
        return match.group(1)

    return default


def parse_readme(folder: Path) -> dict:
    """
    Extract:

    - title
    - url
    - difficulty
    - description
    - approach
    - time complexity
    - space complexity
    """

    readme_path = folder / "README.md"

    html = readme_path.read_text(
        encoding="utf-8",
        errors="ignore",
    )

    soup = BeautifulSoup(html, "html.parser")

    h2 = soup.find("h2")
    link = h2.find("a") if h2 else None

    title = link.get_text(strip=True) if link else folder.name
    url = link.get("href", "") if link else ""

    h3 = soup.find("h3")

    difficulty = (
        h3.get_text(strip=True).lower()
        if h3
        else "unknown"
    )

    full_text = soup.get_text("\n")

    # Remove title + difficulty sections

    for tag in soup.find_all(
        ["h1", "h2", "h3", "hr"]
    ):
        tag.decompose()

    description = soup.get_text("\n").strip()

    description = " ".join(description.split())

    description = description[:350]

    # ---------- Approach ----------

    approach = ""

    keywords = [
        "approach",
        "intuition",
        "algorithm",
        "idea",
    ]

    lower_text = full_text.lower()

    for word in keywords:
        idx = lower_text.find(word)

        if idx != -1:
            approach = full_text[idx: idx + 250]
            break

    if not approach:
        approach = (
            "Optimized solution using an efficient algorithm."
        )

    approach = " ".join(approach.split())

    # ---------- Complexity ----------

    time_complexity = extract_complexity(
        full_text,
        "time complexity",
        "O(n)",
    )

    space_complexity = extract_complexity(
        full_text,
        "space complexity",
        "O(1)",
    )

    return {
        "title": title,
        "url": url,
        "difficulty": difficulty,
        "description": description,
        "approach": approach,
        "time_complexity": time_complexity,
        "space_complexity": space_complexity,
    }


def get_difficulty_from_stats(
    stats_path: Path,
    folder_name: str,
) -> Optional[str]:

    if not stats_path.exists():
        return None

    try:
        data = json.loads(
            stats_path.read_text(
                encoding="utf-8"
            )
        )

        shas = data.get(
            "leetcode",
            {}
        ).get(
            "shas",
            {}
        )

        return shas.get(
            folder_name,
            {}
        ).get(
            "difficulty"
        )

    except (
        json.JSONDecodeError,
        AttributeError,
    ):
        return None


def difficulty_emoji(
    difficulty: str,
) -> str:

    return DIFFICULTY_EMOJI.get(
        (difficulty or "").lower(),
        "⚪",
    )
