import os
import json
from typing import List, Dict, Any


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список словарей с данными о транзакциях.

    Параметры:
    ----------
    file_path : str
        Путь к JSON-файлу, который необходимо прочитать.

    Возвращает:
    ----------
    list
        Список словарей, содержащих данные о транзакциях, если файл существует и содержит корректный JSON.
        Если файл не существует или содержит некорректный JSON, возвращает пустой список.

    Исключения:
    -----------
    JSONDecodeError
        Возникает, если содержимое файла не является корректным JSON. В этом случае функция также вернет пустой список.
    """
    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
        except json.JSONDecodeError:
            return []
