from bs4 import BeautifulSoup
from typing import List, Dict


# Step 3: Transform - Parse HTML and extract table data
def parse_html(html_content: str) -> List[Dict[str, str]]:
    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.find("table", {"class": "table"})

    # Find all rows in the table
    rows = table.find_all('tr')

    # Extract headers
    headers = [header.get_text(strip=True) for header in rows[0].find_all('th')]

    # Initialize a list to hold the data
    team_data = []

    # Iterate through each row (starting from the second row to skip the headers)
    for row in rows[1:]:
        cols = row.find_all('td')
        # Extract team data from each row
        team = {
            "Team Name": cols[0].get_text(strip=True),
            "Year": cols[1].get_text(strip=True),
            "Wins": cols[2].get_text(strip=True),
            "Losses": cols[3].get_text(strip=True),
            "OT Losses": cols[4].get_text(strip=True),
            "Win %": cols[5].get_text(strip=True),
            "Goals For (GF)": cols[6].get_text(strip=True),
            "Goals Against (GA)": cols[7].get_text(strip=True),
            "+ / -": cols[8].get_text(strip=True),
        }
        team_data.append(team)

    # print(team_data)

    return team_data