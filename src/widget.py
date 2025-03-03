def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета.
    Функция принимает строку, содержащую тип карты или счета и его номер,
    и возвращает строку с замаскированным номером.

    Параметры:
    info (str): Строка, содержащая тип карты или счета и его номер.

    Возвращает:
    str: Строка с замаскированным номером карты или счета.
    """
    parts = info.split()
    number = parts[-1]  # последний элемент - номер карты или счета
    if "Счет" in parts:
        return f"**{number[-4:]}"  # маскировка номера счета
    else:
        return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"  # маскировка номера карты

def get_date(date_str: str) -> str:
    """
    Преобразует строку с датой из формата ISO в формат "ДД.ММ.ГГГГ".

    Параметры:
    date_str (str): Строка с датой в формате ISO.

    Возвращает:
    str: Строка с датой в формате "ДД.ММ.ГГГГ".
    """
    from datetime import datetime
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")

if __name__ == "__main__":
    # Примеры использования функций
    print(mask_account_card("Visa Platinum 7000792289606361"))  # "7000 79** **** 6361"
    print(mask_account_card("Счет 73654108430135874305"))      # "**4305"
    print(get_date("2024-03-11T02:26:18.671407"))              # "11.03.2024"
