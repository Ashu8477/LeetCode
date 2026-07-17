import os
import sys
import requests
from pathlib import Path
from bs4 import BeautifulSoup

folder = Path(sys.argv[1])

readme_file = folder / "README.md"

html = readme_file.read_text(
    encoding="utf-8",
    errors="ignore"
)

text = BeautifulSoup(
    html,
    "html.parser"
).get_text("\n")

caption = f"""
🚀 Solved a new LeetCode problem

{text[:2500]}

💻 Solution attached below.

#leetcode #dsa #python #coding #developer #github
"""

payload = {
    "author": f"urn:li:person:{os.environ['LINKEDIN_PERSON_ID']}",
    "commentary": caption,
    "visibility": "PUBLIC",
    "distribution": {
        "feedDistribution": "MAIN_FEED",
        "targetEntities": [],
        "thirdPartyDistributionChannels": []
    },
    "lifecycleState": "PUBLISHED",
    "isReshareDisabledByAuthor": False
}

headers = {
    "Authorization":
        f"Bearer {os.environ['LINKEDIN_ACCESS_TOKEN']}",
    "Content-Type": "application/json",
    "LinkedIn-Version": "202507"

    
}

response = requests.post(
    "https://api.linkedin.com/rest/posts",
    json=payload,
    headers=headers
)

print(response.status_code)
print(response.text)
response.raise_for_status()
