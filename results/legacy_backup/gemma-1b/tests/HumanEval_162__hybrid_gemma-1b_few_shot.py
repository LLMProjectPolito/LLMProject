import hashlib
import pytest

# Suite 1: String to MD5
def string_to_md5(text):
    """
    Given a string 'text', return its MD5 hash equivalent string.
    If 'text' is an empty string, return None.
    """
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    return md5_hash

# Suite 2:  Palindrome Check
def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()  # Case-insensitive check
    return s == s[::-1]

# Suite 3:  Max Value
def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    max_val = arr[0]
    for x in arr:
        if x > max_val:
            max_val = x
    return max_val

# Test Suite - Combining all tests
def test_combined_suite():
    # String to MD5
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('') is None

    # Palindrome Check
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

    # Max Value
    assert get_max([1, 2, 3]) == 3
    assert get_max([]) == None
    assert get_max([5, 2, 8, 1, 9]) == 9
    assert get_max([-1, -2, -3]) == -1
    assert get_max([0, 0, 0]) == 0
    assert get_max([1]) == 1
    assert get_max([]) == None
    assert get_max([1, 1, 1]) == 1
    assert get_max([1, 2, 1]) == 2
    assert get_max([1, 2, 3, 4, 5]) == 5
    assert get_max([1, 2, 3, 4, 5, 6]) == 6
    assert get_max([1, 2, 3, 4, 5, 6, 7]) == 7
    assert get_max([1, 2, 3, 4, 5, 6, 7, 8]) == 8
    assert get_max([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
    assert get_max([]) == None
    assert get_max([10]) == 10
    assert get_max([-10]) == -10
    assert get_max([0]) == 0
    assert get_max([10, 0]) == 10
    assert get_max([10, 0, 10]) == 10
    assert get_max([10, 0, 10, 0]) == 10
    assert get_max([10, 0, 10, 0, 10]) == 10
    assert get_max([10, 0, 10, 0, 10, 10]) == 10
    assert get_max([10, 0, 10, 0, 10, 10, 10]) == 10
    assert get_max([10, 0, 10, 0, 10, 10, 10, 10]) == 10
    print("All tests passed!")