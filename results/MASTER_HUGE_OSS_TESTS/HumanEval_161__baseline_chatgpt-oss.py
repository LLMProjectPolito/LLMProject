import pytest

# The function under test is assumed to be defined in a module named `solution.py`.
# Adjust the import path if the implementation lives elsewhere.
from solution import solve


@pytest.mark.parametrize(
    "inp, expected",
    [
        # No letters → whole string reversed
        ("1234", "4321"),
        ("!@#$", "$#@!"),
        ("", ""),                     # empty string stays empty
        ("   ", "   "),               # spaces are not letters, just reversed (no effect)
        ("😀😁😂", "😂😁😀"),           # emojis are not letters → reversed

        # Only letters → case is flipped, order unchanged
        ("ab", "AB"),
        ("AB", "ab"),
        ("aBcDeF", "AbCdEf"),
        ("XYZ", "xyz"),
        ("xyz", "XYZ"),

        # Mixed letters and non‑letters → only letters change case, order unchanged
        ("#a@C", "#A@c"),
        ("1a2B3c", "1A2b3C"),
        ("Hello, World!", "hELLO, wORLD!"),
        ("PyThOn3.8", "pYtHoN3.8"),

        # Unicode letters (isalpha() returns True) → case flipped
        ("áéíóú", "ÁÉÍÓÚ"),
        ("ÁÉÍÓÚ", "áéíóú"),
        ("ß", "SS"),  # German sharp s → .upper() gives "SS"
        ("İ", "i̇"),   # Turkish dotted capital I → .lower() gives "i̇"

        # Long string to check performance / no overflow
        (
            "a" * 1000 + "1" * 1000,
            "A" * 1000 + "1" * 1000,
        ),
        (
            "1" * 500 + "b" * 500,
            "1" * 500 + "B" * 500,
        ),
    ],
)
def test_solve_various_cases(inp, expected):
    """Parametrized test covering all required behaviours."""
    assert solve(inp) == expected


def test_no_letter_string_is_reversed():
    """Explicit test that a string without any alphabetic characters is reversed."""
    s = "9-8-7-6-5"
    # No letters → reversed string
    assert solve(s) == s[::-1]


def test_string_with_only_spaces_and_symbols():
    """Spaces and symbols are not letters; they should be reversed only when no letters exist."""
    s = "   ***   "
    # Contains no letters → full reversal
    assert solve(s) == s[::-1]


def test_original_string_is_unchanged():
    """`solve` must not modify the original string (strings are immutable, but we check identity)."""
    original = "AbC123"
    result = solve(original)
    # The returned value should be a new string object (different identity)
    assert result is not original
    # The original variable must still hold the same value
    assert original == "AbC123"


def test_mixed_case_preserves_non_alpha_positions():
    """Non‑alphabetic characters must stay at the same indices."""
    s = "a1b2c3!@#"
    expected = "A1B2C3!@#"
    assert solve(s) == expected
    # Verify each non‑alpha character kept its original index
    for i, ch in enumerate(s):
        if not ch.isalpha():
            assert solve(s)[i] == ch