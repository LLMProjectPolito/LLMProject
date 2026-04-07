
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
    res = ""
    for char in s:
        if 'a' <= char <= 'z':
            res += char.upper()
        elif 'A' <= char <= 'Z':
            res += char.lower()
        else:
            res += char
    return res

def test_solve_empty():
    assert solve("") == ""

def test_solve_all_letters():
    assert solve("abcdefg") == "gfedcba"

def test_solve_no_letters():
    assert solve("#a@C") == "#C@a"

def test_solve_mixed_case():
    assert solve("aB") == "Ab"

def test_solve_numbers():
    assert solve("1234") == "4321"

def test_solve_symbols():
    assert solve("!@#") == "!@#"

def test_solve_unicode():
    assert solve("你好世界") == "界世好你"

def test_solve_simple_case():
    assert solve("abc") == "ABC"

def test_solve_complex_case():
    assert solve("aBc") == "aBc"