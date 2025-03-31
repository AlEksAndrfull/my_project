from src.masks import get_mask_account, get_mask_card_number
from src.utils import read_json_file


def main():
    card_number = "1234567812345678"
    account_number = "123456789012"

    masked_card = get_mask_card_number(card_number)
    masked_account = get_mask_account(account_number)

    print(f"Замаскированный номер карты: {masked_card}")
    print(f"Замаскированный номер счета: {masked_account}")

    print(get_mask_card_number("1234"))  # Некорректный ввод
    print(get_mask_account("123"))        # Некорректный ввод


def main_transactions():
    file_path = input("Введите путь к JSON-файлу: ")

    transactions = read_json_file(file_path)

    if transactions:
        print("Данные о транзакциях:")
        for transaction in transactions:
            print(transaction)
    else:
        print("Не удалось прочитать данные из файла или файл пуст.")


if __name__ == "__main__":
    main()
    main_transactions()
