
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

@pytest.mark.parametrize("input_string, expected_output", [
    ("1234", "4321"),
    ("ab", "AB"),
    ("#a@C", "#A@c"),
    ("Hello World", "hELLO wORLD"),
    ("!@#$%^", "!@#$%^"),
    ("aBcDeF", "AbCdEf"),
    ("1a2b3c", "1A2B3C"),
    ("", ""),
    (" ", " "),
    ("a", "A"),
    ("A", "a"),
    ("123", "123"),
    ("abcABC", "AbCabc"),
    ("!@#$", "!@#$"),
    ("aB", "Ab"),
    ("abc", "ABC"),
    ("ABC", "abc"),
    ("1a2B3c", "1A2b3C"),
    ("AbCdEf", "aBcDeF"),
    ("ZYXwvutsrqponmlkjihgfedcba", "zyxWVUTSrqponmlkjihgfedcba"),
    ("abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
    ("This is a long string with mixed case and numbers 1234567890.", "tHIS IS A LONG STRING WITH MIXED CASE AND NUMBERS 1234567890.")
])
def test_solve(input_string, expected_output):
    assert solve(input_string) == expected_output

def test_empty_string():
    assert solve("") == ""

def test_only_numbers():
    assert solve("12345") == "54321"

def test_mixed_case_and_numbers():
    assert solve("a1B2c") == "A1b2C"

def test_special_characters():
    assert solve("!@#$%^") == "!@#$%^"