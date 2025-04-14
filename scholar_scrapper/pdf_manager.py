import os
import re
import requests
from pathlib import Path
from datetime import datetime
from typing import List

from PyPDF2 import PdfReader

PDF_DIR = Path("pdfs")
PDF_DIR.mkdir(exist_ok=True)

def slugify(text: str) -> str:
    return re.sub(r'\W+', '_', text.strip().lower())[:100]

def extract_year_from_metadata(metadata: dict) -> str:
    # fallback if year not available
    return metadata.get("year", str(datetime.now().year))

def extract_authors(metadata: dict) -> str:
    authors = metadata.get("author", "")
    if isinstance(authors, list):
        return authors[0].split()[-1] if authors else "Unknown"
    return authors.split()[-1] if authors else "Unknown"

def generate_filename(metadata: dict) -> str:
    year = extract_year_from_metadata(metadata)
    author = extract_authors(metadata)
    title = metadata.get("title", "Untitled")
    return f"{year}_{author}_{slugify(title)}.pdf"

def download_pdf(url: str, save_path: Path) -> bool:
    try:
        response = requests.get(url, timeout=10)
        if "application/pdf" in response.headers.get("Content-Type", ""):
            with open(save_path, "wb") as f:
                f.write(response.content)
            return True
    except Exception as e:
        print(f"❌ Error downloading PDF: {e}")
    return False

def save_metadata_pdf(pdf_path: Path, metadata: dict):
    # Optional: Embed metadata in PDF using PyPDF2 (advanced)
    pass

def download_pdfs(results: List[dict]):
    for entry in results:
        pdf_url = entry.get("eprint_url")
        if not pdf_url:
            print(f"❌ No PDF found for: {entry.get('title')}")
            continue

        filename = generate_filename(entry)
        filepath = PDF_DIR / filename

        if filepath.exists():
            print(f"⚠️ Already downloaded: {filename}")
            continue

        print(f"⬇️  Downloading: {filename}")
        if download_pdf(pdf_url, filepath):
            print(f"✅ Saved to {filepath}")
            save_metadata_pdf(filepath, entry)  # optional
        else:
            print(f"❌ Failed to download: {filename}")

