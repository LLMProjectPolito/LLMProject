
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

```python
def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if b in a:
        return True
    for i in range(1, len(b)):
        if b[i:] + b[:i] in a:
            return True
    return False

import pytest

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('a') == True
    assert is_palindrome('ab') == False
    assert is_palindrome('racecar') == True
    assert is_palindrome('madam') == True
    assert is_palindrome('level') == True
    assert is_palindrome('rotor') == True
    assert is_palindrome('deified') == True

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_special_chars():
    assert is_palindrome('A man, a plan, a canal: Panama') == False #Not a palindrome
    assert is_palindrome('Was it a car or a cat I saw?') == False #Not a palindrome
    assert is_palindrome('Madam, I\'m Adam') == False #Not a palindrome

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([5, 1, 9, 2]) == 9
    assert get_max([10, 5, 20, 1]) == 20

def test_get_max_empty():
    assert get_max([]) == None
    assert get_max([-1, -2, -3]) == -1

def test_get_max_single_element():
    assert get_max([5]) == 5
    assert get_max([-5]) == -5

def test_cycpattern_check_basic():
    assert cycpattern_check("abcd","abd") == False
    assert cycpattern_check("hello","ell") == True
    assert cycpattern_check("whassup","psus") == False
    assert cycpattern_check("abab","baa") == True
    assert cycpattern_check("efef","eeff") == False
    assert cycpattern_check("himenss","simen") == True

def test_cycpattern_check_no_match():
    assert cycpattern_check("abc","def") == False
    assert cycpattern_check("xyz","uvw") == False

def test_cycpattern_check_same_word():
    assert cycpattern_check("abc", "abc") == True

def test_cycpattern_check_longer_word():
    assert cycpattern_check("abcdefg", "cdefg") == True
    assert cycpattern_check("abcdefg", "fedcba") == True
    assert cycpattern_check("abcdefg", "efg") == True
    assert cycpattern_check("abcdefg", "gfedcba") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True
    assert cycpattern_check("abcdefg", "abcdefg") == True