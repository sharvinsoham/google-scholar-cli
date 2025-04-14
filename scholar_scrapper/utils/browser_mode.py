import time
import undetected_chromedriver as uc
from bs4 import BeautifulSoup

def search_browser(query: str, max_results: int = 10):
    query_str = query.replace(" ", "+")
    search_url = f"https://scholar.google.com/scholar?q={query_str}"
    
    # ... rest of scraping logic
    options = uc.ChromeOptions()
    options.headless = True
    driver = uc.Chrome(options=options)
    driver.get(search_url)

    results = []
    while len(results) < max_results:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        for entry in soup.select('.gs_ri'):
            title_tag = entry.select_one('.gs_rt')
            title = title_tag.text if title_tag else ""
            link = title_tag.a['href'] if title_tag and title_tag.a else ""
            authors = entry.select_one('.gs_a').text if entry.select_one('.gs_a') else ""
            snippet = entry.select_one('.gs_rs').text if entry.select_one('.gs_rs') else ""
            pdf_tag = entry.find_previous_sibling('div').find('a')
            pdf_link = pdf_tag['href'] if pdf_tag and pdf_tag['href'].endswith('.pdf') else ""

            results.append({
                "title": title,
                "authors": authors,
                "abstract": snippet,
                "year": "",
                "url": link,
                "pdf": pdf_link
            })

            if len(results) >= max_results:
                break

        next_btn = driver.find_elements("link text", "Next")
        if next_btn:
            next_btn[0].click()
            time.sleep(2)
        else:
            break

    driver.quit()
    return results
