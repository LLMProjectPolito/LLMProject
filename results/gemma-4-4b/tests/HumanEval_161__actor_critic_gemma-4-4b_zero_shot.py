
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
    ("Ab", "ab"),
    ("HeLlO", "hElLo"),
    ("1a2B3c", "1A2b3C"),
    ("", ""),
    ("!@#$%^", "!@#$%^"),
    ("a", "A"),
    ("A", "a"),
    ("abcABC", "AbCabc"),
    ("aBcDeFg", "AbCdEfG"),
    ("123abc456DEF", "123ABC456def"),
    ("!@#$%", "!@#$%",),
    (" ", " "),
    ("  ", "  "),
    ("aA", "aA"),
    ("Aa", "aA"),
    ("1a2A", "1A2a"),
    ("!a@A#", "!A@a#"),
    ("a!A@a", "a!A@a"),
])
def test_solve(input_string, expected_output):
    assert solve(input_string) == expected_output