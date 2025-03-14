import functools
import time
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования работы функции.
    :param filename: Имя файла для записи логов. Если не задано, логи будут выводиться в консоль.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Время начала выполнения функции
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                duration = time.time() - start_time
                log_message = f"{func.__name__} ok | Duration: {duration:.4f} seconds | Result: {result}"
                write_log(log_message, filename)
                return result
            except Exception as e:
                error_message = f"{func.__name__} error: {str(e)} | Inputs: {args}, {kwargs}"
                write_log(error_message, filename)
                raise
        return wrapper
    return decorator


def write_log(message: str, filename: Optional[str]) -> None:
    """
    Функция для записи сообщения в лог.
    :param message: Сообщение для записи.
    :param filename: Имя файла для записи логов. Если None, будет выведено в консоль.
    """
    if filename:
        with open(filename, 'a') as log_file:
            log_file.write(message + '\n')
    else:
        print(message)
