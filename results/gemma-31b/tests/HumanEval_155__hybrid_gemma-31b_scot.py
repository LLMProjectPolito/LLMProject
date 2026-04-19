
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

# The function even_odd_count is already defined in the environment.

@pytest.mark.parametrize("num, expected", [
    (123, (1, 2)),       # Mixed
    (468, (3, 0)),       # All even
    (135, (0, 3)),       # All odd
    (102, (2, 1)),       # Mixed with zero
    (2046, (4, 0)),      # All even with zero
    (442, (3, 0)),       # All even
    (2468, (4, 0)),      # All even
    (13579, (0, 5)),     # All odd
    (22222, (5, 0)),     # Uniform even
    (11111, (0, 5)),     # Uniform odd
    (888000, (6, 0)),    # Multiple zeros
    (999777, (0, 6)),    # Uniform odd
])
def test_even_odd_count_positive(num, expected):
    """Test positive integers including mixed, uniform parity, and zero-containing numbers."""
    assert even_odd_count(num) == expected

@pytest.mark.parametrize("num, expected", [
    (-12, (1, 1)),       # Mixed
    (-468, (3, 0)),      # All even
    (-135, (0, 3)),      # All odd
    (-102, (2, 1)),      # Mixed with zero
    (-7, (0, 1)),        # Single odd
    (-8, (1, 0)),        # Single even
    (-442, (3, 0)),      # All even
    (-9, (0, 1)),        # Single odd
])
def test_even_odd_count_negative(num, expected):
    """Test negative integers to ensure the sign does not affect the digit count."""
    assert even_odd_count(num) == expected

def test_even_odd_count_zero():
    """Test the edge case of zero, which is defined as an even digit."""
    assert even_odd_count(0) == (1, 0)

@pytest.mark.parametrize("num, expected", [
    (0, (1, 0)), (2, (1, 0)), (4, (1, 0)), (6, (1, 0)), (8, (1, 0)),
    (1, (0, 1)), (3, (0, 1)), (5, (0, 1)), (7, (0, 1)), (9, (0, 1)),
])
def test_even_odd_count_single_digits(num, expected):
    """Exhaustively test every single-digit possibility from 0-9."""
    assert even_odd_count(num) == expected

def test_even_odd_count_large_numbers():
    """Test very large integers to ensure stability and correct iteration."""
    # 10 digits: one '1' (odd), nine '0's (even)
    assert even_odd_count(1000000000) == (9, 1)
    
    # 10 digits: mixed (0-9)
    assert even_odd_count(1234567890) == (5, 5)
    
    # 20 digits: (0-9 repeated twice)
    num_huge = 12345678901234567890
    assert even_odd_count(num_huge) == (10, 10)

def test_even_odd_count_return_type():
    """Ensure the function returns a tuple of exactly two elements."""
    result = even_odd_count(123)
    assert isinstance(result, tuple)
    assert len(result) == 2

@pytest.mark.parametrize("invalid_input", [
    "123",          # String
    123.45,         # Float
    None,           # NoneType
    [1, 2, 3],      # List
])
def test_even_odd_count_invalid_input(invalid_input):
    """Verify that the function raises a TypeError when provided with non-integer inputs."""
    with pytest.raises((TypeError, ValueError)):
        even_odd_count(invalid_input)