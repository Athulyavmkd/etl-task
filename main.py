import asyncio
from fetcher import scrape_all_pages
from html_parser import parse_html
from excel_generator import write_to_excel
from zipper import create_zipfile

BASE_URL = "https://www.scrapethissite.com/pages/forms/"
OUTPUT_FOLDER = "html_pages"
EXCEL_FILE = "nhl_stats.xlsx"

# Main ETL pipeline
async def main():
    html_pages = await scrape_all_pages()
    all_rows = []
    for html_content in html_pages:
        if html_content:
            all_rows.extend(parse_html(html_content))

    # print(all_rows)
    write_to_excel(all_rows)
    create_zipfile()

if __name__ == "__main__":
    asyncio.run(main())
