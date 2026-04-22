
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest
from your_module import specialFilter  # Replace 'your_module' with actual filename

@pytest.mark.parametrize("input_nums, expected", [
    # Provided examples
    ([15, -73, 14, -15], 1),           # Only 15: >10, first=1 (O), last=5 (O)
    ([33, -2, -3, 45, 21, 109], 2),    # 33 and 109: >10, first/last are odd
    
    # Boundary and Edge Cases
    ([], 0),                           # Empty list
    ([0], 0),                          # Zero
    ([10, 11, 12, 13], 2),             # 11 and 13 pass; 10 is not > 10
    ([1, 3, 5, 7, 9], 0),              # Single digits < 10
    ([-11, -13, -15], 0),              # Negative numbers (not > 10)
    
    # Digit Logic: First digit even
    ([21, 43, 65, 87, 201, 403], 0),   # All have even first digits
    
    # Digit Logic: Last digit even
    ([12, 34, 56, 78, 102, 304], 0),   # All have even last digits
    
    # Digit Logic: Large numbers
    ([10001, 10002, 20001, 10000, 30003], 2), # 10001 and 30003 pass
    
    # Mixed complex list
    ([11, 21, 12, 33, 43, 34, 101, 201], 3),  # 11, 33, 101 pass
])
def test_special_filter_logic(input_nums, expected):
    """
    Tests the core logic of specialFilter across various valid integer scenarios.
    """
    assert specialFilter(input_nums) == expected

def test_special_filter_type_safety():
    """
    Tests that the function raises TypeError when provided with invalid input types.
    """
    # Test non-list input
    with pytest.raises(TypeError):
        specialFilter(None)
    
    with pytest.raises(TypeError):
        specialFilter("not a list")
        
    # Test list containing invalid types
    with pytest.raises(TypeError):
        specialFilter([11, "13", 15])
        
    with pytest.raises(TypeError):
        specialFilter([11, 12.5, 13])