import pytest
from math import log

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
    if not s:
        return s[::-1]
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += char.upper()
        elif 'A' <= char <= 'Z':
            result += char.lower()
        else:
            result += char
    return result

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
    if not s:
        return s[::-1]
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += char.upper()
        elif 'A' <= char <= 'Z':
            result += char.lower()
        else:
            result += char
    return result

def test_solve_valid_string():
    assert solve("1234") == "4321"
    assert solve("ab") == "AB"
    assert solve("#a@C") == "#A@c"

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_all_lowercase():
    assert solve("abc") == "cba"

def test_solve_all_uppercase():
    assert solve("ABC") == "CBA"

def test_solve_mixed_case():
    assert solve("aBc") == "aBc"

def test_solve_numbers():
    assert solve("123") == "321"
    assert solve("123a") == "a123"
    assert solve("123.4") == "432.1"