
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

    def test_all_lowercase_with_symbols(self):
        assert solve("hello#world") == "HELLO#WORLD"

    def test_all_uppercase_with_symbols(self):
        assert solve("WORLD#HELLO") == "world#hello"

    def test_long_string(self):
        assert solve("This is a long string with letters and numbers!") == "tHIS iS A LONG STRING WITH LETTERS AND NUMBERS!"

    def test_string_with_only_symbols(self):
        assert solve("!@#$%^") == "!@#$%^"

    def test_string_with_spaces(self):
        assert solve("  a b  ") == "  A B  "

    def test_mixed_with_unicode(self):
        assert solve("你好世界") == "你好世界"

    def test_mixed_with_special_chars(self):
        assert solve("!@#$aB%^") == "!@#$Ab%^"