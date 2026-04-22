
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """

import pytest

# Note: The simplify function implementation is assumed to be present.

@pytest.mark.parametrize("x, n, expected", [
    # --- Standard True Cases (Integers) ---
    # (Renamed from "Whole Numbers" to "Integers" to reflect negative support)
    ("1/5", "5/1", True),
    ("2/3", "3/2", True),
    ("1/2", "4/1", True),
    ("10/1", "5/1", True),
    ("1/10", "100/1", True),
    ("3/4", "4/3", True),

    # --- Standard False Cases (Non-integers) ---
    ("1/6", "2/1", False),
    ("7/10", "10/2", False),
    ("1/3", "1/3", False),
    ("2/5", "3/5", False),
    ("5/2", "1/2", False),
    ("1/10", "1/10", False),
    ("1/2", "2/2", False),

    # --- Large Integers (Precision Check) ---
    # Uses integers > 2^53 (9,007,199,254,740,992) to ensure integer math is used
    ("10000000000000000/1", "1/10000000000000000", True),
    ("10000000000000001/1", "1/1", True),
    ("10000000000000001/1", "1/2", False),

    # --- Whitespace Handling ---
    (" 1/5 ", "5/1", True),
    ("1/2", " 2/1 ", True),
    (" 1/2 ", " 2/1 ", True),

    # --- Zero Edge Cases ---
    ("0/5", "5/1", True),    # 0 is an integer
    ("0/1", "0/1", True),    # 0 * 0 = 0
    ("-0/1", "5/1", True),   # Negative zero handling

    # --- Negative Number Edge Cases (Integers) ---
    ("-1/2", "2/1", True),   # Result: -1
    ("1/-2", "2/1", True),   # Result: -1
    ("-1/2", "-2/1", True),  # Result: 1
    ("-1/2", "1/2", False),  # Result: -0.25
    ("-1/3", "-3/1", True),  # Result: 1
])
def test_simplify_scenarios(x, n, expected):
    """Tests various valid scenarios including true/false, large ints, zero, negatives, and whitespace."""
    assert simplify(x, n) == expected


@pytest.mark.parametrize("x, n, expected_exception", [
    ("1/0", "1/1", ZeroDivisionError),  # Division by zero in first fraction
    ("1/1", "1/0", ZeroDivisionError),  # Division by zero in second fraction (Added)
    ("a/b", "1/1", ValueError),        # Non-numeric strings
    ("1/2", "x/y", ValueError),        # Non-numeric strings
    ("5", "1/1", ValueError),          # Missing denominator
    ("1/2/3", "1/1", ValueError),      # Malformed fraction
    ("", "1/1", ValueError),           # Empty string
])
def test_simplify_invalid_inputs(x, n, expected_exception):
    """Tests how the function handles invalid, malformed, or mathematically impossible inputs."""
    with pytest.raises(expected_exception):
        simplify(x, n)