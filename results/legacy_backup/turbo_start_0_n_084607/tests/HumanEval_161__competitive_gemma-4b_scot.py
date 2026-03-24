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

def test_solve_no_letters():
    assert solve("1234") == "4321"

def test_solve_lowercase():
    assert solve("ab") == "AB"

def test_solve_mixed_case():
    assert solve("#a@C") == "#A@c"

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_all_uppercase():
    assert solve("ABC") == "abc"

def test_solve_all_lowercase():
    assert solve("abc") == "ABC"

def test_solve_with_numbers_and_symbols():
    assert solve("a1b2c#d@") == "A1B2C#D@"

def test_solve_with_spaces():
    assert solve("hello world") == "HELLO WORLD"

def test_solve_with_special_characters():
    assert solve("!@#$%^") == "^%$#@!"

def test_solve_long_string():
    assert solve("This is a long string with mixed case and numbers.") == "tHIS iS A LoNg sTRING wITH MiXeD cASE AnD nUMBErS."