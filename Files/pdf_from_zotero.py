import requests
import os

API_KEY= "Llf48f3eWeoZz18lsACeHb5K"
LIBRARY_ID = "16178790"
BASE_URL = f"https://api.zotero.org/users/{LIBRARY_ID}/items"


# Header for requests
HEADERS = {
    "Zotero-API-Key": API_KEY,
    "Content-Type": "application/json"
}
response = requests.get(BASE_URL, headers=HEADERS)

# Check API connection with Zotero
def check_zotero_connection():
    if response.status_code == 200:
        print(f"Zotero Status Code: {response.status_code}")
    else:
        print(f"Zotero Fehler Code: {response.status_code}")


# Fetch all items from Zotero
def fetch_all_items():
    docs = {}
    response = requests.get(BASE_URL, headers=HEADERS)
    if response.status_code == 200:
        items = response.json()
        print(f"{len(items)} Documents found")
        for item in items:
            key = item.get("key")
            title = item.get("data", {}).get("title", "No Title")
            docs[key] = title
        return docs
    else:
        print(f"Fehler: {response.status_code}")

# Download items
def download_content(item_key, file_name, download_path):
    url = f"{BASE_URL}/{item_key}/file"
    response = requests.get(url, headers=HEADERS)
    path = os.path.join(download_path, f"{file_name}.pdf")
    if response.status_code == 200:
        with open(path, "wb") as f:
            f.write(response.content)
            print(f"Download finished: {file_name}")
    else:
        print(f"Fehler: {response.status_code} - {response.text}")