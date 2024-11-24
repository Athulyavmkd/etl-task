ETL Task: NHL Hockey Team Stats

Introduction

This project is an ETL (Extract, Transform, Load) pipeline designed to scrape NHL Hockey Team stats from Scrape This Site (https://www.scrapethissite.com/pages/forms/), process the data, and generate two outputs:
1. A ZipFile containing the raw HTML files for all pages.
2. An Excel file with two sheets:
   - Sheet 1: "NHL Stats 1990-2011" – contains all raw data scraped from the site.
   - Sheet 2: "Winner and Loser per Year" – summarizes the team with the most wins and the team with the least wins per year.
The program is written in Python 3, ensuring it is efficient, modular, and testable, with comprehensive unit tests for core calculations.

Prerequisites & Setup
- Python 3 or higher
- Virtual environment (recommended)
- Install dependencies 
   pip install -r requirements.txt

Usage
1. Run the script to execute the ETL pipeline:
   python main.py
   This will:
   - Create a ZIP file named html_pages.zip containing all raw HTML pages.
   - Generate an Excel file named NHL_Stats_1990_1991.xlsx with the processed data.

2. Run tests to verify the functionality:
   pytest
   Test scripts test_fetcher.py, test_html_parser.py,test_excel_generator.py provided in the tests folder.

Outputs
1. Zip File: 
   - File: html_pages.zip
   - Contains: HTML files named 1.html, 2.html, ..., 24.html.

2. Excel File:
   - File: NHL_Stats_1990_1991.xlsx
   - Sheet 1 ("NHL Stats 1990-2011"): Full scraped data.
   - Sheet 2 ("Winner and Loser per Year"): Summary of winners and losers.


Technical Details
- Libraries Used:
  - BeautifulSoup 4: For HTML parsing.
  - aiohttp: For asynchronous HTTP requests.
  - openpyxl: For creating and editing Excel files.
  - pytest: For unit testing.
