
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

def test_empty_string():
    assert solve("") == ""

def test_all_numbers():
    assert solve("1234") == "4321"

def test_all_lowercase():
    assert solve("abcdefg") == "ABCDEFG"

def test_all_uppercase():
    assert solve("ABCDEFG") == "abcdefg"

def test_mixed_case_letters():
    assert solve("AbCdEfG") == "aBcDeFg"

def test_mixed_letters_numbers():
    assert solve("a1b2c") == "A1B2C"

def test_mixed_letters_special_chars():
    assert solve("#a@C") == "#A@c"

def test_single_character_letter():
    assert solve("a") == "A"
    assert solve("A") == "a"

def test_single_character_number():
    assert solve("1") == "1"

def test_long_string():
    assert solve("ThisIsALongString") == "tHISiSalONgSTRING"

def test_string_with_spaces():
    assert solve("a b c") == "A B C"

# STEP 1: REASONING
# The function `solve(s)` transforms a string `s` by reversing the case of each letter. Non-letter characters remain unchanged.
# If the string contains no letters, it's simply reversed.
# We need to cover various scenarios:
# 1. String with only letters (mixed case).
# 2. String with only numbers.
# 3. String with only special characters.
# 4. String with mixed letters and numbers.
# 5. String with mixed letters, numbers and special characters.
# 6. Empty string.
# 7. String with a single character (letter, number, or special character).
# 8. String with a single letter (lowercase and uppercase).
# 9. String with a single non-letter character.
# 10. String with multiple consecutive same characters.

# STEP 2: PLAN
# Test function names:
# - test_empty_string
# - test_numbers_only
# - test_special_characters_only
# - test_mixed_letters_and_numbers
# - test_mixed_letters_numbers_and_special_characters
# - test_single_letter_lowercase
# - test_single_letter_uppercase
# - test_single_non_letter_character
# - test_mixed_case_letters
# - test_single_character_mixed

# STEP 3: CODE
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

@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("", ""),
        ("1234", "4321"),
        ("ab", "AB"),
        ("#a@C", "#A@c"),
        ("aA", "Aa"),
        ("bB", "bB"),
        ("a", "A"),
        ("b", "B"),
        ("1", "1"),
        ("abc", "ABC"),
        ("ABC", "abc"),
        ("aBcDeF", "AbCdEf"),
        ("aBcDeF", "AbCdEf"),
        ("aBcDeF", "AbCdEf"),
        ("aBcDeF", "AbCdEf"),
        ("aBcDeF", "AbCdEf"),
    ],
)
def test_solve(input_string, expected_output):
    assert solve(input_string) == expected_output

@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("12345", "54321"),
        ("!@#$%^", "!@#$%^"),
        ("aA1bB2cC", "aA1bB2cC"),
    ],
)
def test_solve_no_letters(input_string, expected_output):
    assert solve(input_string) == expected_output

@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("a", "A"),
        ("b", "B"),
        ("1", "1"),
        ("!", "!")
    ],
)
def test_single_character(input_string, expected_output):
    assert solve(input_string) == expected_output

@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("a", "A"),
        ("A", "a"),
        ("b", "B"),
        ("B", "b"),
        ("1", "1"),
        ("!", "!")
    ],
)
def test_single_character_mixed(input_string, expected_output):
    assert solve(input_string) == expected_output