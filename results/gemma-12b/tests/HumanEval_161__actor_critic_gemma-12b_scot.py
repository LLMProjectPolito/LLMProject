
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
    def test_string_with_only_numbers(self):
        assert solve("1234") == "4321"

    def test_only_lowercase(self):
        assert solve("ab") == "AB"

    def test_mixed_letters_and_symbols(self):
        assert solve("#a@C") == "#A@c"

    def test_empty_string(self):
        assert solve("") == ""

    def test_string_with_only_special_characters_reversed(self):
        assert solve("!@#$%") == "!@#$%"[::-1]

    def test_with_spaces(self):
        assert solve("hello world") == "hello world"

    def test_mixed_case_and_spaces(self):
        assert solve("Hello World") == "hEllo wORLd"

    def test_unicode_characters(self):
        assert solve("你好世界") == "界世好你"

    def test_numbers_and_unicode(self):
        assert solve("12你好世界") == "界世好你21"

    def test_single_character(self):
        assert solve("a") == "A"
        assert solve("1") == "1"

    def test_unicode_non_letter(self):
        assert solve("！") == "！"