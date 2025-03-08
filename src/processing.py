from typing import List, Dict, Optional


def filter_by_state(transactions: List[Dict[str, str]], state: Optional[str] = 'EXECUTED') -> List[Dict[str, str]]:
    """
    Фильтрует список операций по указанному состоянию.

    :param transactions: Список словарей с данными о банковских операциях.
    :param state: Строка, указывающая состояние операции для фильтрации.
    :return: Новый список словарей, содержащий только операции с указанным состоянием.
    """
    return [transaction for transaction in transactions if transaction.get('state') == state]


def sort_by_date(transactions: List[Dict[str, str]], descending: bool = True) -> List[Dict[str, str]]:
    """
    Сортирует список операций по дате.

    :param transactions: Список словарей с данными о банковских операциях.
    :return: Новый список словарей, отсортированный по дате.
    """
    return sorted(transactions, key=lambda x: x['date'], reverse=descending)
