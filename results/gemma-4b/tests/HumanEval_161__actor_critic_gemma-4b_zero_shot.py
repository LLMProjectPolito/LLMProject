
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
        assert solve("hello") == "HELLO"

    def test_uppercase_letters(self):
        assert solve("AB") == "ab"
        assert solve("WORLD") == "world"

    def test_mixed_case_letters(self):
        assert solve("#a@C") == "#A@c"
        assert solve("HeLlO") == "hElLo"

    def test_mixed_characters(self):
        assert solve("a1b2c3") == "A1B2C3"
        assert solve("!@#$") == "$#@!"

    def test_single_letter_lowercase(self):
        assert solve("a") == "A"

    def test_single_letter_uppercase(self):
        assert solve("A") == "a"

    def test_string_with_spaces(self):
        assert solve("hello world") == "HELLO WORLD"

    def test_string_with_numbers_and_symbols(self):
        assert solve("123!@#") == "123!@#"

    def test_long_string(self):
        assert solve("This is a long string with mixed case and characters.") == "tHIS iS A LoNG sTRING wITH MiXeD cASE AND cHARACTERS."

    def test_edge_case_all_uppercase(self):
        assert solve("UPPERCASE") == "uppercase"

    def test_edge_case_all_lowercase(self):
        assert solve("lowercase") == "Lowercase"