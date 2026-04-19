
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
    # Case 1: String contains letters -> Swap case, NO reversal
    ("ab", "AB"),
    ("#a@C", "#A@c"),
    ("aBcD", "AbCd"),
    ("Hello World", "hELLO wORLD"),
    ("a1B2c3", "A1b2C3"),
    ("éÀ", "Éà"),  # Unicode support
    ("a", "A"),
    
    # Case 2: String contains NO letters -> Reverse the string
    ("1234", "4321"),
    ("123!@#", "#@!321"),
    ("12 34", "43 21"),
    ("!@#", "#@!"),
    (" \t\n", "\n\t "), # Whitespace-only (non-palindrome)
    ("", ""),           # Empty string
])
def test_solve_logic(input_s, expected):
    """Tests the core logic: swap case if letters exist, otherwise reverse."""
    assert solve(input_s) == expected

def test_solve_long_string():
    """Tests performance and boundary for large inputs."""
    # Long string with letters (swap case)
    long_letters = "a" * 10000
    assert solve(long_letters) == "A" * 10000
    
    # Long string without letters (reverse)
    long_no_letters = "12345" * 2000
    assert solve(long_no_letters) == long_no_letters[::-1]

@pytest.mark.parametrize("invalid_input", [
    None,
    123,
    ["a", "b"],
    {"s": "abc"},
])
def test_solve_invalid_types(invalid_input):
    """Tests that the function handles non-string inputs gracefully (raises TypeError)."""
    with pytest.raises(TypeError):
        solve(invalid_input)