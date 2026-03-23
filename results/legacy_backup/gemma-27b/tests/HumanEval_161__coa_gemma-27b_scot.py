import pytest
import math


# Focus: Character Type/Case Sensitivity
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
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            has_letter = True
            if 'a' <= char <= 'z':
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    if not has_letter:
        result = result[::-1]
    return result

def test_case_sensitivity_lowercase():
    assert solve("ab") == "AB"

def test_case_sensitivity_uppercase():
    assert solve("AB") == "ab"

def test_case_sensitivity_mixed_case():
    assert solve("#a@C") == "#A@c"

def test_case_sensitivity_with_numbers():
    assert solve("a1B2c") == "A1b2C"

def test_case_sensitivity_empty_string():
    assert solve("") == ""

# Focus: Empty/All Non-Letter Strings
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
    result = ""
    for char in s:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            has_letter = True
            if 'a' <= char <= 'z':
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char
    if not has_letter:
        return result[::-1]
    return result

def test_empty_string():
    assert solve("") == ""

def test_all_non_letter_string():
    assert solve("1234") == "4321"

def test_all_non_letter_string_with_symbols():
    assert solve("#$%^") == "^%$#"

# Focus: Mixed Letter and Non-Letter Strings
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
    result = ""
    for char in s:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            has_letter = True
            if 'a' <= char <= 'z':
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char

    if not has_letter:
        result = result[::-1]

    return result

def test_mixed_letter_and_non_letter_strings():
    """Test cases with mixed letter and non-letter characters."""
    assert solve("#a@C") == "#A@c"
    assert solve("1a2B3c") == "1A2b3C"
    assert solve("HeLlO wOrLd!") == "hElLo WoRlD!"
    assert solve("a1b2c3d4e5f") == "A1B2C3D4E5F"
    assert solve("12345") == "54321"
    assert solve("!@#$%^") == "!@#$%^"
    assert solve("a") == "A"
    assert solve("A") == "a"
    assert solve("1") == "1"
    assert solve("") == ""
    assert solve("a1") == "A1"
    assert solve("1a") == "1A"