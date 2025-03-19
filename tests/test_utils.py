import pytest
from src.utils import read_json_file


@pytest.mark.parametrize("file_path, expected", [
    ('data/operations.json', 'not_empty'),  # Предполагается, что файл не пустой
    ('data/non_existent.json', []),         # Файл не существует
    ('data/empty.json', []),                 # Пустой файл
])
def test_read_json_file(file_path, expected):
    if expected == 'not_empty':
        assert read_json_file(file_path) != []
    else:
        assert read_json_file(file_path) == expected
