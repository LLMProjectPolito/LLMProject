
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

@pytest.mark.parametrize("nums, expected", [
    # Examples provided in the prompt
    ([15, -73, 14, -15], 1),
    ([33, -2, -3, 45, 21, 109], 2),
    
    # Edge cases: Empty list, numbers <= 10, and single digits
    ([], 0),
    ([10], 0),
    ([9], 0),
    ([0], 0),
    ([1, 3, 5, 7, 9], 0),
    
    # Negative numbers (must be > 10)
    ([-11], 0),
    ([-15], 0),
    ([-11, -13, -15, -17, -19], 0),
    ([-11, -33, -55], 0),
    
    # Valid cases: Numbers > 10 with both first and last digits odd
    ([11], 1),
    ([13], 1),
    ([15], 1),
    ([17], 1),
    ([19], 1),
    ([31], 1),
    ([33], 1),
    ([55], 1),
    ([77], 1),
    ([99], 1),
    ([101], 1),
    ([103], 1),
    ([105], 1),
    ([107], 1),
    ([109], 1),
    ([301], 1),
    ([909], 1),
    ([1111], 1),
    ([13579], 1),
    ([1001], 1),
    ([1000000001, 3000000003], 2),
    
    # Invalid cases: Numbers > 10 but failing digit oddity
    ([12], 0),    # Last digit even
    ([21], 0),    # First digit even
    ([22], 0),    # Both even
    ([45], 0),    # First digit even
    ([100], 0),   # Last digit even
    ([209], 0),   # First digit even
    ([108], 0),   # Last digit even
    ([200], 0),   # Both even
    ([21, 41, 61, 81], 0), # All first digit even
    ([12, 14, 16, 18], 0), # All last digit even
    ([22, 44, 66, 88], 0), # All both even
    
    # Mixed lists
    ([11, 12, 21, 22], 1),
    ([11, 33, 55, 77, 99], 5),
    ([10, 20, 30, 40], 0),
    ([101, 202, 303, 404], 2),
    ([11, -11, 33, -33, 55, -55], 3),
    ([109, 11, 21, 12, 33], 3),
    ([11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 101], 6),
    ([111, 222, 333], 2),
    ([121, 141, 161], 3),
    ([11, 10, 1], 1),
    ([10, 11, 12], 1),
    ([101, 102, 201], 1),
])
def test_specialFilter(nums, expected):
    assert specialFilter(nums) == expected