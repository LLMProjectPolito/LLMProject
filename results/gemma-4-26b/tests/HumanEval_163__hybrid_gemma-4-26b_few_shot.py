
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

# Note: generate_integers is assumed to be imported or defined above

@pytest.mark.parametrize("a, b, expected", [
    # --- Standard Ranges ---
    (2, 8, [2, 4, 6, 8]),      # Standard even sequence
    (1, 5, [2, 4]),            # Standard range
    (3, 7, [4, 6]),            # Standard range
    (1, 9, [2, 4, 6, 8]),      # Range ending at odd boundary
    
    # --- Order Independence ---
    (8, 2, [2, 4, 6, 8]),      # Reversed range
    (5, 1, [2, 4]),            # Reversed range
    (7, 3, [4, 6]),            # Reversed range
    
    # --- Single Digit Boundaries & Edge Cases ---
    (0, 2, [0, 2]),            # Including zero
    (2, 2, [2]),               # a and b are the same even digit
    (3, 3, []),                # a and b are the same odd digit
    (2, 3, [2]),               # Even digit at the start
    (7, 8, [8]),               # Even digit at the end
    (1, 1, []),                # Single odd digit
    
    # --- No Even Digits in Single-Digit Range ---
    (1, 1, []),                # Single odd
    (3, 5, [4]),               # Single even in middle
    (5, 7, []),                # Only odd digits in range
    (9, 9, []),                # Boundary odd
    
    # --- Multi-digit & Large Value Ranges ---
    # (The function should only return single-digit evens: 0, 2, 4, 6, 8)
    (10, 14, []),              # Multi-digit range (no single digits)
    (10, 100, []),             # Large multi-digit range
    (100, 200, []),            # Very large range
    (1, 100, [2, 4, 6, 8]),    # Large gap spanning all single-digit evens
])
def test_generate_integers_scenarios(a, b, expected):
    """
    Comprehensive test covering standard ranges, reversed orders, 
    boundary conditions, and multi-digit exclusion.
    """
    assert generate_integers(a, b) == expected

def test_generate_integers_property_order_invariance():
    """
    Property-based test: Ensures that the result is identical 
    regardless of the order of arguments a and b.
    """
    test_cases = [(2, 6), (1, 9), (10, 2), (0, 5)]
    for a, b in test_cases:
        assert generate_integers(a, b) == generate_integers(b, a)

def test_generate_integers_is_always_sorted():
    """
    Property-based test: Ensures the returned list is always 
    in ascending order.
    """
    # Testing a wide range to ensure sorting logic holds
    result = generate_integers(10, 1)
    assert result == sorted(result)