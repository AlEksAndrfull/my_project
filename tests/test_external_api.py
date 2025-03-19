import pytest
from unittest.mock import patch
from src.external_api import convert_currency


@pytest.mark.parametrize("transaction, expected", [
    ({'amount': 100, 'currency': 'USD'}, 7500.0),  # Примерный курс 75
    ({'amount': 100, 'currency': 'EUR'}, 7500.0),  # Примерный курс 75
    ({'amount': 100, 'currency': 'RUB'}, 100.0),    # Без конвертации
])
@patch('src.external_api.requests.get')
def test_convert_currency(mock_get, transaction, expected):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'rates': {'RUB': 75}}

    assert convert_currency(transaction) == expected
