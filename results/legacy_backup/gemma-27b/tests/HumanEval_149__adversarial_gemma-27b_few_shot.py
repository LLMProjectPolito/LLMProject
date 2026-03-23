import pytest

def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    even_length_strings.sort(key=lambda s: (len(s), s))
    return even_length_strings

# Pytest tests
def test_sorted_list_sum_basic():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert sorted_list_sum(["abc", "def", "ghi"]) == []
    assert sorted_list_sum(["abcd", "efgh", "ijkl"]) == ["abcd", "efgh", "ijkl"]
    assert sorted_list_sum(["abcde", "fghij", "klmno"]) == []

def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_duplicates():
    assert sorted_list_sum(["aa", "aa", "bb", "cc"]) == ["aa", "aa", "bb", "cc"]
    assert sorted_list_sum(["ab", "ab", "cd", "cd"]) == ["ab", "ab", "cd", "cd"]

def test_sorted_list_sum_same_length_alphabetical():
    assert sorted_list_sum(["ba", "aa", "ca"]) == ["aa", "ba", "ca"]
    assert sorted_list_sum(["cd", "ab", "ef"]) == ["ab", "cd", "ef"]

def test_sorted_list_sum_mixed_lengths():
    assert sorted_list_sum(["a", "aa", "aaa", "aaaa", "b", "bb", "bbb", "bbbb"]) == ["aa", "bb", "aaaa", "bbbb"]

def test_sorted_list_sum_long_strings():
    assert sorted_list_sum(["abcdef", "ghijkl", "mnopqr"]) == ["abcdef", "ghijkl", "mnopqr"]

def test_sorted_list_sum_all_odd():
    assert sorted_list_sum(["a", "abc", "def"]) == []

def test_sorted_list_sum_all_even():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]