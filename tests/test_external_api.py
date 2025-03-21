import pytest
from unittest.mock import patch
from src.external_api import convert_to_rub


@pytest.mark.parametrize("transaction, expected", [
    ({'amount': 100, 'currency': 'USD'}, 7500.0),  # Пример конвертации USD
    ({'amount': 100, 'currency': 'EUR'}, 8500.0),  # Пример конвертации EUR
    ({'amount': 100, 'currency': 'RUB'}, 100.0),   # Пример конвертации RUB
])
def test_convert_to_rub(transaction, expected):
    """
    Тестирует конвертацию различных валют в RUB.
    """
    if transaction['currency'] in ['USD', 'EUR']:
        with patch('src.external_api.get_exchange_rate', return_value=75 if transaction['currency'] == 'USD' else 85):
            result = convert_to_rub(transaction)
            assert result == expected
    else:
        result = convert_to_rub(transaction)
        assert result == expected


@pytest.mark.parametrize("transaction", [
    {'amount': 100, 'currency': 'GBP'},  # Неподдерживаемая валюта
])
def test_convert_to_rub_invalid_currency(transaction):
    """
    Тестирует обработку не поддерживаемой валюты.
    """
    with pytest.raises(ValueError, match="Валюта не поддерживается: GBP"):
        convert_to_rub(transaction)


@pytest.mark.parametrize("transaction", [
    {'amount': 100, 'currency': 'USD'},  # Тест на получение курса
])
def test_convert_to_rub_api_failure(transaction):
    """
    Тестирует обработку ошибки при получении курса валюты.
    """
    with patch('src.external_api.get_exchange_rate', return_value=None):
        with pytest.raises(ValueError, match="Не удалось получить курс для валюты: USD"):
            convert_to_rub(transaction)
