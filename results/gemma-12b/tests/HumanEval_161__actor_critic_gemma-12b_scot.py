
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
    has_letter = False
    for char in s:
        if 'a' <= char <= 'z':
            result += char.upper()
            has_letter = True
        elif 'A' <= char <= 'Z':
            result += char.lower()
            has_letter = True
        else:
            result += char

    if not has_letter:
        return s[::-1]
    else:
        return result

class TestSolve:
    def test_only_numbers(self):
        assert solve("1234") == "4321"

    def test_only_lowercase(self):
        assert solve("ab") == "AB"

    def test_only_uppercase(self):
        assert solve("AB") == "ab"

    def test_mixed_letters_and_symbols(self):
        assert solve("#a@C") == "#A@c"

    def test_empty_string(self):
        assert solve("") == ""

    def test_only_special_characters(self):
        assert solve("!@#$%") == "%#$@!"

    # def test_with_spaces(self):  # Removed redundant test
    #     assert solve("hello world") == "hello world"

    def test_mixed_case_and_spaces(self):
        assert solve("Hello World") == "hELLO wORLD"

    def test_unicode_characters(self):
        assert solve("你好世界") == "界世好你"

    def test_numbers_and_unicode(self):
        assert solve("12你好世界") == "12界世好你"

    def test_single_character_letter(self):
        assert solve("a") == "A"

    def test_single_character_non_letter(self):
        assert solve("1") == "1"

    def test_single_uppercase_letter(self):
        assert solve("Z") == "z"

    def test_single_number(self):
        assert solve("5") == "5"

    def test_mixed_unicode(self):
        assert solve("你好A世界1") == "1界世A好你"

    def test_long_string(self):
        long_string = "a" * 1000 + "b" * 1000
        assert solve(long_string) == "B" * 1000 + "a" * 1000