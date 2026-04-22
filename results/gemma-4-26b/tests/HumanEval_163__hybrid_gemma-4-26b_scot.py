
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

# Assuming the function is available in the environment/main module
from __main__ import generate_integers

@pytest.mark.parametrize("a, b, expected", [
    # --- Standard Scenarios ---
    (2, 8, [2, 4, 6, 8]),      # Full single-digit even range
    (8, 2, [2, 4, 6, 8]),      # Descending order input
    (2, 7, [2, 4, 6]),         # Partial range (end)
    (3, 8, [4, 6, 8]),         # Partial range (start)
    (1, 9, [2, 4, 6, 8]),      # Wide single-digit range
    
    # --- Single Digit / Boundary Cases ---
    (4, 4, [4]),               # Single even digit
    (3, 3, []),                # Single odd digit
    (5, 5, []),                # Single odd digit
    (0, 2, [2]),               # Zero boundary
    (1, 3, [2]),               # Small range
    (7, 9, [8]),               # Small range
    
    # --- Digit Transition (The 9 to 10 boundary) ---
    (8, 10, [8]),              # Includes 8, stops before 10
    (9, 11, []),               # No single-digit evens
    (5, 12, [6, 8]),           # Transitions past single digits
    
    # --- No Even Digits in Range ---
    (1, 1, []),                # Single value, odd
    (3, 5, [4]),               # Corrected: 4 is an even digit in [3, 5]
    (11, 13, []),              # All numbers > 9
    
    # --- Out of Bounds / Large Values ---
    (10, 14, []),              # All numbers > 9
    (100, 200, []),            # Very large numbers
    (1000, 2000, []),          # Very large numbers
    (1, 1000, [2, 4, 6, 8]),  # Large range, should only pick single digits
    (2, 1000, [2, 4, 6, 8]),  # Large range
])
def test_generate_integers_parametrized(a, b, expected):
    """
    Comprehensive test covering standard ranges, descending inputs, 
    single-digit boundaries, and large integer values.
    """
    assert generate_integers(a, b) == expected

def test_return_type():
    """Ensures the return type is always a list, even if empty."""
    assert isinstance(generate_integers(2, 4), list)
    assert isinstance(generate_integers(10, 20), list)
    assert isinstance(generate_integers(1, 1), list)

def test_order_independence():
    """Ensures the function is agnostic to the order of a and b."""
    a, b = 2, 9
    assert generate_integers(a, b) == generate_integers(b, a)

def test_ascending_order():
    """Explicitly checks that the output is always in ascending order."""
    # Test with descending input to ensure output is sorted
    result = generate_integers(8, 2)
    assert result == sorted(result)
    # Test with a range that might tempt non-sorted logic
    assert generate_integers(9, 1, [2, 4, 6, 8]) == [2, 4, 6, 8]

def test_docstring_examples():
    """Verify the specific examples provided in the function's docstring."""
    # This ensures documentation remains accurate to implementation
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []