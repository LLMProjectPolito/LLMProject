
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

def test_lowercase_letters():
    assert solve("ab") == "AB"

def test_uppercase_letters():
    assert solve("AB") == "ab"

def test_mixed_case_letters():
    assert solve("aB") == "Ab"

def test_letters_and_symbols():
    assert solve("#a@C") == "#A@c"

def test_letters_and_numbers():
    assert solve("a1b2c") == "A1B2C"

def test_all_lowercase_with_symbols():
    assert solve("hello!") == "HELLO!"

def test_all_uppercase_with_symbols():
    assert solve("WORLD#") == "world#"

def test_long_string():
    assert solve("ThisIsALongString") == "tHISiSALONGsTRING"

def test_string_with_only_symbols():
    assert solve("!@#$%^") == "^%$#@!"

def test_string_with_spaces():
    assert solve("hello world") == "HELLO WORLD"

def test_string_with_mixed_characters():
    assert solve("a1b2c3A") == "A1B2C3a"