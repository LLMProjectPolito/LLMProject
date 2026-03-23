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


def test_cycpattern_basic_true():
    assert cycpattern_check("hello","ell") == True

def test_cycpattern_basic_false():
    assert cycpattern_check("abcd","abd") == False

def test_cycpattern_whassup():
    assert cycpattern_check("whassup","psus") == False

def test_cycpattern_abab():
    assert cycpattern_check("abab","baa") == True

def test_cycpattern_efef():
    assert cycpattern_check("efef","eeff") == False

def test_cycpattern_himenss():
    assert cycpattern_check("himenss","simen") == True

def test_cycpattern_empty_b():
    assert cycpattern_check("abcd", "") == True

def test_cycpattern_empty_a():
    assert cycpattern_check("", "abc") == False

def test_cycpattern_both_empty():
    assert cycpattern_check("", "") == True

def test_cycpattern_b_longer_than_a():
    assert cycpattern_check("abc", "abcdef") == False

def test_cycpattern_same_string():
    assert cycpattern_check("abc", "abc") == True

def test_cycpattern_repeated_pattern():
    assert cycpattern_check("ababab", "ab") == True

def test_cycpattern_long_strings():
    assert cycpattern_check("thisisalongstringwithsomepatterns", "string") == True

def test_cycpattern_long_strings_false():
    assert cycpattern_check("thisisalongstringwithsomepatterns", "patternz") == False

def test_cycpattern_case_sensitive():
    assert cycpattern_check("Hello", "ell") == False

def test_cycpattern_special_characters():
    assert cycpattern_check("a!b@c#", "b@c#") == True

def test_cycpattern_special_characters_false():
    assert cycpattern_check("a!b@c#", "b@c$") == False

def test_cycpattern_long_strings_true():
    assert cycpattern_check("thisisalongstring", "long") == True

def test_cycpattern_long_strings_false():
    assert cycpattern_check("thisisalongstring", "short") == False

def test_cycpattern_repeated_chars():
    assert cycpattern_check("aaaaa", "aa") == True

def test_cycpattern_repeated_chars_false():
    assert cycpattern_check("aaaaa", "aaaab") == False

def test_cycpattern_b_is_a():
    assert cycpattern_check("abc", "abc") == True

def test_cycpattern_b_is_a_rotated():
    assert cycpattern_check("abcabc", "bca") == True

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None