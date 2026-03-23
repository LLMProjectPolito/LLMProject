import pytest

# The function `solve` is assumed to be imported from the module under test.
# e.g., from my_module import solve
# No import statement is added here per the problem instructions.

@pytest.mark.parametrize(
    "input_str, expected",
    [
        # No letters → whole string reversed
        ("1234", "4321"),
        ("!@#$", "$#@!"),
        ("   ", "   "),
        ("", ""),
        ("9876543210", "0123456789"),
        # Only letters → case toggled, order unchanged
        ("ab", "AB"),
        ("AB", "ab"),
        ("aBcDeF", "AbCdEf"),
        ("XYZ", "xyz"),
        ("hello", "HELLO"),
        ("HELLO", "hello"),
        # Mixed letters and non‑letters → only letters toggle case
        ("#a@C", "#A@c"),
        ("1a2B3c", "1A2b3C"),
        ("a b c", "A B C"),
        ("a\tB\nc", "A\tb\nC"),
        ("Python3.8!", "pYTHON3.8!"),
        # Unicode letters (isalpha() returns True) → case toggled
        ("éÉ", "Éé"),
        ("ñÑ", "Ññ"),
        ("ß", "SS"),  # German sharp s uppercases to "SS" in Python
        # Edge cases with single characters
        ("a", "A"),
        ("Z", "z"),
        ("5", "5"),
        (" ", " "),
        # Long mixed string
        (
            "The quick brown fox jumps over 13 lazy dogs! 12345",
            "tHE QUICK BROWN FOX JUMPS OVER 13 LAZY DOGS! 12345",
        ),
        # String with only whitespace and punctuation (no letters)
        (" \t\n!@#", "#@!\n\t "),
    ],
)
def test_solve_various_cases(input_str, expected):
    """Test solve() against a variety of typical, edge, and boundary inputs."""
    assert solve(input_str) == expected


def test_solve_no_side_effects():
    """Ensure that solve does not modify the original string (immutability check)."""
    original = "AbC123"
    result = solve(original)
    # Original string should remain unchanged
    assert original == "AbC123"
    # Result should be correctly transformed
    assert result == "aBc123"


def test_solve_large_input():
    """Stress test with a large input string to check performance and correctness."""
    # Create a 10,000‑character string: alternating letters and digits
    base = "a1B2c3D4e5F6g7H8i9J0"
    large_input = base * 1000  # 10,000 characters
    # Expected: letters toggled, digits unchanged, order unchanged
    expected = (
        "A1b2C3d4E5f6G7h8I9j0"
    ) * 1000
    assert solve(large_input) == expected