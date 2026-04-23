
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

@pytest.mark.parametrize("input_nums, expected", [
    # Provided examples
    ([15, -73, 14, -15], 1),
    ([33, -2, -3, 45, 21, 109], 2),
    
    # Edge case: Empty list
    ([], 0),
    
    # Edge case: No elements greater than 10
    ([1, 3, 5, 7, 9, 10], 0),
    
    # Edge case: Negative numbers (even if digits are odd, they are not > 10)
    ([-11, -13, -15, -33, -109], 0),
    
    # All elements meet criteria
    ([11, 33, 55, 77, 99, 135, 157], 7),
    
    # Elements meet > 10 but fail digit criteria
    ([12, 21, 22, 45, 67, 89, 10, 14, 16], 0), # 12 (last even), 21 (first even), etc.
    
    # Boundary condition: Exactly 10
    ([10, 11, 13], 2), # 10 is not > 10
    
    # Single digit numbers (not > 10)
    ([1, 3, 5, 7, 9], 0),
    
    # Large numbers
    ([1000000001, 3000000003, 2000000002, 4000000005], 2),
    
    # Mixed even/odd first and last digits
    ([11, 12, 21, 22, 31, 32, 41, 42], 2), # 11 and 31
])
def test_special_filter(input_nums, expected):
    """Tests the specialFilter function with various scenarios."""
    assert specialFilter(input_nums) == expected

def test_special_filter_type_error():
    """Tests that the function handles non-list inputs if necessary 
    (though standard implementation assumes list of numbers)."""
    with pytest.raises(TypeError):
        specialFilter(None)