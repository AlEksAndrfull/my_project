import pytest
from unittest.mock import patch, MagicMock
from src.finance import read_csv, read_excel
import os


# Параметризация для тестирования read_csv
@pytest.mark.parametrize("mock_data, expected", [
    (MagicMock(to_dict=lambda orient: [{'id': 1, 'amount': 100}]), [{'id': 1, 'amount': 100}]),
    (MagicMock(to_dict=lambda orient: [{'id': 2, 'amount': 200}]), [{'id': 2, 'amount': 200}]),
])
@patch('pandas.read_csv')
def test_read_csv(mock_read_csv, mock_data, expected):
    mock_read_csv.return_value = mock_data

    result = read_csv('dummy_path.csv')
    assert result == expected
    mock_read_csv.assert_called_once_with('dummy_path.csv')


@patch('pandas.read_csv')
def test_read_csv_file_not_found(mock_read_csv):
    mock_read_csv.side_effect = FileNotFoundError
    result = read_csv('dummy_path.csv')
    assert result == []


# Параметризация для тестирования read_excel
@pytest.mark.parametrize("mock_data, expected", [
    (MagicMock(to_dict=lambda orient: [{'id': 1, 'amount': 200}]), [{'id': 1, 'amount': 200}]),
    (MagicMock(to_dict=lambda orient: [{'id': 2, 'amount': 400}]), [{'id': 2, 'amount': 400}]),
])
@patch('pandas.read_excel')
def test_read_excel(mock_read_excel, mock_data, expected):
    mock_read_excel.return_value = mock_data

    result = read_excel('dummy_path.xlsx')
    assert result == expected
    mock_read_excel.assert_called_once_with('dummy_path.xlsx')


@patch('pandas.read_excel')
def test_read_excel_file_not_found(mock_read_excel):
    mock_read_excel.side_effect = FileNotFoundError
    result = read_excel('dummy_path.xlsx')
    assert result == []


def test_read_csv_with_real_file():
    csv_file_path = os.path.join('data', 'transactions.csv')
    result = read_csv(csv_file_path)
    assert isinstance(result, list)
    assert len(result) > 0


def test_read_excel_with_real_file():
    excel_file_path = os.path.join('data', 'transactions_excel.xlsx')
    result = read_excel(excel_file_path)
    assert isinstance(result, list)
    assert len(result) > 0
