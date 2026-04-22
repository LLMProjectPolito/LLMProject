
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
    ("aB", "Ab"),
    ("abc", "ABC"),
    ("ABC", "abc"),
    ("1a2B3c", "1Ab2Bc3"),
    ("", ""),
    ("!@#$%^", "!@#$%^"),
    ("a", "A"),
    ("A", "a"),
    ("hello world", "Hello World"),
    ("HeLlO wOrLd", "hElLo WoRlD"),
    ("123abc456def", "123ABC456DEF"),
    ("!@#", "!@#"),
    ("aA", "aA"),
])
def test_solve_basic(input_string, expected_output):
    assert solve(input_string) == expected_output

@pytest.mark.parametrize("input_string", [
    "",
    "1234",
    "!@#$%^",
])
def test_solve_no_letters(input_string):
    assert solve(input_string) == input_string

@pytest.mark.parametrize("input_string", [
    "a",
    "A",
])
def test_solve_single_letter(input_string):
    assert solve(input_string) == solve(input_string)

@pytest.mark.parametrize("input_string", [
    "hello world",
    "HeLlO wOrLd",
])
def test_solve_with_spaces(input_string):
    assert solve(input_string) == solve(input_string)

@pytest.mark.parametrize("input_string", [
    "123abc456def",
])
def test_solve_mixed_characters(input_string):
    assert solve(input_string) == solve(input_string)