
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

def test_provided_examples():
    """Test the cases explicitly mentioned in the docstring."""
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0

def test_empty_list():
    """Test that an empty list returns 0."""
    assert double_the_difference([]) == 0

def test_parity_and_sign_logic():
    """Test combinations of positive/negative and even/odd integers."""
    # Only positive even numbers
    assert double_the_difference([2, 4, 6, 8, 10]) == 0
    # Only positive odd numbers: 1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35
    assert double_the_difference([1, 3, 5]) == 35
    # Negative odd numbers should be ignored
    assert double_the_difference([-1, -3, -5]) == 0
    # Mixed positive/negative integers: 1^2 + 7^2 = 50
    assert double_the_difference([1, -1, 7, -7, 2, -2]) == 50

def test_non_integer_types():
    """Test that floats, strings, None, and other non-int types are ignored."""
    # 3 and 5 are positive odd ints. 3.0 is float, "7" is str, None is None, [1] is list.
    # 3^2 + 5^2 = 9 + 25 = 34
    assert double_the_difference([3, 5, 3.0, "7", None, 2.1, [1]]) == 34
    # Only 7 is a positive odd int
    assert double_the_difference([3.0, '5', None, 7]) == 49

def test_boolean_handling():
    """
    Test how the function handles booleans. 
    In Python, bool is a subclass of int (True == 1, False == 0).
    True should be treated as 1 (positive odd).
    """
    assert double_the_difference([True, False]) == 1

def test_mixed_valid_invalid():
    """Test a comprehensive combination of valid and invalid inputs."""
    # Valid: 1, 3 -> 1^2 + 3^2 = 10
    # Invalid: -1 (neg), 2 (even), 4.5 (float), '7' (str), -9 (neg)
    assert double_the_difference([1, -1, 2, 3, 4.5, '7', -9]) == 10

def test_large_numbers():
    """Test with large odd integers to ensure squaring and summation are correct."""
    assert double_the_difference([101]) == 10201
    assert double_the_difference([1000001]) == 1000002000001

@pytest.mark.parametrize("input_lst, expected", [
    ([1], 1),
    ([2], 0),
    ([-1], 0),
    ([1, 1, 1], 3),
    ([0, 0, 0], 0),
    ([1, 2, 3, 4, 5], 35),
    ([1.1, 2.2, 3.3], 0),
    (["1", "3"], 0),
    ([], 0),
])
def test_parametrized_cases(input_lst, expected):
    """General purpose parametrization for variety and edge cases."""
    assert double_the_difference(input_lst) == expected