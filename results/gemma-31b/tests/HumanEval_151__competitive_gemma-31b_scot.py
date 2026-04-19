
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

@pytest.mark.parametrize("input_list, expected", [
    ([1, 3, 2, 0], 10),
    ([-1, -2, 0], 0),
    ([9, -2], 81),
    ([0], 0),
    ([], 0),
    ([1, 3, 5], 35),
    ([2, 4, 6, 8], 0),
    ([1, 2, 3, 4, 5], 35),
    ([-1, -3, -5], 0),
    ([1.5, 2.5, 3.5], 0),
    ([1, 2.0, 3], 10),
    ([3.0, 5.0], 0),
    ([1, "a", 3, None, 5], 35),
    ([7, -7, 11, -11], 170),
])
def test_double_the_difference(input_list, expected):
    assert double_the_difference(input_list) == expected

def test_large_numbers():
    assert double_the_difference([101]) == 10201

def test_all_non_integers():
    assert double_the_difference([1.1, "test", None, [], {}]) == 0