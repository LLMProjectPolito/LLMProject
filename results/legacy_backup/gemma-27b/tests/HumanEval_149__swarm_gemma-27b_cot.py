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
    new_lst = [s for s in lst if len(s) % 2 == 0]
    new_lst.sort(key=lambda s: (len(s), s))
    return new_lst

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    assert sorted_list_sum(["a", "abc", ""]) == []

def test_mixed_lengths():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_duplicate_even_lengths():
    assert sorted_list_sum(["aa", "aa", "bb"]) == ["aa", "aa", "bb"]

def test_same_length_alphabetical():
    assert sorted_list_sum(["cb", "ab"]) == ["ab", "cb"]

def test_edge_case_empty_string():
    assert sorted_list_sum(["", "aa", "bb"]) == ["", "aa", "bb"]

def test_edge_case_long_strings():
    assert sorted_list_sum(["abcdef", "ghijkl", "mnopqr"]) == ["abcdef", "ghijkl", "mnopqr"]

def test_edge_case_long_strings_mixed():
    assert sorted_list_sum(["abcdef", "ghi", "mnopqr"]) == ["abcdef", "ghijkl"]

def test_edge_case_with_numbers_as_strings():
    assert sorted_list_sum(["12", "3", "456"]) == ["12"]

def test_edge_case_with_special_characters():
    assert sorted_list_sum(["!@#$", "abc", "def"]) == ["!@#$", "abc", "def"]

def test_edge_case_with_unicode_characters():
    assert sorted_list_sum(["你好", "世界"]) == []

def test_edge_case_with_mixed_unicode_and_ascii():
    assert sorted_list_sum(["你好", "ab", "cd"]) == ["ab", "cd"]

def test_edge_case_very_long_even_string():
    assert sorted_list_sum(["a" * 100]) == ["a" * 100]

def test_edge_case_very_long_odd_string():
    assert sorted_list_sum(["a" * 101]) == []

def test_edge_case_list_with_only_empty_strings():
    assert sorted_list_sum(["", "", ""]) == ["", "", ""]

def test_duplicates():
    assert sorted_list_sum(["ab", "ab", "cd", "a", "aaa"]) == ["ab", "ab", "cd"]

def test_same_length_alphabetical():
    assert sorted_list_sum(["bc", "ab", "cd"]) == ["ab", "bc", "cd"]

def test_long_strings():
    assert sorted_list_sum(["abcdef", "abc", "abcd"]) == ["abcd"]

def test_edge_case_single_even_length():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_edge_case_single_odd_length():
    assert sorted_list_sum(["a"]) == []

def test_edge_case_mixed_with_empty_string():
    assert sorted_list_sum(["", "aa", "a"]) == ["aa"]

@pytest.mark.parametrize("input_list, expected", [
    (["abc", "def", "ghi", "jkl"], ["abc", "def", "ghi", "jkl"]),
    (["abcd", "efgh", "ijkl", "mnop"], ["abcd", "efgh", "ijkl", "mnop"]),
    (["a", "bb", "ccc", "dddd"], ["bb", "dddd"]),
    (["abcde", "fghij", "klmno", "pqrst"], ["abcde", "fghij", "klmno", "pqrst"]),
    (["ab", "cd", "ef", "gh"], ["ab", "cd", "ef", "gh"]),
    (["a", "b", "c", "d"], []),
    (["aa", "bb", "cc", "dd"], ["aa", "bb", "cc", "dd"]),
    (["aaa", "bbb", "ccc", "ddd"], []),
    (["aaaa", "bbbb", "cccc", "dddd"], ["aaaa", "bbbb", "cccc", "dddd"]),
    (["abc", "def", "ghi", "jkl", "mno"], ["abc", "def", "ghi", "jkl", "mno"])
])
def test_various_cases(input_list, expected):
    assert sorted_list_sum(input_list) == expected