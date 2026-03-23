import pytest
import math

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
    res = ''
    for char in s:
        if 'a' <= char <= 'z':
            res += char.upper()
        elif 'A' <= char <= 'Z':
            res += char.lower()
        else:
            res += char
    if not any('a' <= char <= 'z' for char in s):
        return s[::-1]
    return res

def test_empty_string():
    assert solve("") == ""

def test_no_letters():
    assert solve("1234") == "4321"

def test_lowercase():
    assert solve("ab") == "AB"

def test_uppercase():
    assert solve("AB") == "ab"

def test_mixed_case():
    assert solve("#a@C") == "#A@c"

def test_mixed_case_with_numbers():
    assert solve("a1B2c") == "A1b2C"

def test_all_letters_lowercase():
    assert solve("hello") == "HELLO"

def test_all_letters_uppercase():
    assert solve("WORLD") == "world"

def test_special_characters():
    assert solve("!@#$%^") == "^%$#@!"

def test_mixed_characters():
    assert solve("a1B2c!@#") == "A1b2C!@#"