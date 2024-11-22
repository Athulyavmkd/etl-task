from typing import List, Dict
from openpyxl import Workbook

# Step 4: Load - Write data to Excel
def write_to_excel(data: List[Dict[str, str]]):
    # Create a new Workbook
    wb = Workbook()
    ws1 = wb.active
    ws1.title = "NHL Stats 1990-2011"

    # Write headers
    headers = ['Team Name', 'Year', 'Wins', 'Losses', 'OT Losses', 'Win %', 'Goals For (GF)', 'Goals Against (GA)', '+ / -']
    ws1.append(headers)

    # Write data rows
    for entry in data:
        row = [
            entry['Team Name'],
            entry['Year'],
            entry['Wins'],
            entry['Losses'],
            entry['OT Losses'],
            entry['Win %'],
            entry['Goals For (GF)'],
            entry['Goals Against (GA)'],
            entry['+ / -']
        ]
        ws1.append(row)

    # Second sheet - Winner and Loser summary
    ws2 = wb.create_sheet(title="Winner and Loser per Year")

    # Write headers to the second sheet
    ws2.append(['Year', 'Winner', 'Winner No. of Wins', 'Loser', 'Loser No. of Wins'])

    # Write winner and loser data to the second sheet
    years = sorted(set(entry['Year'] for entry in data))
    for year in years:
        teams_in_year = [entry for entry in data if entry['Year'] == year]
        # Sort by the number of wins to determine winner and loser
        sorted_teams = sorted(teams_in_year, key=lambda x: x['Wins'], reverse=True)
        winner = sorted_teams[0]
        loser = sorted_teams[-1]
        ws2.append([year, winner['Team Name'], winner['Wins'], loser['Team Name'], loser['Wins']])


    # Save the workbook to a file
    wb.save('NHL_Stats_1990_1991.xlsx')
    print("Data has been written to 'NHL_Stats_1990_1991.xlsx'")