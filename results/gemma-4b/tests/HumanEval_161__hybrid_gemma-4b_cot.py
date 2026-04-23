
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
    def test_empty_string(self):
        assert solve("") == ""

    def test_no_letters(self):
        assert solve("1234") == "4321"

    def test_lowercase_letters(self):
        assert solve("ab") == "AB"

    def test_uppercase_letters(self):
        assert solve("AB") == "ab"

    def test_mixed_case_letters(self):
        assert solve("aB") == "Ab"

    def test_letters_and_symbols(self):
        assert solve("#a@C") == "#A@c"

    def test_letters_and_numbers(self):
        assert solve("a1B2") == "A1b2"

    def test_all_lowercase(self):
        assert solve("hello") == "HELLO"

    def test_all_uppercase(self):
        assert solve("WORLD") == "world"

    def test_complex_string(self):
        assert solve("HeLlO wOrLd 123!") == "hElLo WoRlD 123!"

    def test_single_letter_lowercase(self):
        assert solve("a") == "A"

    def test_single_letter_uppercase(self):
        assert solve("A") == "a"

    def test_single_symbol(self):
        assert solve("#") == "#"

    def test_multiple_symbols(self):
        assert solve("!@#$%") == "!@#$%"