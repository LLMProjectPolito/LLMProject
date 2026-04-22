
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
    """Tests the examples provided in the problem description."""
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_empty_list():
    """Tests that an empty list returns 0."""
    assert specialFilter([]) == 0

def test_no_elements_greater_than_10():
    """Tests that numbers <= 10 are ignored, even if they have odd digits."""
    assert specialFilter([1, 3, 5, 7, 9, 10, 0, -1, -11, -13]) == 0

def test_boundary_values():
    """Tests boundary values around 10."""
    assert specialFilter([10]) == 0  # Must be > 10
    assert specialFilter([11]) == 1  # First=1, Last=1, > 10
    assert specialFilter([12]) == 0  # Last digit even

def test_negative_numbers():
    """Tests that negative numbers are excluded even if their digits are odd."""
    assert specialFilter([-11, -13, -31, -33, -101]) == 0

def test_first_digit_even():
    """Tests numbers > 10 where the first digit is even."""
    # 21 (2), 43 (4), 65 (6), 87 (8), 201 (2)
    assert specialFilter([21, 43, 65, 87, 201]) == 0

def test_last_digit_even():
    """Tests numbers > 10 where the last digit is even."""
    # 12 (2), 34 (4), 56 (6), 78 (8), 102 (2)
    assert specialFilter([12, 34, 56, 78, 102]) == 0

def test_both_digits_even():
    """Test numbers > 10 where both first and last digits are even."""
    assert specialFilter([22, 44, 66, 88, 202, 404]) == 0

def test_all_conditions_met():
    """Test numbers > 10 where both first and last digits are odd."""
    # 11, 13, 31, 33, 55, 77, 99, 101, 135, 1009
    assert specialFilter([11, 13, 31, 33, 55, 77, 99, 101, 135, 1009]) == 10

def test_large_numbers():
    """Tests very large numbers with odd first and last digits."""
    assert specialFilter([100000000000000000001, 300000000000000000003, 200000000000000000002]) == 2

def test_mixed_input():
    """Tests complex mixes of valid and invalid numbers."""
    # Mix 1: 11 (Y), 12 (N), 21 (N), 22 (N), 33 (Y), -11 (N), 101 (Y), 45 (N), 7 (N)
    assert specialFilter([11, 12, 21, 22, 33, -11, 101, 45, 7]) == 3
    # Mix 2: 15 (Y), 22 (N), 33 (Y), 44 (N), 55 (Y), 66 (N), 77 (Y), 88 (N), 99 (Y), 11 (Y), 10 (N), 101 (Y)
    assert specialFilter([15, 22, 33, 44, 55, 66, 77, 88, 99, 11, 10, 101]) == 7

@pytest.mark.parametrize("nums, expected", [
    ([13, 15, 17, 19], 4),
    ([11, 12, 13, 14, 15], 3),
    ([101, 102, 103, 104, 105], 3),
    ([5, 7, 9, 11, 13], 2),
    ([20, 30, 40, 50], 0),
])
def test_parametrized_cases(nums, expected):
    """Parametrized test for various scenarios."""
    assert specialFilter(nums) == expected