def get_mask_card_number(card_number: int) -> str:
    """
    Возвращает маску номера банковской карты.

    Параметры:
    card_number (int): Номер карты.

    Возвращает:
    str: Замаскированный номер карты по формату XXXX XX** **** XXXX.
    """
    card_str = str(card_number)
    return f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Возвращает маску номера банковского счета.

    Параметры:
    account_number (int): Номер счета.

    Возвращает:
    str: Замаскированный номер счета по формату **XXXX.
    """
    account_str = str(account_number)
    return f"**{account_str[-4:]}"
