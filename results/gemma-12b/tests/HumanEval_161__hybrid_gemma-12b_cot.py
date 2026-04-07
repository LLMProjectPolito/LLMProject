
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
    letter_present = False
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += char.upper()
            letter_present = True
        elif 'A' <= char <= 'Z':
            result += char.lower()
            letter_present = True
        else:
            result += char
            #letter_present = letter_present or False # This line was incorrect in the second suite

    if not letter_present:
        return s[::-1]
    else:
        return result

class TestSolve:
    def test_no_letters(self):
        assert solve("1234") == "4321"
        assert solve("!@#$%^") == "!@#$%^"
        assert solve("") == ""

    def test_all_lowercase(self):
        assert solve("ab") == "AB"
        assert solve("abc") == "ABC"
        assert solve("hello") == "HELLO"

    def test_all_uppercase(self):
        assert solve("AB") == "ab"
        assert solve("ABC") == "abc"
        assert solve("WORLD") == "world"

    def test_mixed_case(self):
        assert solve("#a@C") == "#A@c"
        assert solve("aBcDeF") == "AbCdEf"
        assert solve("HeLlO") == "hElLo"

    def test_special_characters(self):
        assert solve("!a@b#c$") == "!A@B#C$"
        assert solve("1a2b3c") == "1A2B3C"
        assert solve("a1b2c3") == "A1B2C3"
        assert solve("!@#$") == "!@#$"
        assert solve("123abcABC!@#$") == "123ABCabc!@#$"
        assert solve("a1b2c3d4e5") == "A1B2C3D4E5"
        assert solve("!@#a$b%c") == "!@#A$B%C"

    def test_string_with_spaces(self):
        assert solve("a b c") == "A B C"
        assert solve(" A b C ") == " A B C "
        assert solve("hello world") == "HELLO WORLD"
        assert solve("  a b  ") == "  A B  "

    def test_unicode_characters(self):
        assert solve("你好世界") == "你好世界"
        assert solve("你好a世界") == "你好A世界"
        assert solve("a你好世界") == "A你好世界"

    def test_long_string(self):
        long_string = "This is a long string with mixed case letters and numbers 1234567890"
        expected_result = "tHIS IS A LONG STRING WITH MIXED CASE LETTERS AND NUMBERS 1234567890"
        assert solve(long_string) == expected_result
        long_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
        expected_result = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0987654321!@#$%^&*()"
        assert solve(long_string) == expected_result

    def test_string_with_numbers_and_special_chars(self):
        assert solve("1a2b3c") == "1A2B3C"
        assert solve("!@#a$b%c") == "!@#A$B%C"