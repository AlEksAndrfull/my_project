from typing import Any

import pytest

from src.log_decorators import log


@log()
def success_function(x: int, y: int) -> int:
    return x + y


@log()
def error_function(x: int, y: int) -> float:
    return x / y  # Деление на ноль будет поднимать ошибку


@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),  # Пример успешного случая
    (10, 5, 15),  # Другой успешный случай
    (0, 0, 0),    # Сложение нулей
])
def test_success_function(capsys: Any, x: int, y: int, expected: int) -> None:
    result = success_function(x, y)
    assert result == expected

    # Проверка, что сообщение записано в консоль
    captured = capsys.readouterr()
    assert "success_function ok" in captured.out


@pytest.mark.parametrize("x, y", [
    (1, 0),  # Деление на ноль
    (10, 0),  # Другой случай деления на ноль
])
def test_error_function(capsys: Any, x: int, y: int) -> None:
    with pytest.raises(ZeroDivisionError):
        error_function(x, y)

    # Проверка, что сообщение об ошибке записано в консоль
    captured = capsys.readouterr()
    assert "error: division by zero" in captured.out
