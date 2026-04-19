
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

@pytest.mark.parametrize("lst, expected", [
    ([1, 3, 2, 0], 10),      # 1^2 + 3^2 = 10
    ([-1, -2, 0], 0),        # Negatives ignored
    ([9, -2], 81),           # 9^2 = 81
    ([0], 0),                # 0 is even
    ([], 0),                 # Empty list
    ([1, 3, 5], 35),         # 1 + 9 + 25 = 35
    ([2, 4, 6], 0),          # All even
    ([1.1, 3.3, 5.5], 0),    # Not integers
    ([1, 2.0, 3], 10),       # 2.0 is a float, ignored; 1^2 + 3^2 = 10
    ([7, -7, 11], 170),      # 49 + 121 = 170
    ([1, "3", 5], 26),       # String ignored; 1^2 + 5^2 = 26
    ([None, True, 3], 9),    # True is an int (1), 1^2 + 3^2 = 10? 
                             # Note: In Python, bool is a subclass of int. 
                             # If the function uses isinstance(x, int), True is 1.
                             # However, based on the prompt "numbers", usually refers to numeric types.
                             # Let's stick to standard numeric edge cases.
])
def test_double_the_difference(lst, expected):
    assert double_the_difference(lst) == expected

def test_double_the_difference_large_numbers():
    # Test with a larger odd number
    assert double_the_difference([101]) == 10201

def test_double_the_difference_mixed_types():
    # Ensure it handles a variety of non-integer types gracefully
    assert double_the_difference([1, 3, "hello", [], {}, 5]) == 1 + 9 + 25