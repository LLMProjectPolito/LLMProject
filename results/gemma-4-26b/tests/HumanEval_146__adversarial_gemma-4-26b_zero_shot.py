
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

def specialFilter(nums):
    """
    Implementation of the function to be tested.
    Note: This is included so the test suite is runnable.
    """
    count = 0
    for n in nums:
        if n > 10:
            s = str(abs(n))
            first_digit = int(s[0])
            last_digit = int(s[-1])
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count

@pytest.mark.parametrize("input_list, expected", [
    # Provided examples
    ([15, -73, 14, -15], 1),
    ([33, -2, -3, 45, 21, 109], 2),
    
    # Boundary: Greater than 10
    ([10, 11, 9], 1),          # 10 is not > 10, 11 is, 9 is not
    ([11], 1),                 # Minimum valid number
    ([12], 0),                 # 12 is > 10, but last digit 2 is even
    
    # Condition: First digit must be odd
    ([21, 43, 65, 87], 0),     # All > 10, but first digits are even
    ([11, 31, 51, 71, 91], 5), # All > 10, first and last digits are odd
    
    # Condition: Last digit must be odd
    ([12, 34, 56, 78, 90], 0), # All > 10, first digits odd, but last digits even
    ([11, 33, 55, 77, 99], 5), # All > 10, first and last digits are odd
    
    # Condition: Mixed parity
    ([23, 12, 45, 14, 24], 0), # First even/Last odd, First odd/Last even, etc.
    
    # Negative numbers (Must be > 10, so all negatives should fail)
    ([-11, -13, -15, -31, -33], 0),
    ([-101, -103], 0),
    
    # Edge Cases: Empty and Singletons
    ([], 0),
    ([1], 0),
    ([11], 1),
    ([13], 1),
    
    # Large numbers
    ([1000000001, 3000000003, 2000000001], 2), # 1000000001 (1/1 odd), 3000000003 (3/3 odd), 2000000001 (2/1 mixed)
    ([9999999999], 1),
])
def test_special_filter_logic(input_list, expected):
    """Tests the core logic including boundaries and parity requirements."""
    assert specialFilter(input_list) == expected

def test_input_types():
    """Blue Team check: Ensure the function handles various numeric types if passed."""
    # Testing floats (if the requirement implies 'numbers' includes floats)
    # 11.1 is > 10, first digit 1 (odd), last digit 1 (odd)
    # Note: This depends on how the implementation handles string conversion of floats
    assert specialFilter([11.1, 13.5, 12.2]) == 2

def test_large_scale_performance():
    """Ensure the function can handle a large input array without crashing."""
    large_input = [11] * 10000
    assert specialFilter(large_input) == 10000

def test_all_even_digits():
    """Verify that numbers with all even digits are correctly excluded."""
    assert specialFilter([22, 44, 66, 88, 2468]) == 0

def test_all_odd_digits_but_small():
    """Verify that numbers with all odd digits but <= 10 are excluded."""
    assert specialFilter([1, 3, 5, 7, 9]) == 0