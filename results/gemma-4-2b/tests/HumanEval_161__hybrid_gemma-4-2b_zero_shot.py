
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

class TestSolve:

    def test_empty_string(self):
        assert solve("") == ""

    def test_all_numbers(self):
        assert solve("1234") == "4321"

    def test_all_symbols(self):
        assert solve("#@!%") == "#@!%"

    def test_mixed_case_and_numbers(self):
        assert solve("a1B2c") == "A1b2C"

    def test_mixed_case_and_symbols(self):
        assert solve("a#B@c") == "A#B@C"

    def test_only_lowercase(self):
        assert solve("hello") == "HELLO"

    def test_only_uppercase(self):
        assert solve("HELLO") == "hello"

    def test_mixed_lowercase_uppercase(self):
        assert solve("HeLlO") == "hElLo"

    def test_string_with_spaces(self):
        assert solve("a b c") == "A B C"

    def test_string_with_special_characters(self):
        assert solve("!@#$%^") == "!@#$%^"

    def test_long_string(self):
        assert solve("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") == "ZYXWVUTSRQPONMLKJIHGFEDCBA1234567890"

    def test_string_with_unicode(self):
      assert solve("你好世界") == "你好世界"

    def test_another_mixed_case(self):
      assert solve("tEsT") == "TeSt"

    def test_another_mixed_case_with_numbers(self):
      assert solve("a1b2C3d") == "A1b2C3d"

    def test_string_with_leading_and_trailing_spaces(self):
        assert solve("  a b  ") == "  A B  "

    def test_single_letter_lowercase(self):
        assert solve("a") == "A"

    def test_single_letter_uppercase(self):
        assert solve("A") == "a"

    def test_single_letter_mixed(self):
        assert solve("b") == "B"

    def test_multiple_letters(self):
        assert solve("ab") == "AB"

    def test_longer_string(self):
        assert solve("HeLlO wOrLd") == "hElLo WoRlD"

    def test_string_with_spaces(self):
        assert solve("a b C d") == "A b C d"

    def test_string_with_special_characters(self):
        assert solve("!@#$%^&*()") == "!@#$%^&*()"

    def test_string_with_mixed_characters(self):
        assert solve("a1B2c3!@#") == "A1b2C3!@#"

    def test_string_with_unicode_characters(self):
        assert solve("你好世界") == "你好世界"
        assert solve("你好世界你好") == "你好世界你好"

    def test_string_with_unicode_and_ascii(self):
        assert solve("你好a1B2c") == "你好A1b2C"

    def test_complex_string(self):
        assert solve("ThisIsAStringWithMixedCaseAndNumbers123") == "tHISiSABstRiNgwItHmIxEdCaSeAnDnuMbErS123"