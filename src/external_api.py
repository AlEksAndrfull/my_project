import os
import requests


def get_exchange_rate(currency):
    """
    Получает текущий курс валюты к рублю.

    :param currency: Строка, обозначающая код валюты (например, 'USD', 'EUR').
    :return: Курс валюты к рублю в виде float, если курс получен успешно; иначе None.
    """
    api_key = os.getenv('API_KEY')
    url = f'https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB'
    headers = {'apikey': api_key}

    response = requests.get(url, headers=headers)
    data = response.json()

    if response.status_code == 200 and 'rates' in data:
        return data['rates']['RUB']
    return None


def convert_to_rub(transaction):
    """
    Конвертирует сумму транзакции в рубли.

    :param transaction: Словарь с данными транзакции, содержащий ключи:
                       - 'amount': сумма транзакции (float или int)
                       - 'currency': код валюты (строка), по умолчанию 'RUB'.
    :return: Сумма в рублях в виде float.
    :raises ValueError: Если валюта не поддерживается или не удалось получить курс.
    """
    amount = transaction['amount']
    currency = transaction.get('currency', 'RUB')  # По умолчанию считаем, что валюта RUB

    if currency == 'RUB':
        return float(amount)  # Если валюта уже в рублях, просто возвращаем сумму

    # Если валюта USD или EUR, получаем курс и конвертируем
    if currency in ['USD', 'EUR']:
        rate = get_exchange_rate(currency)
        if rate is not None:
            return float(amount) * rate  # Конвертируем сумму в рубли
        else:
            raise ValueError(f"Не удалось получить курс для валюты: {currency}")

    # Если валюта не поддерживается, можно вернуть None или выбросить исключение
    raise ValueError(f"Валюта не поддерживается: {currency}")
