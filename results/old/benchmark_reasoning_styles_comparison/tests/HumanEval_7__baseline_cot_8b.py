import pytest

@pytest.mark.parametrize("strings, substring, expected", [
    ([], 'a', []),
    (['abc', 'bacd', 'cde', 'array'], 'a', ['abc', 'bacd', 'array']),
    (['hello', 'world', 'python'], 'hello', ['hello']),
    (['test', 'example', 'sample'], 'ex', ['example']),
    (['apple', 'banana', 'cherry'], 'an', ['banana']),
    (['dog', 'cat', 'bird'], '', ['dog', 'cat', 'bird']),
    (['car', 'bike', 'train'], 'car', ['car']),
    (['house', 'tree', 'flower'], 'house', ['house']),
])
def test_filter_by_substring(strings, substring, expected):
    assert filter_by_substring(strings, substring) == expected

def test_filter_by_substring_empty_substring():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], '') == ['abc', 'bacd', 'cde', 'array']

def test_filter_by_substring_none_input():
    with pytest.raises(TypeError):
        filter_by_substring(None, 'a')

def test_filter_by_substring_none_substring():
    with pytest.raises(TypeError):
        filter_by_substring(['abc', 'bacd', 'cde', 'array'], None)

def test_filter_by_substring_non_string_substring():
    with pytest.raises(TypeError):
        filter_by_substring(['abc', 'bacd', 'cde', 'array'], 123)

def test_filter_by_substring_non_list_input():
    with pytest.raises(TypeError):
        filter_by_substring('abc', 'a')