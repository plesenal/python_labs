import pytest
from lib.text import *


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\\nМИр\\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\\r\\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected

@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("2025 год", ["2025", "год"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        (["a", "b", "a", "c", "b", "a"], [("a", 3), ("b", 2), ("c", 1)]),
        (["bb", "aa", "bb", "aa", "cc"], [("aa", 2), ("bb", 2), ("cc", 1)]),
    ],
)
def test_count_freq_and_top_n(source, expected):
    assert top_n(count_freq(source)) == expected


def test_top_n_tie_breaker():
    assert top_n(count_freq(["bb", "aa", "bb", "aa", "cc"]), 2) == [
        ("aa", 2),
        ("bb", 2),
    ]
def test_normalize_error():
    with pytest.raises(TypeError) as excinfo:
        normalize(123)
    assert excinfo.type == TypeError
@pytest.mark.parametrize(
    "source, expected",
    [
        ('ПрИвЕт\nМИр\t' , [('мир', 1), ('привет', 1)]),
        ('ёжик, Ёлка' , [('ежик', 1), ('елка', 1)]),
        ('Hello\r\nWorld' ,[('hello', 1), ('world', 1)]),
        ('  двойные   пробелы  ' , [('двойные', 1), ('пробелы', 1)])
    ]
)
def test_all_for_top_basic(source, expected):
    assert all_for_top_n(source) == expected
