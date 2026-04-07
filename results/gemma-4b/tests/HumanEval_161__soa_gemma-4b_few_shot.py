
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

def test_empty_string():
    assert solve("") == ""

def test_no_letters():
    assert solve("1234") == "4321"

def test_lowercase_letters():
    assert solve("ab") == "AB"

def test_uppercase_letters():
    assert solve("AB") == "ab"

def test_mixed_case_letters():
    assert solve("#a@C") == "#A@c"

def test_mixed_case_with_numbers():
    assert solve("a1B2c3") == "A1b2C3"

def test_special_characters():
    assert solve("!@#$%^") == "^%$#@!"

def test_letters_and_special_characters():
    assert solve("a!b@c#") == "A!B@C#"

def test_long_string():
    assert solve("This is a long string with mixed case and numbers 123") == "tHIS iS A LoNg sTRING wITH mIXEd cASE AnD nUMBERs 321"

def test_all_uppercase():
    assert solve("ABC") == "abc"

def test_all_lowercase():
    assert solve("abc") == "ABC"

def test_single_letter_lowercase():
    assert solve("a") == "A"

def test_single_letter_uppercase():
    assert solve("A") == "a"

def test_single_special_character():
    assert solve("#") == "#"

def test_string_with_spaces():
    assert solve("hello world") == "HELLO WORLD"

def test_string_with_leading_and_trailing_spaces():
    assert solve("  hello world  ") == "  HELLO WORLD  "

def test_string_with_unicode_characters():
    assert solve("你好世界") == "你道世界"