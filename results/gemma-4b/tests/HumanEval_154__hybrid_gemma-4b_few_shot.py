
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """

import pytest

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = ''.join(filter(str.isalnum, s)).lower()
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
    if not a or not b:
        return False

    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False


def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True
    assert is_palindrome('Madam') == True
    assert is_palindrome('level') == True
    assert is_palindrome('noon') == True
    assert is_palindrome('rotor') == True
    assert is_palindrome('stats') == True
    assert is_palindrome('refer') == True
    assert is_palindrome('deified') == True
    assert is_palindrome('reviver') == True
    assert is_palindrome('redder') == True
    assert is_palindrome('detartrated') == True
    assert is_palindrome('rotator') == True
    assert is_palindrome('hannah') == True
    assert is_palindrome('ababa') == True
    assert is_palindrome('12321') == True
    assert is_palindrome('12345') == False

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([3, 2, 1]) == 3
    assert get_max([1, 3, 2]) == 3
    assert get_max([-1, -2, -3]) == -1
    assert get_max([0, 0, 0]) == 0

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_single_element():
    assert get_max([5]) == 5

def test_get_max_mixed_positive_negative():
    assert get_max([-1, 2, -3, 4]) == 4
    assert get_max([1, -2, 3, -4]) == 3

def test_cycpattern_check_basic():
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("himenss", "simen") == True
    assert cycpattern_check("abcde", "cde") == True
    assert cycpattern_check("abcde", "edc") == True
    assert cycpattern_check("abcde", "abc") == True
    assert cycpattern_check("abcde", "de") == True
    assert cycpattern_check("abcde", "e") == True
    assert cycpattern_check("abcde", "a") == True
    assert cycpattern_check("abcde", "d") == True
    assert cycpattern_check("abcde", "c") == True
    assert cycpattern_check("abcde", "b") == True
    assert cycpattern_check("abcde", "ab") == False
    assert cycpattern_check("abcde", "bc") == False
    assert cycpattern_check("abcde", "cd") == False
    assert cycpattern_check("abcde", "de") == False
    assert cycpattern_check("abcde", "e") == False
    assert cycpattern_check("abcde", "abc") == False
    assert cycpattern_check("abcde", "abcd") == False
    assert cycpattern_check("abcde", "abcde") == True
    assert cycpattern_check("abcde", "edcba") == False
    assert cycpattern_check("abcde", "abcde") == True
    assert cycpattern_check("abcde", "edc") == True
    assert cycpattern_check("abcde", "abc") == True
    assert cycpattern_check("abcde", "de") == True
    assert cycpattern_check("abcde", "e") == True
    assert cycpattern_check("abcde", "a") == True
    assert cycpattern_check("abcde", "d") == True
    assert cycpattern_check("abcde", "c") == True
    assert cycpattern_check("abcde", "b") == True
    assert cycpattern_check("abcde", "ab") == False
    assert cycpattern_check("abcde", "bc") == False
    assert cycpattern_check("abcde", "cd") == False
    assert cycpattern_check("abcde", "de") == False
    assert cycpattern_check("abcde", "e") == False
    assert cycpattern_check("abcde", "abc") == False
    assert cycpattern_check("abcde", "abcd") == False
    assert cycpattern_check("abcde", "abcde") == True
    assert cycpattern_check("abcde", "edcba") == False
    assert cycpattern_check("abcde", "abcde") == True
    assert cycpattern_check("abcde", "edc") == True
    assert cycpattern_check("abcde", "abc") == True
    assert cycpattern_check("abcde", "de") == True
    assert cycpattern_check("abcde", "e") == True
    assert cycpattern_check("abcde", "a") == True
    assert cycpattern_check("abcde", "d") == True
    assert cycpattern_check("abcde", "c") == True
    assert cycpattern_check("abcde", "b") == True