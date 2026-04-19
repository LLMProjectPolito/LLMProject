
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
    ([1.5, "3", None, 3, 5, -7, 4, 0], 34),
    ([1, 3.0, -3, 5, 2], 26),
    ([3.0, -5, 4, 7, "string", None], 49),
])
def test_double_the_difference_filtering(input_list, expected):
    """
    Test that the function strictly filters for positive odd integers,
    ignoring floats, strings, None, negative numbers, and even integers.
    """
    assert double_the_difference(input_list) == expected