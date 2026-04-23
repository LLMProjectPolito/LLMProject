
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

import pytest
from solution import generate_integers

@pytest.mark.parametrize("a, b, expected", [
    # --- Provided Examples & Standard Cases ---
    (2, 8, [2, 4, 6, 8]),    # Standard ascending
    (8, 2, [2, 4, 6, 8]),    # Standard descending
    (10, 14, []),            # Range entirely above single digits

    # --- Single Point Ranges (a == b) ---
    (0, 0, [0]),             # Single even digit (zero)
    (2, 2, [2]),             # Single even digit
    (4, 4, [4]),             # Single even digit
    (6, 6, [6]),             # Single even digit
    (8, 8, [8]),             # Single even digit
    (1, 1, []),              # Single odd number
    (3, 3, []),              # Single odd number
    (7, 7, []),              # Single odd number
    (9, 9, []),              # Single odd number

    # --- Small Ranges (Within single digits) ---
    (1, 5, [2, 4]),          # Subset of even digits
    (3, 7, [4, 6]),          # Subset of even digits
    (5, 9, [6, 8]),          # Subset of even digits
    (2, 3, [2]),             # Range containing one even digit
    (7, 8, [8]),             # Range containing one even digit
    (1, 2, [2]),             # Range containing one even digit
    (8, 9, [8]),             # Range containing one even digit
    (1, 3, [2]),             # Small range (ascending)
    (3, 1, [2]),             # Small range (descending)
    (7, 9, [8]),             # Small range (ascending)
    (9, 7, [8]),             # Small range (descending)
    (2, 4, [2, 4]),          # Continuous even digits
    (4, 2, [2, 4]),          # Continuous even digits (descending)
    (1, 9, [2, 4, 6, 8]),    # Full range of even digits
    (9, 1, [2, 4, 6, 8]),    # Full range of even digits (descending)

    # --- Boundary & Zero Crossing ---
    (0, 5, [0, 2, 4]),       # Range including zero
    (5, 11, [6, 8]),         # Range crossing the 10 boundary (ascending)
    (11, 5, [6, 8]),         # Range crossing the 10 boundary (descending)
    (8, 12, [8]),            # Range starting on a digit and going above
    (12, 8, [8]),            # Range starting above and ending on a digit

    # --- Large Ranges & Non-Digit Ranges ---
    (11, 20, []),            # No single digits in range
    (100, 200, []),          # Large numbers
    (1000, 5000, []),        # Large range (no digits)
    (2, 5000, [2, 4, 6, 8]), # Massive range including single digits
    (1000, 5, [2]),          # Massive range (descending)
    (5, 1000, [2, 4, 6, 8]), # Massive range (ascending)
])
def test_generate_integers_logic(a, b, expected):
    """
    Tests the core logic: identifying even single-digit integers (0, 2, 4, 6, 8) 
    within the range [min(a, b), max(a, b)].
    """
    assert generate_integers(a, b) == expected

def test_generate_integers_return_properties():
    """
    Ensures the return type is a list and contains only integers.
    """
    result = generate_integers(2, 8)
    assert isinstance(result, list)
    assert all(isinstance(x, int) for x in result)

def test_generate_integers_order_and_symmetry():
    """
    Verifies that the output is always in ascending order and that 
    the result is identical regardless of input order (a, b) vs (b, a).
    """
    a, b = 8, 2
    res_asc = generate_integers(a, b)
    res_desc = generate_integers(b, a)
    
    # Check symmetry
    assert res_asc == res_desc
    # Check ascending order
    assert res_asc == sorted(res_asc)