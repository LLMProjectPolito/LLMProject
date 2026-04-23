
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

def test_mixed_case():
    assert solve("ab") == "AB"
    assert solve("aB") == "Ab"
    assert solve("Ac") == "ac"

def test_all_uppercase():
    assert solve("ABC") == "abc"

def test_all_lowercase():
    assert solve("abc") == "ABC"

def test_special_characters():
    assert solve("#a@C") == "#A@c"
    assert solve("!@#$%^") == "^%$#@"

def test_mixed_characters():
    assert solve("a1B2c") == "A1b2C"

def test_complex_string():
    assert solve("HeLlO wOrLd") == "hElLo WoRlD"

def test_single_character_lowercase():
    assert solve("a") == "A"

def test_single_character_uppercase():
    assert solve("A") == "a"

def test_single_character_mixed():
    assert solve("x") == "X"

def test_long_string():
    assert solve("ThisIsALongStringWithMixedCaseAndSpecialCharacters!@#$%^&*()") == "tHISiSAlOnGStRiNgWiThMiXeDcASeAnDSpEcIaLChArAcTeRs!@#$%^&*()"