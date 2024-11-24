import pytest
from html_parser import parse_html

# Sample valid HTML content
sample_html = """
<html>
    <body>
        <table class="table">
            <tr>
                <th>Team Name</th><th>Year</th><th>Wins</th><th>Losses</th><th>OT Losses</th><th>Win %</th><th>Goals For (GF)</th><th>Goals Against (GA)</th><th>+ / -</th>
            </tr>
            <tr>
                <td>Team A</td><td>1990</td><td>10</td><td>5</td><td>2</td><td>0.600</td><td>120</td><td>100</td><td>+20</td>
            </tr>
            <tr>
                <td>Team B</td><td>1991</td><td>15</td><td>3</td><td>0</td><td>0.750</td><td>150</td><td>80</td><td>+70</td>
            </tr>
        </table>
    </body>
</html>
"""

# Test case 1: Valid HTML with proper table data
def test_parse_html_valid():
    result = parse_html(sample_html)
    expected_result = [
        {
            "Team Name": "Team A",
            "Year": "1990",
            "Wins": "10",
            "Losses": "5",
            "OT Losses": "2",
            "Win %": "0.600",
            "Goals For (GF)": "120",
            "Goals Against (GA)": "100",
            "+ / -": "+20",
        },
        {
            "Team Name": "Team B",
            "Year": "1991",
            "Wins": "15",
            "Losses": "3",
            "OT Losses": "0",
            "Win %": "0.750",
            "Goals For (GF)": "150",
            "Goals Against (GA)": "80",
            "+ / -": "+70",
        }
    ]
    assert result == expected_result