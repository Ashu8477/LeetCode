"""Generate a cover slide + syntax-highlighted code slides for a solved
LeetCode problem, ready to be posted on LinkedIn.

Usage:
    python generate_images.py <problem-folder>
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from pygments import lex
from pygments.lexers import PythonLexer
from pygments.token import Token

from utils import parse_readme, get_difficulty_from_stats, difficulty_emoji

WIDTH, HEIGHT = 1600, 900
BG_COLOR = (7, 10, 18) # GitHub-dark-style background
LINE_HEIGHT = 38
PADDING = 50
CHUNK_SIZE = 18  # source lines per code slide

TOKEN_COLORS = {
    Token.Keyword: (255, 123, 114),
    Token.Name.Function: (210, 168, 255),
    Token.Name.Class: (255, 166, 87),
    Token.String: (165, 214, 255),
    Token.Number: (121, 192, 255),
    Token.Comment: (139, 148, 158),
    Token.Operator: (255, 123, 114),
    Token.Punctuation: (201, 209, 217),
}
DEFAULT_COLOR = (230, 237, 243)

FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf",
]


def load_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    """Try a few common Ubuntu-runner monospace fonts, falling back to
    Pillow's built-in bitmap font so this never crashes if fonts are
    missing on the runner image.
    """
    candidates = FONT_CANDIDATES
    if bold:
        candidates = [p for p in FONT_CANDIDATES if "Bold" in p] + FONT_CANDIDATES

    for path in candidates:
        if Path(path).exists():
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                continue

    try:
        return ImageFont.load_default(size=size)  # Pillow >= 10.1
    except TypeError:
        return ImageFont.load_default()


def token_color(token_type) -> tuple:
    while token_type is not None:
        if token_type in TOKEN_COLORS:
            return TOKEN_COLORS[token_type]
        token_type = token_type.parent
    return DEFAULT_COLOR


def highlighted_lines(code: str):
    """Return list[list[(text, color)]] -- one entry per source line."""
    lines = [[]]
    for token_type, value in lex(code, PythonLexer()):
        color = token_color(token_type)
        parts = value.split("\n")
        for i, part in enumerate(parts):
            if part:
                lines[-1].append((part, color))
            if i < len(parts) - 1:
                lines.append([])
    return lines


def draw_cover_slide(folder: Path, meta: dict) -> Image.Image:
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    title_font = load_font(42, bold=True)
    meta_font = load_font(28)
    body_font = load_font(24)

    difficulty_colors = {
        "easy": (46, 204, 113),
        "medium": (241, 196, 15),
        "hard": (231, 76, 60),
    }

    diff_color = difficulty_colors.get(
        meta["difficulty"],
        (255, 255, 255),
    )

    emoji = difficulty_emoji(meta["difficulty"])

    diff_label = (
        meta["difficulty"].capitalize()
        if meta["difficulty"] != "unknown"
        else ""
    )

    draw.text(
        (PADDING, 60),
        "🚀 LEETCODE SOLVED",
        fill=(88, 166, 255),
        font=meta_font,
    )

    draw.text(
        (PADDING, 140),
        meta["title"],
        fill=(255, 255, 255),
        font=title_font,
    )

    if diff_label:
        draw.text(
            (PADDING, 220),
            f"{emoji} {diff_label}",
            fill=diff_color,
            font=meta_font,
        )

    draw.rounded_rectangle(
        [(50, 300), (1550, 650)],
        radius=20,
        fill=(22, 27, 34),
        outline=(48, 54, 61),
        width=3,
    )

    approach = meta.get(
        "approach",
        "Optimized solution using an efficient algorithm."
    )

    complexities = [
        "⚡ Time Complexity: O(n)",
        "📦 Space Complexity: O(1)",
    ]

    draw.text(
        (90, 340),
        "🧠 Approach",
        fill=(88, 166, 255),
        font=meta_font,
    )

    draw.text(
        (90, 410),
        approach,
        fill=(230, 237, 243),
        font=body_font,
    )

    draw.text(
        (90, 510),
        complexities[0],
        fill=(241, 196, 15),
        font=body_font,
    )

    draw.text(
        (90, 560),
        complexities[1],
        fill=(46, 204, 113),
        font=body_font,
    )

    draw.text(
        (PADDING, HEIGHT - 70),
        "github.com/Ashu8477",
        fill=(139, 148, 158),
        font=body_font,
    )

    return img


def draw_code_slide(py_file_name: str, chunk_lines, start_line: int, part: int, total_parts: int) -> Image.Image:
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    header_font = load_font(26, bold=True)
    code_font = load_font(28)

    draw.text((PADDING, 30), py_file_name, fill=(88, 166, 255), font=header_font)
    draw.text((WIDTH - PADDING - 150, 30), f"part {part}/{total_parts}", fill=(139, 148, 158), font=header_font)
    draw.line([(PADDING, 75), (WIDTH - PADDING, 75)], fill=(48, 54, 61), width=2)
    draw.rounded_rectangle(
        [(35, 90), (1565, 850)],
        radius=18,
        fill=(22, 27, 34),
        outline=(48, 54, 61),
        width=2,
    )

    y = 120
    for idx, line_tokens in enumerate(chunk_lines):
        line_no = start_line + idx + 1
        draw.text((PADDING, y), f"{line_no:>3}", fill=(88, 96, 105), font=code_font)
        x = PADDING + 70
        for text, color in line_tokens:
            draw.text((x, y), text, fill=color, font=code_font)
            x += draw.textlength(text, font=code_font)
        y += LINE_HEIGHT
    return img


def main(folder_arg: str) -> None:
    folder = Path(folder_arg)
    if not folder.is_dir():
        print(f"::error::Folder '{folder}' does not exist.")
        sys.exit(1)

    py_files = sorted(folder.glob("*.py"))
    if not py_files:
        print(f"::error::No .py file found in {folder}")
        sys.exit(1)
    py_file = py_files[0]

    meta = parse_readme(folder)
    if meta["difficulty"] == "unknown":
        fallback = get_difficulty_from_stats(Path("stats.json"), folder.name)
        if fallback:
            meta["difficulty"] = fallback

    cover = draw_cover_slide(folder, meta)
    cover.save(folder / "cover.png")

    code = py_file.read_text(encoding="utf-8")
    lines = highlighted_lines(code)
    while lines and not lines[-1]:
    lines.pop()

    starts = list(range(0, len(lines), CHUNK_SIZE)) or [0]
    chunks = [lines[s:s + CHUNK_SIZE] for s in starts]
    total_parts = len(chunks)

    for part, (start, chunk) in enumerate(zip(starts, chunks), start=1):
        slide = draw_code_slide(py_file.name, chunk, start, part, total_parts)
        slide.save(folder / f"code_{part}.png")

    print(f"Generated 1 cover slide + {total_parts} code slide(s) for {folder.name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_images.py <folder>")
        sys.exit(1)
    main(sys.argv[1])
