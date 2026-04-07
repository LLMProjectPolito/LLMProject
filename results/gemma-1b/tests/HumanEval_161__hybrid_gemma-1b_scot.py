
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
    """
    You are given a string s.
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

def test_empty_string():
    assert solve("") == ""

def test_single_character():
    assert solve("a") == "A"

def test_all_letters():
    assert solve("abc") == "ABC"

def test_mixed_case():
    assert solve("ab") == "AB"

def test_numbers():
    assert solve("123") == "321"

def test_symbols():
    assert solve("#a") == "#A"

def test_palindrome():
    assert solve("#a") == "#a"

def test_longer_string():
    assert solve("Hello World!") == "dlroW olleH"

def test_string_with_spaces():
    assert solve("hello world") == "dlrow olleh"

def test_case_insensitive():
    assert solve("Hello World!") == "dlroW olleH"

def test_special_characters():
    assert solve("#a") == "#A"

def test_complex_string():
    assert solve("aBcDeF") == "aBcDeF"