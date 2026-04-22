
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
    sum_of_squares = 0
    for num in lst:
        if isinstance(num, int) and num >= 0 and num % 2 != 0:
            sum_of_squares += num * num
    return sum_of_squares

@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        ([1, 3, 2, 0], 10),
        ([-1, -2, 0], 0),
        ([9, -2], 81),
        ([0], 0),
        ([], 0),
        ([1, 2, 3, 4, 5], 35),
        ([-1, 1, 2, 3], 10),
        ([2, 4, 6], 0),
        ([1, 3, 5, 7, 9], 165),
        ([1.5, 2, 3], 9), #float test
        ([1, "a", 3], 10), #string test
        ([-1, 1, 2, 3.5], 10), #float test
        ([1, -1, 2, 3], 10),
        ([1, 3, 2, 0, -5], 10),
    ],
)
def test_double_the_difference(input_list, expected_output):
    assert double_the_difference(input_list) == expected_output

def test_empty_list():
    assert double_the_difference([]) == 0

def test_negative_numbers():
    assert double_the_difference([-1, -3, -5]) == 0

def test_zero_numbers():
    assert double_the_difference([0, 0, 0]) == 0

def test_mixed_numbers():
    assert double_the_difference([1, 2, 3, -4, 5]) == 35