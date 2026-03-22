# STEP 1: REASONING
# The function `solve(s)` aims to modify a string based on the presence of letters.
# If the string contains letters, it toggles the case of each letter while preserving non-letter characters.
# If the string contains no letters, it reverses the entire string.
# The test suite needs to cover these two main scenarios, as well as edge cases like empty strings, strings with only letters, strings with only non-letters, and mixed strings with various characters.

# STEP 2: PLAN
# Test functions:
# - test_no_letters: Tests a string with no letters, expecting a reversed string.
# - test_only_letters_lower: Tests a string with only lowercase letters, expecting an uppercase string.
# - test_only_letters_upper: Tests a string with only uppercase letters, expecting a lowercase string.
# - test_mixed_letters_and_symbols: Tests a string with letters and symbols, expecting case toggling for letters and symbols unchanged.
# - test_empty_string: Tests an empty string, expecting an empty string.
# - test_single_letter: Tests a string with a single letter, expecting the case toggled letter.
# - test_single_non_letter: Tests a string with a single non-letter, expecting the same non-letter.
# - test_numbers_and_letters: Tests a string with numbers and letters, expecting numbers unchanged and letters case toggled.

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
    def test_no_letters(self):
        assert solve("1234") == "4321"

    def test_only_letters_lower(self):
        assert solve("ab") == "AB"

    def test_only_letters_upper(self):
        assert solve("AB") == "ab"

    def test_mixed_letters_and_symbols(self):
        assert solve("#a@C") == "#A@c"

    def test_empty_string(self):
        assert solve("") == ""

    def test_single_letter(self):
        assert solve("a") == "A"
        assert solve("A") == "a"

    def test_single_non_letter(self):
        assert solve("1") == "1"
        assert solve("#") == "#"

    def test_numbers_and_letters(self):
        assert solve("a1B2c") == "A1b2C"

    def test_string_with_spaces(self):
        assert solve("hello world") == "HELLO WORLD"

    def test_string_with_special_characters(self):
        assert solve("!@#$%^") == "!@#$%^"

    def test_string_with_mixed_case_and_symbols(self):
        assert solve("HeLlO!@#") == "hElLo!@#"