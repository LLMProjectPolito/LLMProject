
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

@pytest.mark.parametrize("input_s, expected", [
    # Provided examples
    ("1234", "4321"),
    ("ab", "AB"),
    ("#a@C", "#A@c"),
    
    # Edge Case: Empty string
    ("", ""),
    
    # Edge Case: No letters (should reverse)
    ("123", "321"),
    ("!@#$", "$#@!"),
    ("   ", "   "),
    ("1 2 3", "3 2 1"),
    
    # Edge Case: Only letters (should swap case)
    ("abc", "ABC"),
    ("ABC", "abc"),
    ("aBcD", "AbCd"),
    ("z", "Z"),
    ("Z", "z"),
    
    # Edge Case: Mixed letters and non-letters (should swap case, NOT reverse)
    ("a1b2", "A1B2"),
    ("1a2b", "1A2B"),
    ("Hello World!", "hELLO wORLD!"),
    ("123a", "123A"),
    ("a123", "A123"),
    
    # Edge Case: Single character
    ("a", "A"),
    ("1", "1"),
    ("!", "!"),
    
    # Edge Case: Unicode/Special letters
    ("éÀ", "Éà"),
    ("123é", "123É"),
    ("é123", "É123"),
])
def test_solve(input_s, expected):
    """
    Tests the solve function against various scenarios:
    1. Strings with no letters should be reversed.
    2. Strings with at least one letter should have their case swapped.
    3. Non-letter characters in strings containing letters should remain unchanged.
    """
    assert solve(input_s) == expected

def test_solve_idempotency():
    """
    If a string contains letters, applying solve twice should return the original string.
    If a string contains no letters, applying solve twice should return the original string.
    """
    test_cases = ["Hello World!", "12345", "a1B2", "!!!", ""]
    for s in test_cases:
        assert solve(solve(s)) == s