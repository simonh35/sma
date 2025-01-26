import argparse
import PyPDF2
from langchain_community.document_loaders import PyPDFLoader, PyPDFDirectoryLoader
from populate_database import clear_database, add_to_chroma
from pdf_from_zotero import fetch_all_items, download_content, check_zotero_connection
from splitter import split_documents

import os

# Path to the directory containing the PDF files.
DATA_PATH = "/home/t35/kms/data/"

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

# Load the PDF files into the data dictionary.
for filename in os.listdir(DATA_PATH):
    if(filename.endswith(".pdf")):
        loader = PyPDFLoader(f"{DATA_PATH+filename}")
        doc = loader.load()
        chunks = split_documents(doc)
        # data[filename] = doc
        print(f"Split {filename} into {len(chunks)} chunks.")
        add_to_chroma(chunks)

