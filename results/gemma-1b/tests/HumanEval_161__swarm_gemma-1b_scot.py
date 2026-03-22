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
    s = s.lower()
    if not s.isalpha():
        s = s[::-1]
    return s

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
    if not s:
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

Final Suite:
    def test_solve_empty():
        assert solve("") == ""

    def test_solve_single_letter():
        assert solve("a") == "A"

    def test_solve_simple_string():
        assert solve("ab") == "AB"

    def test_solve_mixed_case():
        assert solve("aBc") == "aBc"

    def test_solve_no_letters():
        assert solve("#a@C") == "#A@c"

    def test_solve_all_letters():
        assert solve("abc") == "cba"

    def test_solve_numbers():
        assert solve("123") == "123"