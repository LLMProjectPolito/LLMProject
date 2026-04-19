
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
import math

@pytest.mark.parametrize("input_list, expected", [
    ([7, -7, 7.0, 0, 2, 3.14], 49),
    ([3.0, -3, 5.0, -5, 7, "9", None], 49),
    ([1, 3.0, -1, 5, 2, -3, 7.0], 26),
])
def test_double_the_difference_filtering(input_list, expected):
    """
    Tests that the function correctly filters for positive odd integers,
    ignoring negative numbers, even numbers, floats, and non-numeric types.
    """
    assert double_the_difference(input_list) == expected