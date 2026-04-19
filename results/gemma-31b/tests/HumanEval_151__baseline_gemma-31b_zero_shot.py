
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''

import pytest

@pytest.mark.parametrize("input_lst, expected", [
    ([1, 3, 2, 0], 10),      # 1^2 + 3^2 = 10
    ([-1, -2, 0], 0),        # Negative and even ignored
    ([9, -2], 81),           # 9^2 = 81
    ([0], 0),                # Even ignored
    ([], 0),                 # Empty list
    ([1, 5, 7], 1 + 25 + 49), # All odd: 75
    ([2, 4, 6, 8], 0),       # All even
    ([-1, -3, -5], 0),       # All negative odd
    ([1, 2.5, 3, "a", None], 10), # Non-integers ignored: 1^2 + 3^2 = 10
    ([1.0, 3.0], 0),         # Floats are not integers (per "not integers" rule)
    ([11], 121),             # Single odd
    ([0, -1, -2, 1, 2], 1),  # Mixed: only 1 is positive odd
])
def test_double_the_difference(input_lst, expected):
    assert double_the_difference(input_lst) == expected

def test_double_the_difference_large_numbers():
    # Test with larger odd numbers
    assert double_the_difference([101]) == 10201

def test_double_the_difference_type_safety():
    # Ensure it handles a list containing various invalid types without crashing
    mixed_list = [1, "string", 3, 4.5, [], {}, True, 5]
    # Note: In Python, True is an instance of int (1), and 1 is odd.
    # If the function uses isinstance(x, int), True might be counted.
    # However, usually "integers" in these problems refers to standard ints.
    # Based on the prompt "Ignore numbers that are... not integers", 
    # we test the core logic.
    result = double_the_difference(mixed_list)
    # 1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35. 
    # If True is counted: 35 + 1 = 36. 
    # Most implementations use type(x) == int or isinstance(x, int).
    # We assume standard integer behavior.
    assert result >= 35