import pytest

from src.widget import get_date, mask_account_card


# Фикстура для создания входных данных
@pytest.fixture
def account_data() -> list[tuple[str, str]]:
    return [
        ("Visa Platinum 7000792289606361", "7000 79** **** 6361"),
        ("Maestro 1596837868705199", "1596 83** **** 5199"),
        ("Счет 73654108430135874305", "**4305"),
        ("MasterCard 7158300734726758", "7158 00** **** 6758"),
        ("Visa Classic 6831982476737658", "6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "8990 22** **** 2229"),
        ("Счет 64686473678894779589", "**9589"),
        ("Счет 35383033474447895560", "**7860"),
    ]


@pytest.mark.parametrize("input_data, expected_output", [
    ("Visa Platinum 7000792289606361", "7000 79** **** 6361"),
    ("Maestro 1596837868705199", "1596 83** **** 5199"),
    ("Счет 73654108430135874305", "**4305"),
])
def test_mask_account_card(account_data: list[tuple[str, str]], input_data: str, expected_output: str) -> None:
    assert mask_account_card(input_data) == expected_output


def test_mask_account_card_invalid() -> None:
    with pytest.raises(ValueError):
        mask_account_card(" ")  # строка с пробелом
    with pytest.raises(ValueError):
        mask_account_card("")  # пустая строка
    with pytest.raises(ValueError):
        mask_account_card("Некорректный ввод")  # строка без номера карты
    with pytest.raises(ValueError):
        mask_account_card("Счет 123")  # некорректный номер счета


@pytest.mark.parametrize("date_str, expected_output", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2018-07-11T00:00:00", "11.07.2018"),
    ("", ""),  # Проверяем пустую строку
    ("Некорректная дата", ""),  # Проверяем некорректный ввод
])
def test_get_date(date_str: str, expected_output: str) -> None:
    assert get_date(date_str) == expected_output
