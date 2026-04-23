
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

def solve(s: str) -> str:
    """
    If the string contains at least one letter, reverse the case of all letters 
    and keep non-letters as they are. If the string contains no letters, 
    reverse the entire string.
    """
    if any(c.isalpha() for c in s):
        return s.swapcase()
    return s[::-1]

@pytest.mark.parametrize("input_str, expected", [
    # --- Scenario 1: No Letters (Should Reverse Entire String) ---
    ("", ""),                  # Empty string
    (" ", ""),                 # Single space (Note: " " reversed is " ")
    ("   ", "   "),            # Multiple spaces
    ("1234", "4321"),          # Pure numbers
    ("!@#$", "$#@!"),          # Pure special characters
    ("12!@34", "43@!21"),      # Mixed numbers and special chars
    ("123 456", "654 321"),    # Numbers and spaces
    ("!@# 123", "321 #@!"),    # Mixed complex non-alpha
    ("12 34 !@", "@! 43 21"),  # Complex non-alpha

    # --- Scenario 2: Contains Letters (Should Swap Case) ---
    ("a", "A"),                # Single lowercase
    ("Z", "z"),                # Single uppercase
    ("ab", "AB"),              # All lowercase
    ("ABC", "abc"),            # All uppercase
    ("aBcD", "AbCd"),          # Mixed case
    ("Python", "pYTHON"),      # Standard word
    ("hello world", "HELLO WORLD"), # Sentence with space
    ("a b C", "A B c"),        # Mixed case with spaces
    ("! a ?", "? A !"),        # Letters with special characters
    ("#a@C", "#A@c"),          # Letters with special characters
    ("a1b2C3", "A1B2c3"),      # Letters with numbers
    ("a123", "A123"),          # Letter at start
    ("123a", "123A"),          # Letter at end
    ("Aa1! Bb2@ Cc3#", "aA1! bB2@ cC3#"), # Long mixed string

    # --- Scenario 3: Unicode / Non-ASCII ---
    ("αβγ", "ΑΒΓ"),             # Greek lowercase to uppercase
    ("α", "Α"),                # Single Greek letter
    ("é", "É"),                # Accented character
    ("123α", "123Α"),          # Unicode letter with numbers (triggers swap, not reverse)
    ("你好", "你好"),            # Chinese characters (isalpha is True, but swapcase is identity)
])
def test_solve_parametrized(input_str, expected):
    """Tests core logic across standard, mixed, and Unicode scenarios."""
    assert solve(input_str) == expected

def test_solve_boundary_logic():
    """Explicitly tests the threshold where one letter changes the entire behavior."""
    # Even a single letter prevents the reversal logic
    assert solve("1234a") == "1234A"
    assert solve("a1234") == "A1234"
    # Ensure non-letters are truly ignored for the 'contains letters' check
    assert solve("!!!a!!!") == "!!!A!!!"

def test_solve_large_inputs():
    """Tests performance and stability with large strings."""
    # Large string with letters (Swap Case)
    large_alpha = "a" * 5000 + "B" * 5000
    expected_alpha = "A" * 5000 + "b" * 5000
    assert solve(large_alpha) == expected_alpha

    # Large string without letters (Reverse)
    large_numeric = "1" * 5000 + "2" * 5000
    expected_numeric = "2" * 5000 + "1" * 5000
    assert solve(large_numeric) == expected_numeric