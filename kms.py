import argparse
from langchain_community.document_loaders import PyPDFLoader
from populate_database import clear_database, add_to_chroma
from pdf_from_zotero import fetch_all_items, download_content, check_zotero_connection
from splitter import split_documents

import os

# Path to the directory containing the PDF files.
DATA_PATH = "/home/t35/kms/data/"

# Dictionary to store the metadata of the documents.
docs = {}

# Clear database if requested.
parser = argparse.ArgumentParser()
parser.add_argument("--reset", action="store_true", help="Reset the database.")
args = parser.parse_args()
if args.reset:
    print("Clearing Database...")
    clear_database()
    print("Database Cleared!")


# Check Zotero connection
# check_zotero_connection()

# Fetch all items from Zotero
# docs = fetch_all_items()
# for key, title in docs.items():
#     print(f"Key: {key} - Title: {title}")

# Download items from Zotero
# for key, title in docs.items():
#     print(f"Downloading {title} ...")
#     download_content(key,title, DATA_PATH)

# Load Docs from DATA_PATH into data 
data = []
pages = []
chunks = []

for filename in os.listdir(DATA_PATH):
    if(filename.endswith(".pdf")):
        file_loader = PyPDFLoader(os.path.join(DATA_PATH, f"{filename}.pdf"))
        data.append(file_loader)

# Create (or update) the data store.
for doc in data:
    for page in doc.pages:
        print(page)
#         pages.append(page)
    
#     chunks = (split_documents(pages))
#     print(f"Split {doc.get("title")} into {len(chunks)} chunks.")
    #add_to_chroma(chunks)
