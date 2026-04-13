
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
    has_letter = False
    result = ""
    for char in s:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            has_letter = True
            if 'a' <= char <= 'z':
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    if not has_letter:
        return s[::-1]
    return result

class TestSolve:
    def test_no_letters(self):
        assert solve("1234") == "4321"
        assert solve("!@#$%^") == "^%$#@!"
        assert solve("") == ""

    def test_all_letters_lower(self):
        assert solve("ab") == "AB"
        assert solve("abc") == "ABC"
        assert solve("hello") == "HELLO"

    def test_all_letters_upper(self):
        assert solve("AB") == "ab"
        assert solve("ABC") == "abc"
        assert solve("WORLD") == "world"

    def test_mixed_letters_and_symbols(self):
        assert solve("#a@C") == "#A@c"
        assert solve("1a2B3c") == "1A2b3C"
        assert solve("!a@B#c%") == "!A@b#C%"

    def test_empty_string(self):
        assert solve("") == ""

    def test_single_letter(self):
        assert solve("a") == "A"
        assert solve("A") == "a"

    def test_single_symbol(self):
        assert solve("!") == "!"

    def test_long_string(self):
        assert solve("ThisIsALongString") == "tHISiSALONGSTRING"
        assert solve("ThisIsALongString123") == "tHISiSALONGSTRING123"

    def test_string_with_spaces(self):
        assert solve("Hello World") == "hELLO wORLD"

    def test_string_with_numbers_and_letters(self):
        assert solve("a1b2c3d") == "A1B2C3D"
        assert solve("1a2b3c") == "1A2B3C"

    def test_string_with_special_characters(self):
        assert solve("!@#$%^&*()") == "!@#$%^&*()"
        assert solve("!a@B#c$") == "!A@b#C$"