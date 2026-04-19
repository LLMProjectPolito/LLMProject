
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
    ([1, 3, 2, 0], 10),
    ([-1, -2, 0], 0),
    ([9, -2], 81),
    ([0], 0),
    ([], 0),
    ([1, 3, 5], 35),
    ([2, 4, 6], 0),
    ([-1, -3, -5], 0),
    ([1, 2, 3, 4, 5], 35),
    ([1.5, 2.5, 3.5], 0),
    ([1, "a", 3, None, 5], 35),
    ([7, -7, 0], 49),
    ([11], 121),
    ([0, 0, 0], 0),
])
def test_double_the_difference(lst, expected):
    assert double_the_difference(lst) == expected

def test_double_the_difference_non_int_types():
    # Specifically testing a mix of types to ensure robustness
    input_list = [1, 3, "string", 2.2, None, [1], {1}, 5]
    # Odd integers are 1, 3, 5 -> 1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35
    assert double_the_difference(input_list) == 35

def test_double_the_difference_large_numbers():
    input_list = [101, 1]
    # 101^2 + 1^2 = 10201 + 1 = 10202
    assert double_the_difference(input_list) == 10202