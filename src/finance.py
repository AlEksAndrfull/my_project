import pandas as pd


def read_csv(file_path):
    """Читает CSV файл и возвращает данные в виде списка словарей.

    Args:
        file_path (str): Путь к CSV файлу.

    Returns:
        list: Список словарей, где каждый словарь представляет строку данных из файла.
              Если файл не найден или пуст, возвращает пустой список.
    """
    try:
        data = pd.read_csv(file_path)
        return data.to_dict(orient='records')
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except pd.errors.EmptyDataError:
        print(f"Файл {file_path} пуст.")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла {file_path}: {e}")
        return []


def read_excel(file_path):
    """Читает Excel файл и возвращает данные в виде списка словарей.

    Args:
        file_path (str): Путь к Excel файлу.

    Returns:
        list: Список словарей, где каждый словарь представляет строку данных из файла.
              Если файл не найден или пуст, возвращает пустой список.
    """
    try:
        data = pd.read_excel(file_path)
        return data.to_dict(orient='records')
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except pd.errors.EmptyDataError:
        print(f"Файл {file_path} пуст.")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла {file_path}: {e}")
        return []
