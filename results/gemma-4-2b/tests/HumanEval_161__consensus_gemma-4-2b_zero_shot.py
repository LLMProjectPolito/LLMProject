
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
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += char.upper()
        elif 'A' <= char <= 'Z':
            result += char.lower()
        else:
            result += char
    return result

def test_empty_string():
    assert solve("") == ""

def test_no_letters():
    assert solve("12345") == "54321"

def test_lowercase_letters():
    assert solve("ab") == "AB"

def test_uppercase_letters():
    assert solve("aB") == "Ab"

def test_mixed_case_letters():
    assert solve("abCd") == "ABcd"

def test_mixed_case_with_non_letters():
    assert solve("#a@C") == "#A@c"

def test_all_uppercase():
    assert solve("ABC") == "abc"

def test_all_lowercase():
    assert solve("abc") == "ABC"

def test_single_letter_lower():
    assert solve("a") == "A"

def test_single_letter_upper():
    assert solve("A") == "a"

def test_complex_string():
    assert solve("HeLlO wOrLd") == "hElLo WoRlD"

def test_string_with_spaces():
    assert solve("hello world") == "HELLO WORLD"

def test_string_with_special_characters():
    assert solve("!@#$%^&*()") == "!@#$%^&*()"

def test_string_with_numbers_and_letters():
    assert solve("1a2B3c") == "1A2b3C"