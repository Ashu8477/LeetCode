import os
import json
import sys
from pathlib import Path

import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name=os.environ["CLOUDINARY_CLOUD_NAME"],
    api_key=os.environ["CLOUDINARY_API_KEY"],
    api_secret=os.environ["CLOUDINARY_API_SECRET"]
)

folder = Path(sys.argv[1])

urls = []

for image in sorted(folder.glob("code_*.png")):

    result = cloudinary.uploader.upload(str(image))

    urls.append(result["secure_url"])

with open("image_urls.json", "w") as f:
    json.dump(urls, f)

print(urls)
