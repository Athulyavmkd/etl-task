import pytest
from unittest.mock import AsyncMock, patch

@pytest.mark.asyncio
async def test_scrape_all_pages():
    # Mock HTML responses for all 24 pages
    mock_html_pages = [f"<html><body><h1>Page {i}</h1></body></html>" for i in range(1, 25)]

    # Patch fetch_page to return the mocked pages
    with patch("fetcher.fetch_page", new_callable=AsyncMock) as mock_fetch_page:
        mock_fetch_page.side_effect = mock_html_pages

        # Import and call the function under test
        from fetcher import scrape_all_pages
        html_pages = await scrape_all_pages()

        # Verify the output
        assert len(html_pages) == 24
        for i in range(1, 25):
            assert html_pages[i - 1] == f"<html><body><h1>Page {i}</h1></body></html>"

        # Verify that fetch_page was called 24 times
        assert mock_fetch_page.call_count == 24