import re
from collections import Counter


def find_transactions_by_description(transactions, search_string):
    """
    Ищет транзакции по описанию.
    :param transactions: Список транзакций (словарей).
    :param search_string: Строка для поиска.
    :return: Список найденных транзакций.
    """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    found_transactions = [
        transaction for transaction in transactions
        if pattern.search(transaction.get('description', ''))
    ]
    return found_transactions


def count_transaction_types(transactions):
    """
    Подсчитывает количество транзакций по категориям.
    :param transactions: Список транзакций (словарей).
    :return: Словарь с количеством транзакций по категориям.
    """
    categories = [transaction.get('description', 'Неизвестно') for transaction in transactions]
    return dict(Counter(categories))
