import pytest

def list_sort(lst):
    """
    Sorts a list of strings by length of each word, and returns the sorted list.
    """
    return sorted(lst, key=lambda x: (len(x), x))

def test_list_sort_positive():
    assert list_sort(["aa", "a", "aaa"]) == ["aa"]

def test_list_sort_empty():
    assert list_sort([]) == []

def test_list_sort_single_element():
    assert list_sort(["hello"]) == ["hello"]

def test_list_sort_duplicate_elements():
    assert list_sort(["aa", "a", "aaa"]) == ["aa", "a", "aaa"]

def test_list_sort_mixed_lengths():
    assert list_sort(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_list_sort_same_length_words():
    assert list_sort(["aa", "a", "aaa"]) == ["aa", "a", "aaa"]

def test_is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_is_palindrome_single_char():
    assert is_palindrome('a') == True

def test_is_palindrome_single_char_reverse():
    assert is_palindrome('a') == False

def test_get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None