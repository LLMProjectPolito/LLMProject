
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
        if 'a' <= char <= 'z':
            result += char.upper()
            has_letter = True
        elif 'A' <= char <= 'Z':
            result += char.lower()
            has_letter = True
        else:
            result += char
            has_letter = has_letter or (not ('a' <= char <= 'z' or 'A' <= char <= 'Z'))

    if not has_letter:
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

    def test_with_numbers_and_symbols(self):
        assert solve("1a2B3c") == "1A2b3C"
        assert solve("!a@B#c$") == "!A@b#C$"
        assert solve("123aB456c") == "123A456B"

    def test_empty_string(self):
        assert solve("") == ""

    def test_single_letter(self):
        assert solve("a") == "A"
        assert solve("A") == "a"

    def test_long_string(self):
        long_string = "ThisIsALongStringWithMixedCaseAndNumbers123!"
        expected_result = "tHISisAlongsTRINGwithmIXedCASEandnUMBERS123!"
        assert solve(long_string) == expected_result

    def test_string_with_unicode_characters(self):
        assert solve("你好世界") == "你好世界"
        assert solve("你好a世界") == "你好A世界"
        assert solve("a你好世界") == "A你好世界"