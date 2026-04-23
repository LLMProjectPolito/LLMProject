
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
    if not any('a' <= c <= 'z' for c in s):
        return s[::-1]
    return res

def test_empty_string():
    assert solve("") == ""

def test_no_letters():
    assert solve("1234") == "4321"

def test_lowercase_letters():
    assert solve("ab") == "AB"
    assert solve("hello") == "HELLO"

def test_uppercase_letters():
    assert solve("ABC") == "abc"
    assert solve("WORLD") == "world"

def test_mixed_case_letters():
    assert solve("aBc") == "AbC"
    assert solve("HeLlO") == "hElLo"

def test_letters_and_symbols():
    assert solve("#a@C") == "#A@c"
    assert solve("!@#$") == "$#@!"
    assert solve("a1b2c") == "A1B2C"

def test_numbers_and_letters():
    assert solve("1a2b3c") == "1A2B3C"
    assert solve("123abc") == "123ABC"

def test_special_characters():
    assert solve("!@#$%^") == "^%$#@!"
    assert solve("!@#$") == "$#@!"

def test_long_string():
    assert solve("This is a long string with mixed case and symbols.") == "tHIS iS A LoNg sTRING wITH mIXEd cASE AnD sYMBOLS."

def test_all_uppercase():
    assert solve("ALLCAPS") == "allcaps"

def test_all_lowercase():
    assert solve("alllowercase") == "ALLLOWERCASE"

def test_single_letter_lowercase():
    assert solve("a") == "A"

def test_single_letter_uppercase():
    assert solve("A") == "a"

def test_single_char_non_letter():
    assert solve("1") == "1"

def test_complex_string():
    assert solve("HeLlO wOrLd! 123") == "hElLo WoRlD! 123"

def test_string_with_spaces():
    assert solve("  hello world  ") == "  HELLO WORLD  "