import pytest

def test_longest_empty_list():
    assert longest([]) is None

def test_longest_single_element_list():
    assert longest(['a']) == 'a'

def test_longest_multiple_elements_list():
    assert longest(['a', 'b', 'c']) == 'a'

def test_longest_list_with_multiple_max_length_strings():
    assert longest(['a', 'bb', 'bb', 'ccc']) == 'bb'

def test_longest_list_with_mixed_length_strings():
    assert longest(['a', 'bb', 'ccc', 'dddd']) == 'dddd'

def test_longest_list_with_all_strings_of_same_length():
    assert longest(['aa', 'bb', 'cc']) == 'aa'

def test_longest_list_with_empty_strings():
    assert longest(['', 'a', 'bb']) == ''

def test_longest_tie():
    assert longest(['a', 'b', 'aa']) == 'a'

def test_longest_single_element():
    assert longest(['single']) == 'single'

@pytest.mark.parametrize("input_list, expected_output", [
    ([], None),
    (['a', 'b', 'c'], 'a'),
    (['a', 'bb', 'ccc'], 'ccc'),
    (['abc', 'a', 'b', 'c'], 'abc'),
    (['a' * 10, 'b' * 5, 'c' * 15], 'c' * 15),
    (['apple', 'banana', 'cherry'], 'banana'),
])
def test_longest(input_list, expected_output):
    assert longest(input_list) == expected_output