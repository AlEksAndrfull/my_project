from typing import Dict, Iterator, List


def filter_by_currency(transactions: List[Dict],
                       currency_code: str) -> Iterator[Dict]:
    """
    Фильтрует транзакции по валюте и возвращает итератор.

    :param transactions: Список транзакций,
    где каждая транзакция представлена в виде словаря.
    :param currency_code: Код валюты,
    по которой необходимо фильтровать транзакции.
    :return: Итератор, который поочередно выдает транзакции,
    где валюта соответствует заданному коду.

    Пример использования:
    >>> transactions = [{"operationAmount":
    {"currency": {"code": "USD"}}}, ...]
    >>> filtered = filter_by_currency(transactions, "USD")
    >>> for transaction in filtered:
    ...     print(transaction)
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Возвращает описания транзакций по очереди.

    :param transactions: Список транзакций,
    где каждая транзакция представлена в виде словаря.
    :return: Итератор, который поочередно выдает описания транзакций.

    Пример использования:
    >>> transactions = [{"description": "Перевод"}, ...]
    >>> descriptions = transaction_descriptions(transactions)
    >>> for desc in descriptions:
    ...     print(desc)
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор банковских карт в формате XXXX XXXX XXXX XXXX.

    :param start: Начальное значение диапазона для генерации номеров карт.
    :param stop: Конечное значение диапазона для генерации номеров карт.
    :return: Итератор,
    который выдает номера карт в формате 'XXXX XXXX XXXX XXXX'.

    Пример использования:
    >>> for card_number in card_number_generator(1, 5):
    ...     print(card_number)
    """
    for number in range(start, stop + 1):
        yield (
            f"{number:016d}"[:4] + " " +
            f"{number:016d}"[4:8] + " " +
            f"{number:016d}"[8:12] + " " +
            f"{number:016d}"[12:]
        )
