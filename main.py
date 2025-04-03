import json
import pandas as pd
import csv
from src.operations import find_transactions_by_description


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")

    if choice == '1':
        with open("data/operations.json", 'r', encoding='utf-8') as file:
            transactions = json.load(file)
        file_type = 'JSON'

    elif choice == '2':
        with open("data/transactions.csv", 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            transactions = list(reader)
        file_type = 'CSV'

    elif choice == '3':
        transactions = pd.read_excel("data/transactions_excel.xlsx").to_dict(orient='records')
        file_type = 'XLSX'

    else:
        print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")
        return

    print(f"Для обработки выбран {file_type}-файл.")

    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. "
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
            "Пользователь: "
        )
        statuses = ['EXECUTED', 'CANCELED', 'PENDING']
        if status.upper() in statuses:
            break
        print(f"Статус операции \"{status}\" недоступен.")

    status = status.upper()
    filtered_transactions = [tx for tx in transactions if tx.get('state', '').upper() == status]

    print(f"Операции отфильтрованы по статусу \"{status}\"")

    sort_choice = input("Отсортировать операции по дате? Да/Нет\nПользователь: ")
    if sort_choice.lower() == 'да':
        order_choice = input("Сортировать по возрастанию или по убыванию?\nПользователь: ")
        if order_choice.lower() == "по убыванию":
            filtered_transactions.sort(key=lambda x: x['date'], reverse=True)
        else:
            filtered_transactions.sort(key=lambda x: x['date'])

    currency_choice = input("Выводить только рублевые транзакции? Да/Нет\nПользователь: ")
    if currency_choice.lower() == 'да':
        filtered_transactions = [tx for tx in filtered_transactions if tx.get('currency') == 'RUB']

    keyword_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: ")
    if keyword_choice.lower() == 'да':
        keyword = input("Введите слово для фильтрации: ")
        filtered_transactions = find_transactions_by_description(filtered_transactions, keyword)

    print("Распечатываю итоговый список транзакций...")
    if not filtered_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
    for tx in filtered_transactions:
        print(f"{tx['date']} {tx['description']}")
        print(f"Счет **{tx['account'][-4:]}")
        print(f"Сумма: {tx['amount']} {tx.get('currency', '')}\n")


if __name__ == "__main__":
    main()
