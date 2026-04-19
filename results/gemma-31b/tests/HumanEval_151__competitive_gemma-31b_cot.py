
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
    # Provided examples
    ([1, 3, 2, 0], 10),
    ([-1, -2, 0], 0),
    ([9, -2], 81),
    ([0], 0),
    # Edge cases
    ([], 0),
    ([2, 4, 6, 8], 0),
    ([1, 3, 5], 35),
    ([-1, -3, -5], 0),
    ([-2, -4, -6], 0),
    # Type handling (Ignore non-integers)
    ([1, 2.5, 3, "4", None, 5], 35),
    ([1.0, 3.0, 5.0], 0),
    ([True, False], 1), # Booleans are technically integers in Python (True=1), 
                        # but usually, "not integers" implies type checking.
                        # However, standard Python behavior for 'isinstance(True, int)' is True.
                        # If the function uses type(x) is int, True will be ignored.
                        # Given the prompt, I'll include a mix.
    # Mixed scenarios
    ([1, 3, 2, 0, -1, -2, 1.5, 'test', 7], 1 + 9 + 49),
    ([101], 10201),
])
def test_double_the_difference(input_list, expected):
    assert double_the_difference(input_list) == expected

def test_double_the_difference_large_list():
    # Test with a larger range of odd numbers
    lst = list(range(1, 11)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Odds: 1, 3, 5, 7, 9 -> Squares: 1, 9, 25, 49, 81 -> Sum: 165
    assert double_the_difference(lst) == 165

def test_double_the_difference_all_invalid():
    # Test with only negative and non-integer values
    lst = [-1, -3, -5, 1.1, 2.2, "odd", None]
    assert double_the_difference(lst) == 0