import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logs/masks.log', mode='w')
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """
    Возвращает маску номера банковской карты.
    Параметры:
    card_number (str): Номер карты.
    Возвращает:
    str: Замаскированный номер карты по формату XXXX XX** **** XXXX или сообщение об ошибке.
    """
    if not card_number.isdigit() or len(card_number) != 16:
        logger.warning(f"Некорректный ввод номера карты: {card_number}.")
        return "Некорректный ввод"
    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.info(f"Замаскированный номер карты: {masked_number}.")
    return masked_number


def get_mask_account(account_number: str) -> str:
    """
    Возвращает маску номера банковского счета.
    Параметры:
    account_number (str): Номер счета.
    Возвращает:
    str: Замаскированный номер счета по формату **XXXX или сообщение об ошибке.
    """
    if not account_number.isdigit() or len(account_number) < 4:
        logger.warning(f"Некорректный ввод номера счета: {account_number}.")
        return "Некорректный ввод"
    masked_account = f"**{account_number[-4:]}"
    logger.info(f"Замаскированный номер счета: {masked_account}.")
    return masked_account
