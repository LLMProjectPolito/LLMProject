import pytest

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    max_val = arr[0]
    for word in arr:
        if word > max_val:
            max_val = word
    return max_val

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_max_string():
    assert get_max(["string"]) == "string"

def test_max_mixed():
    assert get_max(["a", "b", "c", "a"]) == "a"

def test_max_duplicate_max():
    assert get_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_max_same_max():
    assert get_max(["aaaaaaa", "bb", "cc"]) == ""

def test_is_palindrome():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_is_palindrome_empty():
    assert is_palindrome('') == True