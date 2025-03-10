def get_mask_card_number(card_number: str) -> str:
    """
    Возвращает маску номера банковской карты.
    Параметры:
    card_number (str): Номер карты.
    Возвращает:
    str: Замаскированный номер карты по формату XXXX XX** **** XXXX или сообщение об ошибке.
    """
    if not card_number.isdigit() or len(card_number) != 16:
        return "Некорректный ввод"
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Возвращает маску номера банковского счета.
    Параметры:
    account_number (str): Номер счета.
    Возвращает:
    str: Замаскированный номер счета по формату **XXXX или сообщение об ошибке.
    """
    if not account_number.isdigit() or len(account_number) < 4:
        return "Некорректный ввод"
    return f"**{account_number[-4:]}"
