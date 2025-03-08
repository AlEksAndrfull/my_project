from typing import List, Tuple

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def card_numbers() -> List[Tuple[str, str]]:
    return [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567812345678", "1234 56** **** 5678"),
        ("0000000000000000", "0000 00** **** 0000"),
        ("", "Некорректный ввод"),  # Проверка пустого ввода
        ("123", "Некорректный ввод"),  # Проверка короткого ввода
    ]


@pytest.fixture
def account_numbers() -> List[Tuple[str, str]]:
    return [
        ("73654108430135874305", "**4305"),
        ("12345678901234567890", "**7890"),
        ("00000000000000000000", "**0000"),
        ("", "Некорректный ввод"),  # Проверка пустого ввода
        ("123", "Некорректный ввод"),  # Проверка короткого ввода
    ]


def test_get_mask_card_number(card_numbers: List[Tuple[str, str]]) -> None:
    for card, expected in card_numbers:
        assert get_mask_card_number(card) == expected


def test_get_mask_account(account_numbers: List[Tuple[str, str]]) -> None:
    for account, expected in account_numbers:
        assert get_mask_account(account) == expected


@pytest.mark.parametrize("card, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1234567812345678", "1234 56** **** 5678"),
    ("0000000000000000", "0000 00** **** 0000"),
    ("", "Некорректный ввод"),  # Проверка пустого ввода
    ("123", "Некорректный ввод"),  # Проверка короткого ввода
])
def test_get_mask_card_number_parametrized(card: str, expected: str) -> None:
    assert get_mask_card_number(card) == expected


@pytest.mark.parametrize("account, expected", [
    ("73654108430135874305", "**4305"),
    ("12345678901234567890", "**7890"),
    ("00000000000000000000", "**0000"),
    ("", "Некорректный ввод"),  # Проверка пустого ввода
    ("123", "Некорректный ввод"),  # Проверка короткого ввода
])
def test_get_mask_account_parametrized(account: str, expected: str) -> None:
    assert get_mask_account(account) == expected
