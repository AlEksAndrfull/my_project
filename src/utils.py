import json
import logging
import os

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logs/utils.log', mode='w')
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def read_json_file(file_path):
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
        logger.warning(f"Файл {file_path} не найден.")
        return []
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Успешно прочитан файл {file_path}.")
                return data
            logger.warning(f"Файл {file_path} не содержит корректный JSON-список.")
            return []
        except json.JSONDecodeError:
            logger.error(f"Ошибка декодирования JSON в файле {file_path}.")
            return []
