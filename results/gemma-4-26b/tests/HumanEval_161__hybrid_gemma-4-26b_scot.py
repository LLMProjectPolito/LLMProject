
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

# Assuming the function is in solution.py
from solution import solve

@pytest.mark.parametrize("input_str, expected", [
    # --- BRANCH A: Letters are present (Case flipping, preservation of others) ---
    # Only letters
    ("abc", "ABC"),
    ("ABC", "abc"),
    ("aBcD", "AbCd"),
    
    # Mixed letters and non-letters
    ("#a@C", "#A@c"),
    ("1a2B3c", "1A2b3C"),
    ("Hello World!", "hELLO wORLD!"),
    ("   abc", "   ABC"),
    ("123aB", "123Ab"),
    ("a1b2", "A1B2"),
    ("   a   ", "   A   "),
    
    # --- BRANCH B: No letters present (Full string reversal) ---
    # Only numbers
    ("1234", "4321"),
    ("1 2 3", "3 2 1"),
    ("123 ", " 321"),
    
    # Only symbols/special characters
    ("!@#$", "$#@!"),
    ("!@#$%^&*()", ")(*&^%$#@!"),
    ("12!@34", "43@!21"),
    
    # Whitespace only
    ("   ", "   "),
    
    # --- EDGE CASES ---
    ("", ""),          # Empty string
    ("a", "A"),        # Single letter
    ("A", "a"),        # Single letter
    ("1", "1"),        # Single non-letter
    ("!", "!"),        # Single non-letter
    ("é", "É"),        # Single Unicode letter
])
def test_solve_parametrized(input_str, expected):
    """
    Comprehensive test covering the primary logic branches:
    - Branch A: Case swapping when letters exist.
    - Branch B: String reversal when no letters exist.
    - Edge cases: Empty strings and single characters.
    """
    assert solve(input_str) == expected

def test_solve_unicode_alphabetic():
    """
    Ensures that the implementation correctly identifies Unicode 
    alphabetic characters for case-swapping (Branch A).
    """
    assert solve("é") == "É"
    assert solve("12é") == "12É"
    assert solve("π") == "Π"
    assert solve("αβγ") == "ΑΒΓ"

def test_solve_complex_non_alpha_reversal():
    """
    Ensures that complex non-alphabetic characters (emojis, math symbols)
    trigger the reversal logic (Branch B) and are reversed correctly.
    """
    # Emojis and symbols should be reversed as they are not 'alpha'
    input_str = "🚀123!@#"
    expected = "#@!321🚀"
    assert solve(input_str) == expected
    
    # Math symbols
    assert solve("∑∫≈") == "≈∫∑"