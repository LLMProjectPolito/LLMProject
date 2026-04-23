
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
        ([1.5, 2, 3], 9),  # float input should be ignored
        ([1, "a", 3], 10), # string input should be ignored
        ([1, True, 3], 10), # boolean input should be ignored
        ([-1, 1, 0], 2),  # negative and zero should be ignored
        ([100], 0),
        ([1, 1, 1], 3),
        ([1, 1, 2, 1], 3),
        ([-1, 1, -1, 1], 2),
        ([10, 20, 30], 0),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 165)
    ],
)
def test_double_the_difference_basic(input_list, expected_output):
    assert double_the_difference(input_list) == expected_output

@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        ([1, 3, -5, 7, 9, -2], 1 + 9 + 49 + 81),  # Mixed positive/negative
        ([1, 3, 5, 7, -9], 1 + 9 + 25 + 49), #Mixed positive/negative
    ]
)
def test_double_the_difference_mixed_signs(input_list, expected_output):
    assert double_the_difference(input_list) == expected_output

@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        ([1000, 2000, 3000], 0), # Large numbers
        ([-1000, -2000, -3000], 0), # Large negative numbers
    ]
)
def test_double_the_difference_large_numbers(input_list, expected_output):
    assert double_the_difference(input_list) == expected_output

@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 1 + 9 + 25 + 49 + 81 + 121), # Long list
    ]
)
def test_double_the_difference_long_list(input_list, expected_output):
    assert double_the_difference(input_list) == expected_output