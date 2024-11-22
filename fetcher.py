import aiohttp
import os
from typing import List, Dict
import asyncio

BASE_URL = "https://www.scrapethissite.com/pages/forms/"
OUTPUT_FOLDER = "html_pages"
START_PAGE = 1
NO_OF_PAGES = 25

# Step 1: Extract - Function to fetch a single page
async def fetch_page(session: aiohttp.ClientSession, url: str, page_number: int) -> str:
    try:
        async with session.get(url, timeout=10) as response:
            if response.status == 200:
                html_content = await response.text()
                os.makedirs(OUTPUT_FOLDER, exist_ok=True)
                file_path = os.path.join(OUTPUT_FOLDER, f"{page_number}.html")
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(html_content)
                return html_content
            else:
                raise Exception(f"Failed to fetch page {page_number}. HTTP Status: {response.status}")
    except Exception as e:
        print(f"Error fetching page {page_number}: {e}")
        return ""

# Step 2: Extract - Scrape all pages asynchronously
async def scrape_all_pages() -> List[str]:
    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_page(session, f"{BASE_URL}?page_num={i}", i)
            for i in range(START_PAGE, NO_OF_PAGES)
        ]
        return await asyncio.gather(*tasks)