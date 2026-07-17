from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import sys

folder = Path(sys.argv[1])

py_file = next(folder.glob("*.py"))

code = py_file.read_text(encoding="utf-8").splitlines()

CHUNK_SIZE = 40

font = ImageFont.load_default()

for idx, start in enumerate(range(0, len(code), CHUNK_SIZE), start=1):

    chunk = code[start:start + CHUNK_SIZE]

    img = Image.new("RGB", (1400, 1000), (30, 30, 30))

    draw = ImageDraw.Draw(img)

    y = 40

    draw.text(
        (40, 10),
        py_file.name,
        fill=(255, 255, 255),
        font=font
    )

    for line in chunk:
        draw.text(
            (40, y),
            line,
            fill=(220, 220, 220),
            font=font
        )
        y += 25

    img.save(folder / f"code_{idx}.png")

print("Done")
