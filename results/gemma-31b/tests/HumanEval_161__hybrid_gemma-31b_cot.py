
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

@pytest.mark.parametrize("input_str, expected", [
    # --- Standard Examples ---
    ("1234", "4321"),
    ("ab", "AB"),
    ("#a@C", "#A@c"),
    
    # --- Case 1: Strings containing letters (Swap Case Logic) ---
    # Only letters
    ("Hello", "hELLO"),
    ("WORLD", "world"),
    ("a", "A"),
    ("A", "a"),
    ("abcDEF", "ABCdef"),
    # Mixed alphanumeric/symbols
    ("a1B2", "A1b2"),
    ("!hello 123!", "!HELLO 123!"),
    ("Case Sensitive 123", "cASE sENSITIVE 123"),
    ("123-abc-456", "123-ABC-456"),
    ("Hello World", "hELLO wORLD"),
    ("Python3.10", "pYTHON3.10"),
    ("MixedCase123", "mIXEDcASE123"),
    # Letters with surrounding non-letters
    ("!!!abc!!!", "!!!ABC!!!"),
    ("   a   ", "   A   "),
    ("!!!a123!!!", "!!!A123!!!"),
    (" a B ", " A b "),
    # Unicode/Extended characters
    ("éÀ", "Éà"), 
    
    # --- Case 2: Strings containing NO letters (Reversal Logic) ---
    # Empty and whitespace
    ("", ""),
    (" ", " "),
    ("   ", "   "),
    # Digits and symbols
    ("123", "321"),
    ("!@#$", "$#@!"),
    ("1.2.3", "3.2.1"),
    ("123 456", "654 321"),
    ("!!!", "!!!"),
    ("123#$%", "%$#321"),
    # Single non-letter characters
    ("1", "1"),
    ("!", "!"),
])
def test_solve(input_str, expected):
    """
    Tests the solve function across all logic branches:
    1. If the string contains letters, it should swap the case of all letters.
    2. If the string contains no letters, it should reverse the entire string.
    3. Covers edge cases: empty strings, single characters, unicode, and whitespace.
    """
    assert solve(input_str) == expected

def test_solve_idempotency_no_letters():
    """
    For strings with no letters, reversing the string twice should return the original.
    """
    s = "123456789#$%"
    assert solve(solve(s)) == s

def test_solve_idempotency_with_letters():
    """
    For strings with letters, swapping the case twice should return the original.
    """
    s = "PyTest 123 aB12cD"
    assert solve(solve(s)) == s