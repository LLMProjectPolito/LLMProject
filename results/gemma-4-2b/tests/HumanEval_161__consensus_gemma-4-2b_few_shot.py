
def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """

import pytest

def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """
    res = ""
    for char in s:
        if 'a' <= char <= 'z':
            res += char.upper()
        elif 'A' <= char <= 'Z':
            res += char.lower()
        else:
            res += char
    return res

def test_empty_string():
    assert solve("") == ""

def test_no_letters():
    assert solve("12345") == "54321"

def test_single_letter_lower():
    assert solve("a") == "A"

def test_single_letter_upper():
    assert solve("A") == "a"

def test_mixed_case():
    assert solve("ab") == "AB"

def test_mixed_case_with_non_letters():
    assert solve("#a@C") == "#A@c"

def test_all_upper():
    assert solve("ABC") == "abc"

def test_all_lower():
    assert solve("abc") == "ABC"

def test_complex_string():
    assert solve("HeLlO wOrLd") == "hElLo WoRlD"

def test_string_with_numbers_and_symbols():
    assert solve("1a2B3c4D") == "1A2b3C4d"

def test_string_with_special_characters():
    assert solve("!@#$%^&*()") == "!@#$%^&*()"

def test_long_string():
    assert solve("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()") == "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"

def test_string_with_spaces():
    assert solve("a b c") == "A B C"

def test_string_with_spaces_and_numbers():
    assert solve("a b 1 c 2") == "A B 1 C 2"

def test_string_with_mixed_characters():
    assert solve("a1B2c3D") == "A1b2C3d"

def test_string_with_unicode():
    assert solve("你好世界") == "你好世界"

def test_string_with_unicode_mixed_case():
    assert solve("你好世界你好") == "你好世界你好"

def test_string_with_unicode_mixed_case_case_swap():
    assert solve("你好世界你好") == "你好世界你好"