
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
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for n in nums:
        if n > 10:
            s = str(n)
            first_digit = int(s[0])
            last_digit = int(s[-1])
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count

@pytest.mark.parametrize("input_nums, expected", [
    # Provided examples
    ([15, -73, 14, -15], 1),
    ([33, -2, -3, 45, 21, 109], 2),
    
    # Boundary cases for "greater than 10"
    ([10, 11, 12, 13], 2),  # 11 and 13 are > 10 and odd/odd. 10 is not > 10.
    ([9, 11], 1),           # 9 is not > 10.
    
    # Parity of first and last digits
    ([21, 43, 65, 87], 0),  # First digits are even (2, 4, 6, 8)
    ([12, 34, 56, 78], 0),  # Last digits are even (2, 4, 6, 8)
    ([22, 44, 66, 88], 0),  # Both even
    ([11, 33, 55, 77, 99], 5), # Both odd
    
    # Negative numbers (should always fail the > 10 condition)
    ([-11, -13, -15, -33], 0),
    ([-101, -303], 0),
    
    # Single digit numbers (should always fail the > 10 condition)
    ([1, 3, 5, 7, 9], 0),
    
    # Large numbers
    ([1001, 3003, 5005, 7007, 9009], 5),
    ([2001, 4003, 6005, 8007], 0),
    
    # Empty list and zeros
    ([], 0),
    ([0, 0, 0], 0),
    
    # Mixed complex case
    ([11, 13, 15, 17, 19, 21, 23, 31, 33, 10, 5, -11, 101], 8), 
    # Matches: 11, 13, 15, 17, 19, 31, 33, 101

    # Floating-point numbers (Clarifying behavior for non-integers)
    # 11.1 (1,1) -> Yes; 11.0 (1,0) -> No; 13.5 (1,5) -> Yes; 15.7 (1,7) -> Yes
    ([11.1, 11.0, 13.5, 15.7], 3),

    # Special float values
    # float('inf') is > 10, but lacks numeric digits; expected to be handled/skipped
    ([float('inf'), 11], 1),
])
def test_special_filter(input_nums, expected):
    assert specialFilter(input_nums) == expected

def test_type_error():
    """Check if the function handles unexpected input types robustly."""
    # Test with list of strings
    with pytest.raises(TypeError):
        specialFilter(["a", "b"])
    
    # Test with mixed-type list containing None
    with pytest.raises(TypeError):
        specialFilter([11, None, 13])