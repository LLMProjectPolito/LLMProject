
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

@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("1234", "4321"),
        ("ab", "AB"),
        ("#a@C", "#A@c"),
        ("Hello World", "hELLO wORLD"),
        ("aBcDeFg", "AbCdEfG"),
        ("1a2B3c", "1A2b3C"),
        ("", ""),
        ("!@#$%^", "!@#$%^"),
        ("This is a test", "tHIS IS A TEST"),
        ("ALL CAPS", "all caps"),
        ("all lower", "ALL LOWER"),
        ("MixedCase123", "mIXEDcASE123"),
        ("aA", "Aa"),
    ],
)
def test_solve_basic(input_string, expected_output):
    assert solve(input_string) == expected_output

@pytest.mark.parametrize(
    "input_string",
    [
        "",
        "1234567890",
        "!@#$%^&*()_+=-`~[]\{}|;':\",./<>?",
    ],
)
def test_solve_no_letters(input_string):
    assert solve(input_string) == input_string

@pytest.mark.parametrize(
    "input_string",
    [
        "a",
        "A",
    ],
)
def test_solve_single_letter(input_string):
    assert solve(input_string) == solve(input_string)

@pytest.mark.parametrize(
    "input_string",
    [
        "aBcDeFgHiJkLmNoPqRsTuVwXyZ",
        "zYXwvutsrqponmlkjihgfedcba",
    ],
)
def test_solve_long_string(input_string):
    assert solve(input_string) == solve(input_string)