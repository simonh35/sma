import argparse
import os
from langchain_community.document_loaders import PyPDFLoader, PyPDFDirectoryLoader
from populate_database import clear_database, add_to_chroma
from pdf_from_zotero import fetch_all_items, download_content, check_zotero_connection
from splitter import split_documents
from dotenv import load_dotenv, find_dotenv

# Dictionary to store the metadata of the documents.
zotero_metadata = {}

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
# zotero_metadata = fetch_all_items()
# for key, title in zotero_metadata.items():
#     print(f"Key: {key} - Title: {title}")

# Download items from Zotero
# for key, title in zotero_metadata.items():
#     print(f"Downloading {title} ...")
#     download_content(key,title, DATA_PATH)

# Load Docs from DATA_PATH into data 
data = {}
data_path = os.getenv("DATA_PATH")

# Load all PDFs from DATA_PATH and Split them into chunks
for filename in os.listdir(data_path):
    if(filename.endswith(".pdf")):
        loader = PyPDFLoader(f"{data_path+filename}")
        doc = loader.load()
        chunks = split_documents(doc)
        # data[filename] = doc
        print(f"Split {filename} into {len(chunks)} chunks.")
        add_to_chroma(chunks)

