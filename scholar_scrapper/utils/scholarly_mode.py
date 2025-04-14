from scholarly import scholarly
import csv
import os
import requests
import re

def search_scholarly(query, max_results=10):
    search_results = scholarly.search_pubs(query)
    papers = []

    for _ in range(max_results):
        paper = next(search_results)
        papers.append({
            "title": paper.get("bib", {}).get("title", ""),
            "authors": paper.get("bib", {}).get("author", ""),
            "abstract": paper.get("bib", {}).get("abstract", ""),
            "year": paper.get("bib", {}).get("pub_year", ""),
            "url": paper.get("pub_url", ""),
            "pdf": ""
        })

    return papers


def slugify(query):
    # Turn query into a safe filename
    return re.sub(r'\W+', '_', query.strip().lower())
    
def save_to_csv(results, query="results"):
    base_name = slugify(query)
    file_name = f"{base_name}.csv"
    counter = 1

    while os.path.exists(file_name):
        file_name = f"{base_name}_{counter}.csv"
        counter += 1

    with open(file_name, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    print(f"✅ Saved to {file_name}")

          


def slugify(text):
    return re.sub(r'\W+', '_', text.strip().lower())[:80]

def download_pdfs(results, output_dir="pdfs"):
    Path(output_dir).mkdir(exist_ok=True)

    for paper in results:
        title = paper.get("title", "Untitled")
        pdf_url = paper.get("eprint_url")

        if not pdf_url:
            print(f"❌ No PDF link found for: {title}")
            continue

        try:
            response = requests.get(pdf_url, timeout=10)
            if response.headers.get("Content-Type", "").lower() != "application/pdf":
                print(f"⚠️ Skipped non-PDF content: {title}")
                continue

            filename = slugify(title) + ".pdf"
            filepath = os.path.join(output_dir, filename)

            with open(filepath, "wb") as f:
                f.write(response.content)

            print(f"✅ Downloaded: {title}")

        except Exception as e:
            print(f"❌ Failed to download {title}: {e}")
