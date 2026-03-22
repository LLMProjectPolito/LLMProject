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
    if not any(c.isalpha() for c in s):
        return s[::-1]
    
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

    def test_no_letters(self):
        assert solve("1234") == "4321"

    def test_all_lowercase(self):
        assert solve("ab") == "AB"

    def test_all_uppercase(self):
        assert solve("AB") == "ab"

    def test_mixed_case(self):
        assert solve("aB") == "Ab"

    def test_single_letter(self):
        assert solve("a") == "A"

    def test_with_spaces(self):
        assert solve("hello world") == "HELLO WORLD"

    def test_with_special_characters(self):
        assert solve("#a@C") == "#A@c"

    def test_numbers_and_special_characters(self):
        assert solve("123#a@C") == "123#A@c"

    def test_leading_trailing_spaces(self):
        assert solve("  hello world  ") == "  WORLD hello  "

    def test_multiple_spaces(self):
        assert solve("hello   world") == "hello   WORLD"

    def test_mixed_string(self):
        assert solve("HeLlO 123!") == "hElLo 123!"

    def test_numbers_only(self):
        assert solve("12345") == "54321"

    def test_symbols_only(self):
        assert solve("!@#$%") == "%#$@!"