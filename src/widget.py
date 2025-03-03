from .masks import get_mask_card_number, get_mask_account

def mask_account_card(input_str: str) -> str:
    """Маскирует номер карты или счета в зависимости от типа.

    Параметры:
    input_str (str): Строка, содержащая тип и номер (например, "Visa Platinum 7000792289606361").

    Возвращает:
    str: Строка с замаскированным номером карты или счета.
    """
    if "Счет" in input_str:
        return input_str.split(' ')[0] + ' ' + get_mask_account(int(input_str.split(' ')[1]))
    else:
        return input_str.split(' ')[0] + ' ' + get_mask_card_number(int(input_str.split(' ')[1]))

def get_date(input_date: str) -> str:
    """Преобразует входную строку даты в форматированный вид.

    Параметры:
    input_date (str): Строка даты в формате "YYYY-MM-DDTHH:MM:SS.ffffff".

    Возвращает:
    str: Строка с датой в формате "ДД.ММ.ГГГГ".
    """
    from datetime import datetime
    dt = datetime.fromisoformat(input_date.split('T')[0])
    return dt.strftime("%d.%m.%Y")
