import os
import sys
import requests
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import datetime
import random


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

problem_name = folder.name

caption = f"""
🚀 Solved LeetCode Problem: {problem_name}

{text[:1500]}

💻 Solution attached below.
⏰ {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}
🎲 {random.randint(100000, 999999)}

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
print(response.json())
print(response.text)
response.raise_for_status()
