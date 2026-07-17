import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

folder = Path(sys.argv[1])

py_file = list(folder.glob("*.py"))[0]

code = py_file.read_text(encoding="utf-8")

lines = code.splitlines()

CHUNK = 45

parts = [
    lines[i:i + CHUNK]
    for i in range(0, len(lines), CHUNK)
]

font = ImageFont.load_default()

for idx, block in enumerate(parts, start=1):

    img = Image.new(
        "RGB",
        (1200, 900),
        (30, 30, 46)
    )

    draw = ImageDraw.Draw(img)

    y = 40

    draw.text(
        (40, 10),
        py_file.name,
        fill=(255, 255, 255),
        font=font
    )

    for line in block:

        draw.text(
            (40, y),
            line,
            fill=(220, 220, 220),
            font=font
        )

        y += 20

    img.save(folder / f"code_{idx}.png")

print("Images generated")
