import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions() -> list[dict]:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"name": "RUB", "code": "RUB"}
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
    ]


@pytest.mark.parametrize(
    "currency_code, expected_count",
    [
        ("USD", 2),
        ("RUB", 1),
        ("EUR", 0),  # Проверяем валюту, которой нет в тестовых данных
    ]
)
def test_filter_by_currency(sample_transactions: list[dict], currency_code: str, expected_count: int) -> None:
    transactions = list(filter_by_currency(sample_transactions, currency_code))
    assert len(transactions) == expected_count


@pytest.mark.parametrize(
    "start, stop, expected_numbers",
    [
        (1, 5, [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
            "0000 0000 0000 0004",
            "0000 0000 0000 0005"
        ]),
        (10, 12, [
            "0000 0000 0000 0010",
            "0000 0000 0000 0011",
            "0000 0000 0000 0012"
        ]),
    ]
)
def test_card_number_generator(start: int, stop: int, expected_numbers: list[str]) -> None:
    card_numbers = list(card_number_generator(start, stop))
    assert card_numbers == expected_numbers, (
        f"Expected {expected_numbers}, but got {card_numbers}"
    )


def test_transaction_descriptions(sample_transactions: list[dict]) -> None:
    descriptions = list(transaction_descriptions(sample_transactions))
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет"
    ]
    assert descriptions == expected_descriptions
