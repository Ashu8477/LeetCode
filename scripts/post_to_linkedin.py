import os
import sys
import requests
from pathlib import Path
from bs4 import BeautifulSoup

folder = Path(sys.argv[1])

readme = folder / "README.md"

html = readme.read_text(
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

#leetcode
#python
#dsa
#coding
#developer
#github
"""

payload = {
    "author": f"urn:li:person:{os.environ['LINKEDIN_PERSON_ID']}",
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": caption
            },
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

headers = {
    "Authorization":
        f"Bearer {os.environ['LINKEDIN_ACCESS_TOKEN']}",
    "X-Restli-Protocol-Version": "2.0.0",
    "Content-Type": "application/json"
}

response = requests.post(
    "https://api.linkedin.com/v2/ugcPosts",
    json=payload,
    headers=headers
)

print(response.status_code)
print(response.text)
