
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
    ([1, 3, 5.0, -7, "9", None, 2], 10),
    ([1, 3, -5, 2.2, '7', None, 5], 35),
    ([1, 5, -7, 2.2, '3'], 26),
])
def test_double_the_difference(input_list, expected):
    assert double_the_difference(input_list) == expected