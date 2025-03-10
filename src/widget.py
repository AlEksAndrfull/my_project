from datetime import datetime


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета.
    Функция принимает строку, содержащую тип карты или счета и его номер,
    и возвращает строку с замаскированным номером.
    """
    if not info or len(info.strip()) == 0:
        raise ValueError("Некорректный ввод")

    parts = info.split()

    if len(parts) < 2:
        raise ValueError("Некорректный ввод")

    number = parts[-1]  # последний элемент - номер карты или счета

    if "Счет" in parts:
        if len(number) < 4 or not number.isdigit():
            raise ValueError("Некорректный номер счета")
        return f"**{number[-4:]}"  # маскировка номера счета
    else:
        if len(number) != 16 or not number.isdigit():
            raise ValueError("Некорректный номер карты")
        return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"  # маскировка номера карты


def get_date(date_str: str) -> str:
    """
    Преобразует строку с датой из формата ISO в формат "ДД.ММ.ГГГГ".
    """
    if not date_str or len(date_str.strip()) == 0:
        return ""

    try:
        date_obj = datetime.fromisoformat(date_str)
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return ""
