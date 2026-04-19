
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

def test_special_filter_examples():
    """Test the examples provided in the docstring"""
    assert specialFilter([15, -73, 14, -15]) == 1
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_special_filter_empty():
    """Test with an empty list"""
    assert specialFilter([]) == 0

def test_special_filter_boundary_10():
    """Test numbers around the threshold of 10"""
    # 10 is not greater than 10
    assert specialFilter([10]) == 0
    # 11 is > 10 and both digits are odd
    assert specialFilter([11]) == 1

def test_special_filter_negatives():
    """Test that negative numbers are excluded regardless of digits"""
    # -11 has odd digits but is not > 10
    assert specialFilter([-11, -33, -55]) == 0

def test_special_filter_digit_parity():
    """Test various combinations of odd/even first and last digits"""
    # First even, last odd (e.g., 21) -> False
    # First odd, last even (e.g., 12) -> False
    # First even, last even (e.g., 22) -> False
    # First odd, last odd (e.g., 13) -> True
    assert specialFilter([21, 12, 22, 13]) == 1

def test_special_filter_single_digits():
    """Test that single digit numbers are excluded (since they are not > 10)"""
    assert specialFilter([1, 3, 5, 7, 9]) == 0

def test_special_filter_large_numbers():
    """Test multi-digit numbers"""
    # 13579: > 10, first=1 (odd), last=9 (odd) -> True
    # 23579: > 10, first=2 (even), last=9 (odd) -> False
    # 13572: > 10, first=1 (odd), last=2 (even) -> False
    assert specialFilter([13579, 23579, 13572]) == 1

def test_special_filter_all_fail():
    """Test a list where no elements meet the criteria"""
    assert specialFilter([2, 4, 6, 8, 10, 20, 40, 60]) == 0

def test_special_filter_all_pass():
    """Test a list where all elements meet the criteria"""
    assert specialFilter([11, 33, 55, 77, 99, 101]) == 6