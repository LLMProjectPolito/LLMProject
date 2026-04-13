
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
    for char in s:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            has_letter = True
            break

    if not has_letter:
        return s[::-1]
    else:
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
    def test_all_lowercase(self):
        assert solve("abc") == "ABC"

    def test_all_uppercase(self):
        assert solve("ABC") == "abc"

    def test_mixed_case(self):
        assert solve("aBc") == "AbC"

    def test_no_letters(self):
        assert solve("1234") == "4321"

    def test_symbols_only(self):
        assert solve("#@$") == "#@$"

    def test_letters_and_symbols(self):
        assert solve("#a@C") == "#A@c"

    def test_empty_string(self):
        assert solve("") == ""

    def test_single_lowercase_letter(self):
        assert solve("a") == "A"

    def test_single_uppercase_letter(self):
        assert solve("A") == "a"

    def test_single_non_letter(self):
        assert solve("1") == "1"

    def test_spaces(self):
        assert solve(" ") == " "

    def test_long_string(self):
        assert solve("abcdefghijklmnopqrstuvwxyz") == "ZYXWVUTSRQPONMLKJIHGFEDCBA"

    def test_unicode_characters(self):
        assert solve("你好世界") == "你好世界"

    def test_mixed_unicode_and_letters(self):
        assert solve("你好a世界") == "你好A世界"

    def test_integer_input(self):
        with pytest.raises(TypeError):
            solve(123)