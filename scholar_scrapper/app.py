import typer
from scholar_scrapper.utils.scholarly_mode import search_scholarly, save_to_csv, download_pdfs
from scholar_scrapper.utils.browser_mode import search_browser

app = typer.Typer()


@app.command()
def scrape(
    query: str = typer.Option(..., help="Search query for Google Scholar"),
    max_results: int = typer.Option(10, help="Max number of results"),
    save: bool = typer.Option(False, help="Save results to a CSV named after the query"),
    download_pdf: bool = typer.Option(False, help="Download available PDFs"),
    browser_fallback: bool = typer.Option(False, help="Use browser-based fallback if scholarly fails")
):
    typer.echo(f"🔍 Searching for: {query}")
    
    results = []
    try:
        results = search_scholarly(query, max_results)
        typer.echo("✅ Fetched results using `scholarly` (no browser).")
    except Exception as e:
        typer.echo(f"⚠️ Scholarly failed: {e}")
        if browser_fallback:
            typer.echo("🔁 Switching to browser-based scraping...")
            results = search_browser(query, max_results)
        else:
            typer.echo("❌ Use `--browser-fallback` to enable fallback mode.")
            raise typer.Exit()

    if save:
        save_to_csv(results, query)
        typer.echo("📁 Results saved to CSV")

    if download_pdf:
        download_pdfs(results)
        typer.echo("📄 Attempted PDF downloads.")


if __name__ == "__main__":
    app()