
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
        assert solve("#a@C") == "#A@c"

    def test_mixed_case_with_numbers(self):
        assert solve("a1B2c") == "A1b2C"

    def test_special_characters(self):
        assert solve("!@#$%^") == "^%$#@!"

    def test_mixed_characters(self):
        assert solve("a1B2c!@#") == "A1b2C!@#"

    def test_long_string(self):
        assert solve("This is a long string with mixed case and numbers.") == "tHIS Is A LONG STRING wITH MIXED CASE AND NUMBERS."

    def test_all_lowercase_with_numbers(self):
        assert solve("hello123world") == "HELLO123WORLD"

    def test_all_uppercase_with_numbers(self):
        assert solve("HELLO123WORLD") == "hello123world"

    def test_string_with_spaces(self):
        assert solve("  a b c  ") == "  A B C  "

    def test_string_with_unicode_characters(self):
        assert solve("你好世界") == "界世好你"

    def test_string_with_mixed_unicode_and_ascii(self):
        assert solve("a你好b") == "A你好b"