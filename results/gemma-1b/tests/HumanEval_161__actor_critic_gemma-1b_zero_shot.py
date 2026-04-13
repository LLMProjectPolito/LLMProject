
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

def test_single_character():
    assert solve("a") == "A"

def test_all_letters():
    assert solve("abc") == "ABC"

def test_all_lowercase():
    assert solve("abc") == "ABC"

def test_mixed_case():
    assert solve("aBc") == "aBc"

def test_numbers_and_letters():
    assert solve("1234") == "4321"

def test_numbers_only():
    assert solve("123") == "123"

def test_special_characters():
    assert solve("#a@C") == "#A@c"

def test_mixed_case_and_numbers():
    assert solve("a1b2c3") == "A1b2c3"

def test_longer_string():
    assert solve("abcdefg") == "gfedcba"

def test_string_with_only_numbers():
    assert solve("12345") == "54321"