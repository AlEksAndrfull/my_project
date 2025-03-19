import os
import requests


def convert_currency(transaction):
    """
    Конвертирует сумму транзакции в рубли.

    Параметры:
    ----------
    transaction : dict
        Словарь, содержащий информацию о транзакции.
        Должен содержать ключи:
        - 'amount' (float): сумма транзакции.
        - 'currency' (str): валюта транзакции ('USD' или 'EUR').

    Возвращает:
    ----------
    float
        Конвертированная сумма в рублях. Если валюта не 'USD' или 'EUR',
        возвращает сумму без конвертации.

    Исключения:
    -----------
    requests.exceptions.RequestException
        Возникает, если запрос к API не удался.
    KeyError
        Возникает, если в ответе API отсутствует ожидаемое поле 'rates'.
    """

    amount = transaction.get('amount')
    currency = transaction.get('currency')

    if currency not in ['USD', 'EUR']:
        return float(amount)

    api_key = os.getenv('API_KEY')
    url = f'https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB'
    headers = {'apikey': api_key}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        rates = response.json().get('rates', {})
        rub_rate = rates.get('RUB', 1)
        return float(amount) * rub_rate
    return float(amount)
