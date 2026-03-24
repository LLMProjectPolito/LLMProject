
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

    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += char.upper()
        elif 'A' <= char <= 'Z':
            result += char.lower()
        else:
            result += char
    return result

### Tests (Pytest):
import pytest

def test_solve_basic():
    assert solve("1234") == "4321"
    assert solve("ab") == "AB"
    assert solve("#a@C") == "#A@c"

def test_solve_empty_string():
    assert solve("") == ""

def test_solve_mixed_case_and_numbers():
    assert solve("a1B2c") == "A1b2C"

def test_solve_special_characters():
    assert solve("!@#$%^&*()") == "!@#$%^&*()"

def test_solve_unicode_characters():
    assert solve("héllö wørld") == "HÉLLÖ WØRLD"

def test_solve_all_uppercase():
    assert solve("ABC") == "abc"

def test_solve_all_lowercase():
    assert solve("abc") == "ABC"

def test_solve_string_with_only_spaces():
    assert solve("   ") == "   "

def test_solve_string_with_only_non_alphanumeric():
    assert solve("!@#") == "!@#"

def test_solve_no_letters_and_special_characters():
    assert solve("!@#") == "!@#"

def test_solve_long_string():
    long_string = "aBcDeFgHiJkLmNoPqRsTuVwXyZ1234567890!@#$%^&*()"
    expected_result = "AbCdEfGhIjKlMnOpQrStUvWxYz0987654321!@#$%^&*()"
    assert solve(long_string) == expected_result