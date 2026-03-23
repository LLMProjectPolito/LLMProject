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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


@pytest.mark.parametrize("input_list, expected_output", [
    (["aa", "a", "aaa"], ["aa"]),
    (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
    (["aa", "bb", "cc"], ["aa", "bb", "cc"]),
    (["a", "b", "c"], []),
    (["aa", "aa", "bb"], ["aa", "aa", "bb"]),
    (["abc", "ab", "abcd", "a"], ["ab"]),
    (["abc", "ab", "abcd", "a", "aba"], ["ab"]),
    (["", "a", "aa"], [""]),
    (["a", "aa", ""], ["", "aa"]),
    (["abc", "def", "ghi"], []),
    (["abc", "def", "ghi", "jkl"], ["abc", "def", "ghi", "jkl"]),
    (["abc", "def", "ghi", "jkl", "mno"], ["abc", "def", "ghi", "jkl"]),
    (["abc", "def", "ghi", "jkl", "mno", "pqr"], ["abc", "def", "ghi", "jkl"]),
    (["abc", "def", "ghi", "jkl", "mno", "pqr", "stu"], ["abc", "def", "ghi", "jkl"]),
    (["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx"], ["abc", "def", "ghi", "jkl"]),
    (["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz"], ["abc", "def", "ghi", "jkl"]),
    (["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz", "aaa"], ["abc", "def", "ghi", "jkl"]),
    (["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz", "aaa", "bbb"], ["abc", "def", "ghi", "jkl"]),
])
def test_sorted_list_sum(input_list, expected_output):
    assert sorted_list_sum(input_list) == expected_output

def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd():
    assert sorted_list_sum(["a", "b", "c"]) == []

def test_sorted_list_sum_same_length():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_sorted_list_sum_same_length_alphabetical():
    assert sorted_list_sum(["bb", "aa", "cc"]) == ["aa", "bb", "cc"]

def test_sorted_list_sum_mixed_lengths_and_alphabetical():
    assert sorted_list_sum(["abc", "ab", "abcd", "a", "aba"]) == ["ab"]


def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None