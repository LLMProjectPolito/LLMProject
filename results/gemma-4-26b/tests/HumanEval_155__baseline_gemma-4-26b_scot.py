
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

@pytest.mark.parametrize("input_num, expected", [
    (123, (1, 2)),          # Mixed: 1 even (2), 2 odd (1, 3)
    (444, (3, 0)),          # All even
    (135, (0, 3)),          # All odd
    (-12, (1, 1)),          # Negative mixed
    (-468, (3, 0)),         # Negative all even
    (0, (1, 0)),            # Zero is even
    (7, (0, 1)),            # Single odd
    (8, (1, 0)),            # Single even
    (1029384756, (5, 5)),   # Large mixed
    (24680, (5, 0)),        # Large all even (including zero)
])
def test_even_odd_count_parametrized(input_num, expected):
    """Test various integer inputs against expected even/odd counts."""
    assert even_odd_count(input_num) == expected

def test_even_odd_count_return_type():
    """Verify that the function returns a tuple of two integers."""
    result = even_odd_count(123)
    assert isinstance(result, tuple), "Output should be a tuple"
    assert len(result) == 2, "Tuple should have exactly two elements"
    assert isinstance(result[0], int), "First element should be an integer"
    assert isinstance(result[1], int), "Second element should be an integer"

def test_even_odd_count_large_number():
    """Explicitly test a very large integer for stability."""
    large_num = 98765432109876543210
    # Digits: 9,8,7,6,5,4,3,2,1,0 (repeated twice)
    # Evens: 8,6,4,2,0 (5 digits) * 2 = 10
    # Odds: 9,7,5,3,1 (5 digits) * 2 = 10
    assert even_odd_count(large_num) == (10, 10)