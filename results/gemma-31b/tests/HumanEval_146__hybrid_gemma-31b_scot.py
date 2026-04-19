
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

# The function specialFilter is assumed to be defined as per the problem description.
# We are testing it without redefining it here.

@pytest.mark.parametrize("nums, expected", [
    ([15, -73, 14, -15], 1),        # Example 1: Only 15 matches
    ([33, -2, -3, 45, 21, 109], 2), # Example 2: 33 and 109 match
])
def test_provided_examples(nums, expected):
    """Verify the function produces correct results for the provided docstring examples."""
    assert specialFilter(nums) == expected

def test_empty_list():
    """An empty list should return 0."""
    assert specialFilter([]) == 0

@pytest.mark.parametrize("nums, expected", [
    ([10], 0),       # Boundary: Exactly 10 is not > 10
    ([9], 0),        # Single digit odd is not > 10
    ([11], 1),       # Boundary: 11 is > 10 and both digits are odd
    ([0, -1, -9], 0),# Various values <= 10
])
def test_threshold_boundary(nums, expected):
    """Test numbers around the threshold of 10 to ensure strict inequality (>10)."""
    assert specialFilter(nums) == expected

def test_negative_numbers():
    """
    Negative numbers should be ignored even if their digits are odd, 
    because they are strictly less than 10.
    """
    # -73 has odd digits (7, 3), -11 has odd digits (1, 1), but both are < 10
    assert specialFilter([-73, -11, -131, -99]) == 0

@pytest.mark.parametrize("nums, expected", [
    ([11, 13, 15, 17, 19], 5),      # All satisfy (Odd-Odd)
    ([31, 53, 75, 97], 4),          # All satisfy (Odd-Odd)
    ([21, 43, 65, 87], 0),          # Fail: First digit even
    ([12, 34, 56, 78], 0),          # Fail: Last digit even
    ([22, 44, 66, 88], 0),          # Fail: Both digits even
    ([102, 304, 506], 0),           # Fail: First odd, last even
    ([201, 403, 605], 0),           # Fail: First even, last odd
    ([109, 301, 507], 3),           # Pass: First odd, last odd, middle digit irrelevant
])
def test_digit_parity_logic(nums, expected):
    """Test various combinations of first and last digit parity for numbers > 10."""
    assert specialFilter(nums) == expected

@pytest.mark.parametrize("nums, expected", [
    ([1000000001], 1), # Pass: 1...1
    ([3000000005], 1), # Pass: 3...5
    ([2000000001], 0), # Fail: 2...1 (First even)
    ([1000000002], 0), # Fail: 1...2 (Last even)
    ([9999999999], 1), # Pass: 9...9
])
def test_large_numbers(nums, expected):
    """Test very large numbers to ensure digit extraction logic is robust."""
    assert specialFilter(nums) == expected

def test_comprehensive_mix():
    """
    A high-complexity mix of passing and failing cases to ensure 
    no interference between elements in the list.
    """
    nums = [
        11,    # Pass: >10, Odd-Odd
        12,    # Fail: Last even
        21,    # Fail: First even
        22,    # Fail: Both even
        9,     # Fail: <= 10
        10,    # Fail: <= 10
        -11,   # Fail: <= 10
        101,   # Pass: >10, Odd-Odd
        505,   # Pass: >10, Odd-Odd
        409,   # Fail: First even
        500,   # Fail: Last even
        307,   # Pass: >10, Odd-Odd
    ]
    # Matches: 11, 101, 505, 307
    assert specialFilter(nums) == 4