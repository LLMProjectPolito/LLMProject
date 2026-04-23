
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

def test_provided_examples():
    """Validates the specific examples provided in the problem description."""
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_edge_cases_and_boundaries():
    """Tests empty lists, single elements, and the boundary condition around 10."""
    # Empty list
    assert specialFilter([]) == 0
    # Single element: Pass
    assert specialFilter([13]) == 1
    # Single element: Fail (Even last digit)
    assert specialFilter([12]) == 0
    # Single element: Fail (Too small)
    assert specialFilter([5]) == 0
    # Boundary: 9 is < 10
    assert specialFilter([9]) == 0
    # Boundary: 10 is not > 10
    assert specialFilter([10]) == 0
    # Boundary: 11 is > 10 and both digits are odd
    assert specialFilter([11]) == 1

def test_negative_numbers():
    """
    Negative numbers must return 0 (or not be counted) because they are not > 10,
    even if their digits are odd.
    """
    assert specialFilter([-11, -13, -15, -31, -73]) == 0
    # Mixed negative and positive
    assert specialFilter([-15, 15]) == 1

@pytest.mark.parametrize("num, expected", [
    (13, 1),    # Odd/Odd, > 10 -> Pass
    (12, 0),    # Odd/Even, > 10 -> Fail
    (23, 0),    # Even/Odd, > 10 -> Fail
    (22, 0),    # Even/Even, > 10 -> Fail
    (307, 1),   # Odd/Odd, > 10 -> Pass
    (401, 0),   # Even/Odd, > 10 -> Fail
    (502, 0),   # Odd/Even, > 10 -> Fail
    (809, 0),   # Even/Odd, > 10 -> Fail
    (10001, 1), # Odd/Odd, > 10 -> Pass
])
def test_digit_parity_logic(num, expected):
    """Tests the core logic of digit parity for individual numbers > 10."""
    assert specialFilter([num]) == expected

def test_large_and_multi_digit_numbers():
    """Tests numbers with many digits and extremely large integers."""
    # Multi-digit: 109 (O/O, >10), 100 (O/E), 201 (E/O), 357 (O/O), 1000 (O/E)
    assert specialFilter([109, 100, 201, 357, 1000]) == 2
    
    # Extremely large number: 1st digit 1 (O), last digit 7 (O), > 10
    assert specialFilter([1234567891234567891234567897]) == 1
    # Extremely large number: 1st digit 2 (E), last digit 7 (O), > 10
    assert specialFilter([222222222222222222222222222222222227]) == 0
    # Extremely large number: 1st digit 1 (O), last digit 8 (E), > 10
    assert specialFilter([111111111111111111111111111111111118]) == 0

def test_complex_mixed_lists():
    """Tests various combinations of numbers in a single list to ensure correct counting."""
    # 13 (Pass), 25 (Fail-E/O), 10 (Fail-<10), 7 (Fail-<10), 99 (Pass), -13 (Fail-<10), 44 (Fail-E/E), 101 (Pass)
    # Expected: 13, 99, 101 -> 3
    nums = [13, 25, 10, 7, 99, -13, 44, 101]
    assert specialFilter(nums) == 3

    # All fail scenario
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 20, 22]) == 0
    
    # All pass scenario
    assert specialFilter([11, 33, 55, 77, 99]) == 5