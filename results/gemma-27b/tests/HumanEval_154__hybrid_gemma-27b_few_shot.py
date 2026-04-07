
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

def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    if not b:
        return True  # Empty string is always a substring

    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]
        if rotated_b in a:
            return True
    return False

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


def test_cycpattern_check_basic_true():
    assert cycpattern_check("hello", "ell") == True

def test_cycpattern_check_basic_false():
    assert cycpattern_check("abcd", "abd") == False

def test_cycpattern_check_whassup():
    assert cycpattern_check("whassup", "psus") == False

def test_cycpattern_check_abab():
    assert cycpattern_check("abab", "baa") == True

def test_cycpattern_check_efef():
    assert cycpattern_check("efef", "eeff") == False

def test_cycpattern_check_himenss():
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_empty_b():
    assert cycpattern_check("abc", "") == True

def test_cycpattern_check_empty_a():
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_both_empty():
    assert cycpattern_check("", "") == True

def test_cycpattern_check_b_longer_than_a():
    assert cycpattern_check("abc", "abcd") == False

def test_cycpattern_check_same_string():
    assert cycpattern_check("abc", "abc") == True

def test_cycpattern_check_rotation_at_start():
    assert cycpattern_check("abcdef", "cdefab") == True

def test_cycpattern_check_rotation_at_end():
    assert cycpattern_check("abcdef", "fabcde") == True

def test_cycpattern_check_complex_rotation():
    assert cycpattern_check("waterbottle", "erbottlewat") == True

def test_cycpattern_check_no_rotation_match():
    assert cycpattern_check("waterbottle", "bottlewaterx") == False

def test_cycpattern_check_long_strings():
    a = "a" * 1000 + "b"
    b = "b" + "a" * 999
    assert cycpattern_check(a, b) == True

def test_cycpattern_check_long_strings_no_match():
    a = "a" * 1000
    b = "b" * 1000
    assert cycpattern_check(a, b) == False

def test_cycpattern_check_rotation_true():
    assert cycpattern_check("abab", "baa") == True

def test_cycpattern_check_no_match():
    assert cycpattern_check("efef", "eeff") == False

def test_cycpattern_check_longer_string():
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_empty_a():
    assert cycpattern_check("", "abc") == False

def test_cycpattern_check_empty_b():
    assert cycpattern_check("abc", "") == False

def test_cycpattern_check_both_empty():
    assert cycpattern_check("", "") == False

def test_cycpattern_check_same_string():
    assert cycpattern_check("abc", "abc") == True

def test_cycpattern_check_b_longer_than_a():
    assert cycpattern_check("abc", "abcd") == False

def test_cycpattern_check_repeated_pattern():
    assert cycpattern_check("ababab", "aba") == True

def test_cycpattern_check_complex_rotation():
    assert cycpattern_check("waterbottle", "erbottlewat") == True

def test_cycpattern_check_case_sensitive():
    assert cycpattern_check("Hello", "ell") == False

def test_cycpattern_check_with_spaces():
    assert cycpattern_check("hello world", "world") == True

def test_cycpattern_check_with_special_chars():
    assert cycpattern_check("a!b@c#", "b@c#a") == True

def test_cycpattern_check_long_strings():
    a = "abcdefghijklmnopqrstuvwxyz" * 10
    b = "uvwxyzabcdefghijklm"
    assert cycpattern_check(a, b) == True

def test_cycpattern_check_long_strings_no_match():
    a = "abcdefghijklmnopqrstuvwxyz" * 10
    b = "zyxwvutsrqponmlkjihgfedcba"
    assert cycpattern_check(a, b) == False

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None