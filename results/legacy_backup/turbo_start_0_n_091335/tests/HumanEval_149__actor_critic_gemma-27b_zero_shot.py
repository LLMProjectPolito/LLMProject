import pytest

def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order.
    The list should be sorted by length (ascending), and then alphabetically
    if strings have the same length.
    The function handles strings of varying lengths and may contain duplicates.
    For example:
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    """
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    even_length_strings.sort(key=lambda s: (len(s), s))
    return even_length_strings

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    assert sorted_list_sum(["a", "abc", "def"]) == []

def test_mixed_lengths():
    assert sorted_list_sum(["aa", "a", "aaa", "bb"]) == ["aa", "bb"]

def test_mixed_lengths_with_duplicates():
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "aa"]) == ["aa", "aa", "bb"]

def test_same_length_alphabetical():
    assert sorted_list_sum(["cb", "ab", "db"]) == ["ab", "cb", "db"]

def test_single_even_length():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_single_odd_length():
    assert sorted_list_sum(["a"]) == []

def test_longer_strings():
    assert sorted_list_sum(["abcdef", "abc", "defgh"]) == ["abcdef", "defgh"]

def test_empty_string():
    assert sorted_list_sum(["", "a", "aa"]) == ["aa"]

def test_multiple_empty_strings():
    assert sorted_list_sum(["", "", "aa", "bb"]) == ["aa", "bb"]

def test_large_input():
    large_list = ["a" * i for i in range(1, 201)]
    expected = ["a" * i for i in range(2, 201, 2)]
    assert sorted_list_sum(large_list) == expected

def test_non_string_element():
    with pytest.raises(TypeError):
        sorted_list_sum(["aa", 123, "bb"])