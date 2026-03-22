import pytest
import math


# Focus: Boundary Values
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
        return res[::-1]
    return res

def test_empty_string():
    assert solve("") == ""

def test_no_letters():
    assert solve("1234") == "4321"

def test_mixed_case_letters():
    assert solve("ab") == "AB"

def test_mixed_case_with_symbols():
    assert solve("#a@C") == "#A@c"

def test_all_uppercase():
    assert solve("ABC") == "abc"

def test_all_lowercase():
    assert solve("abc") == "ABC"

def test_mixed_with_numbers_and_symbols():
    assert solve("a1!b2@c") == "A1!B2@C"

# Focus: Type Scenarios
import pytest

def test_no_letters():
    assert solve("1234") == "4321"

def test_lowercase_letters():
    assert solve("ab") == "AB"

def test_mixed_case_letters():
    assert solve("#a@C") == "#A@c"

# Focus: Logic Branches
import pytest

def test_no_letters():
    assert solve("1234") == "4321"

def test_lowercase_to_uppercase():
    assert solve("ab") == "AB"

def test_mixed_case_reversal():
    assert solve("#a@C") == "#A@c"