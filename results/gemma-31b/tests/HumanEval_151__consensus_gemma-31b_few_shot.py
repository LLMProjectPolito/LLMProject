
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

def test_double_the_difference_basic():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0

def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

def test_double_the_difference_no_odds():
    assert double_the_difference([2, 4, 6, 8]) == 0
    assert double_the_difference([0, 2, -1, -3]) == 0

def test_double_the_difference_all_odds():
    assert double_the_difference([1, 3, 5]) == 35
    assert double_the_difference([7]) == 49

def test_double_the_difference_negatives():
    assert double_the_difference([-1, -3, -5]) == 0
    assert double_the_difference([1, -1, 3, -3]) == 10
    assert double_the_difference([-1, 1]) == 1

def test_double_the_difference_non_integers():
    # Should ignore floats, strings, None, and booleans
    assert double_the_difference([1, 3, 2.5, "3", None]) == 10
    assert double_the_difference([1.0, 3.0]) == 0
    assert double_the_difference([True, False]) == 0
    assert double_the_difference([1, 3.0, "a", None, 5]) == 35

def test_double_the_difference_mixed_types():
    # 1^2 + 5^2 = 26
    # Ignore: -3 (negative), 2 (even), 4.0 (float), "7" (string), -1.1 (negative float)
    assert double_the_difference([1, -3, 2, 4.0, "7", 5, -1.1]) == 26

@pytest.mark.parametrize("input_list, expected", [
    ([1, 3, 5, 7], 84),
    ([2, 4, 6], 0),
    ([1.1, 3.3, 5.5], 0),
    (["1", "3"], 0),
    ([101], 10201),
    ([-101], 0),
    ([0, 0, 0], 0),
    ([1, 1, 1], 3),
    ([7, 11], 170),
])
def test_double_the_difference_parametrized(input_list, expected):
    assert double_the_difference(input_list) == expected