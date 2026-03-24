
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
    if not any('a' <= char <= 'z' for char in s):
        return s[::-1]
    return res

class TestSolve:
    def test_no_letters(self):
        assert solve("1234") == "4321"

    def test_lowercase_letters(self):
        assert solve("ab") == "AB"

    def test_mixed_case_letters(self):
        assert solve("#a@C") == "#A@c"

    def test_empty_string(self):
        assert solve("") == ""

    def test_all_uppercase(self):
        assert solve("ABC") == "abc"

    def test_all_lowercase(self):
        assert solve("abc") == "ABC"

    def test_mixed_with_numbers_and_symbols(self):
        assert solve("a1b2c#") == "A1B2C#"

    def test_long_string(self):
        assert solve("This is a test string.") == "tHIS IS A tEST sTRING."

    def test_string_with_spaces(self):
        assert solve("Hello World") == "hELLO wORLD"

    def test_special_characters(self):
        assert solve("!@#$%^") == "^%$#@!"

    def test_mixed_special_characters_and_letters(self):
        assert solve("a!b@c#") == "A!B@C#"