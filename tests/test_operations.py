import pytest
from src.operations import find_transactions_by_description, count_transaction_types


# Тестовые данные
transactions = [
    {"description": "Оплата в магазине", "amount": 100},
    {"description": "Перевод на счет", "amount": 200},
    {"description": "Оплата за интернет", "amount": 50},
    {"description": "Оплата в магазине", "amount": 150},
    {"description": "Перевод на счет", "amount": 300},
]


@pytest.mark.parametrize("search_string, expected", [
    ("магазин", [
        {"description": "Оплата в магазине", "amount": 100},
        {"description": "Оплата в магазине", "amount": 150}
    ]),
    ("перевод", [
        {"description": "Перевод на счет", "amount": 200},
        {"description": "Перевод на счет", "amount": 300}
    ]),
    ("интернет", [
        {"description": "Оплата за интернет", "amount": 50}
    ]),
    ("неизвестно", []),
])
def test_find_transactions_by_description(search_string, expected):
    result = find_transactions_by_description(transactions, search_string)
    assert result == expected


@pytest.mark.parametrize("expected_count", [
    ({"Оплата в магазине": 2, "Перевод на счет": 2, "Оплата за интернет": 1}),
])
def test_count_transaction_types(expected_count):
    result = count_transaction_types(transactions)
    assert result == expected_count
