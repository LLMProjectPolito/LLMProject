
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
    ("1a2b3c", "1A2B3C"),
    ("abcABC", "AbCabc"),
    ("", ""),
    ("!@#$%^", "!@#$%^"),
    ("a", "A"),
    ("A", "a"),
    ("123", "123"),
    ("!a@B", "!A@b"),
    ("aB", "Ab"),
    ("abcABC", "AbCabc"),
    ("AbCdEf", "aBcDeF"),
    ("madam", "MaDaM"),
    ("This is a long string with mixed case and numbers 1234567890.", "tHIS IS A LONG STRING WITH MIXED CASE AND NUMBERS 1234567890.")
])
def test_solve_basic(input_string, expected_output):
    assert solve(input_string) == expected_output

@pytest.mark.parametrize("input_string, expected_output", [
    ("1234", "4321"),
    ("ab", "AB"),
    ("#a@C", "#A@c"),
    ("Hello World", "hELLO wORLD"),
    ("1a2b3c", "1A2B3C"),
    ("abcABC", "AbCabc"),
    ("", ""),
    ("!@#$%^", "!@#$%^"),
    ("a", "A"),
    ("A", "a"),
    ("123", "123"),
    ("!a@B", "!A@b"),
    ("aB", "Ab"),
    ("abcABC", "AbCabc"),
    ("AbCdEf", "aBcDeF"),
    ("madam", "MaDaM"),
    ("This is a long string with mixed case and numbers 1234567890.", "tHIS IS A LONG STRING WITH MIXED CASE AND NUMBERS 1234567890.")
])
def test_solve_basic_2(input_string, expected_output):
    assert solve(input_string) == expected_output

@pytest.mark.parametrize("input_string, expected_output", [
    ("1234", "4321"),
    ("ab", "AB"),
    ("#a@C", "#A@c"),
    ("Hello World", "hELLO wORLD"),
    ("1a2b3c", "1A2B3C"),
    ("abcABC", "AbCabc"),
    ("", ""),
    ("!@#$%^", "!@#$%^"),
    ("a", "A"),
    ("A", "a"),
    ("123", "123"),
    ("!a@B", "!A@b"),
    ("aB", "Ab"),
    ("abcABC", "AbCabc"),
    ("AbCdEf", "aBcDeF"),
    ("madam", "MaDaM"),
    ("This is a long string with mixed case and numbers 1234567890.", "tHIS IS A LONG STRING WITH MIXED CASE AND NUMBERS 1234567890.")
])
def test_solve_basic_3(input_string, expected_output):
    assert solve(input_string) == expected_output