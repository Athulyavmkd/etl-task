import pytest
from unittest.mock import MagicMock, patch
from excel_generator import write_to_excel
from openpyxl import Workbook


@pytest.fixture
def sample_data():
    return [
        {
            'Team Name': 'Team A',
            'Year': '1990',
            'Wins': 50,
            'Losses': 20,
            'OT Losses': 5,
            'Win %': 0.625,
            'Goals For (GF)': 200,
            'Goals Against (GA)': 150,
            '+ / -': 50
        },
        {
            'Team Name': 'Team B',
            'Year': '1990',
            'Wins': 30,
            'Losses': 35,
            'OT Losses': 10,
            'Win %': 0.375,
            'Goals For (GF)': 180,
            'Goals Against (GA)': 210,
            '+ / -': -30
        },
        {
            'Team Name': 'Team C',
            'Year': '1991',
            'Wins': 45,
            'Losses': 25,
            'OT Losses': 5,
            'Win %': 0.600,
            'Goals For (GF)': 190,
            'Goals Against (GA)': 160,
            '+ / -': 30
        },
        {
            'Team Name': 'Team D',
            'Year': '1991',
            'Wins': 25,
            'Losses': 45,
            'OT Losses': 5,
            'Win %': 0.250,
            'Goals For (GF)': 150,
            'Goals Against (GA)': 220,
            '+ / -': -70
        },
    ]


@patch('excel_generator.Workbook')
def test_write_to_excel(mock_workbook, sample_data):
    # Arrange
    mock_wb_instance = MagicMock()
    mock_workbook.return_value = mock_wb_instance
    mock_ws1 = MagicMock()
    mock_ws2 = MagicMock()
    mock_wb_instance.active = mock_ws1
    mock_wb_instance.create_sheet.return_value = mock_ws2

    # Act
    write_to_excel(sample_data)

    # Assert
    # Check if Workbook is created
    mock_workbook.assert_called_once()
    mock_ws1.title = "NHL Stats 1990-2011"
    assert mock_ws1.append.call_count > 0  # Headers and data rows added

    # Verify data written to the first sheet
    expected_headers = ['Team Name', 'Year', 'Wins', 'Losses', 'OT Losses', 'Win %', 'Goals For (GF)', 'Goals Against (GA)', '+ / -']
    mock_ws1.append.assert_any_call(expected_headers)
    for entry in sample_data:
        mock_ws1.append.assert_any_call([
            entry['Team Name'],
            entry['Year'],
            entry['Wins'],
            entry['Losses'],
            entry['OT Losses'],
            entry['Win %'],
            entry['Goals For (GF)'],
            entry['Goals Against (GA)'],
            entry['+ / -']
        ])

    # Verify second sheet is created and data is written
    mock_wb_instance.create_sheet.assert_called_once_with(title="Winner and Loser per Year")
    mock_ws2.append.assert_any_call(['Year', 'Winner', 'Winner No. of Wins', 'Loser', 'Loser No. of Wins'])

    # Verify winners and losers were computed correctly
    mock_ws2.append.assert_any_call(['1990', 'Team A', 50, 'Team B', 30])
    mock_ws2.append.assert_any_call(['1991', 'Team C', 45, 'Team D', 25])

    # Ensure the workbook save method is called
    mock_wb_instance.save.assert_called_once_with('NHL_Stats_1990_1991.xlsx')
