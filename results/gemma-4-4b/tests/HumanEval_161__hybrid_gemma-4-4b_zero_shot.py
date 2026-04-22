
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
        ("HeLlO", "hElLo"),
        ("aBcDeFg", "AbCdEfG"),
        ("1a2B3c", "1A2b3C"),
        ("", ""),
        ("!@#$%^", "!@#$%^"),
        ("  ", "  "),
        ("aA", "Aa"),
        ("bB", "bB"),
        ("cC", "cC"),
        ("zZ", "zZ"),
        ("Aa", "aA"),
        ("123abcABC", "123ABCabc"),
    ],
)
def test_solve_basic(input_string, expected_output):
    assert solve(input_string) == expected_output

@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("This is a test", "tHiS iS A TeSt"),
        ("Hello World!", "hElLo wOrLd!"),
        ("123 abc ABC", "123 AbC aBc"),
    ],
)
def test_solve_with_spaces(input_string, expected_output):
    assert solve(input_string) == expected_output

@pytest.mark.parametrize(
    "input_string",
    [
        ("a"),
        ("A"),
        ("1"),
        ("!"),
    ],
)
def test_solve_single_character(input_string):
    assert solve(input_string) == input_string

@pytest.mark.parametrize(
    "input_string",
    [
        ("abcdefghijklmnopqrstuvwxyz"),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
    ],
)
def test_solve_all_lowercase(input_string):
    assert solve(input_string) == input_string.upper()

@pytest.mark.parametrize(
    "input_string",
    [
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
    ],
)
def test_solve_all_uppercase(input_string):
    assert solve(input_string) == input_string.lower()

@pytest.mark.parametrize(
    "input_string",
    [
        ("aBcDeFgHiJkLmNoPqRsTuVwXyZ"),
    ],
)
def test_solve_mixed_case(input_string):
    assert solve(input_string) == "AbCdEfGhIjKlMnOpQrStUvWxYz"

@pytest.mark.parametrize(
    "input_string",
    [
        ("a1b2c3d4e"),
    ],
)
def test_solve_alphanumeric(input_string):
    assert solve(input_string) == "A1B2C3D4E"