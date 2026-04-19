
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

def test_even_odd_count_basic():
    """Test standard positive integers with mixed digits."""
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(468135) == (3, 3)
    assert even_odd_count(10) == (1, 1)

def test_even_odd_count_negative():
    """Test that negative signs are ignored and only digits are counted."""
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-442) == (3, 0)
    assert even_odd_count(-135) == (0, 3)

def test_even_odd_count_zero():
    """Test the edge case of zero. Zero is considered an even digit."""
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_single_digits():
    """Test single digit boundaries."""
    assert even_odd_count(2) == (1, 0)
    assert even_odd_count(7) == (0, 1)

def test_even_odd_count_all_same_parity():
    """Test numbers consisting entirely of even or entirely of odd digits."""
    assert even_odd_count(2468) == (4, 0)
    assert even_odd_count(13579) == (0, 5)

def test_even_odd_count_large_number():
    """Test with a very large integer to ensure no overflow or performance issues."""
    num = 12345678901234567890
    # 10 even (2,4,6,8,0 x2), 10 odd (1,3,5,7,9 x2)
    assert even_odd_count(num) == (10, 10)

@pytest.mark.parametrize("invalid_input", [
    "123",       # String
    12.34,       # Float
    None,        # NoneType
    [],          # List
])
def test_even_odd_count_invalid_types(invalid_input):
    """
    Robustness check: Ensure the function handles or raises appropriate 
    errors when non-integer types are passed.
    """
    with pytest.raises((TypeError, ValueError)):
        even_odd_count(invalid_input)