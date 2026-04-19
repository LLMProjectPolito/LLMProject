
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
    """Test the examples explicitly mentioned in the docstring."""
    assert double_the_difference([1, 3, 2, 0]) == 10  # 1^2 + 3^2 = 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81       # 9^2 = 81
    assert double_the_difference([0]) == 0

def test_empty_list():
    """Test that an empty list returns 0."""
    assert double_the_difference([]) == 0

def test_all_even():
    """Test that only even positive integers result in 0."""
    assert double_the_difference([2, 4, 6, 8, 10]) == 0
    assert double_the_difference([0, 2, 0]) == 0

def test_all_negative():
    """Test that negative numbers (odd or even) are ignored."""
    assert double_the_difference([-1, -3, -5]) == 0
    assert double_the_difference([-2, -4, -6]) == 0
    assert double_the_difference([-1, -2, -3, -4]) == 0

def test_non_integers():
    """Test that floats and other non-integer types are ignored."""
    assert double_the_difference([1.5, 3.7, 2.0]) == 0
    assert double_the_difference([1, 3.0, 5]) == 26 # 1^2 + 5^2 = 26 (3.0 is float)
    assert double_the_difference(["1", None, [1]]) == 0

def test_mixed_valid_invalid():
    """Test a complex mix of all possible input types."""
    # Valid odds: 1, 5, 7 -> 1^2 + 5^2 + 7^2 = 1 + 25 + 49 = 75
    # Ignored: 2 (even), -3 (negative), 4.4 (float), 0 (even), -1.1 (negative float)
    input_list = [1, 2, -3, 5, 4.4, 0, 7, -1.1]
    assert double_the_difference(input_list) == 75

def test_large_odd_numbers():
    """Test with larger odd integers to ensure squaring is correct."""
    assert double_the_difference([11, 13]) == 121 + 169 # 290
    assert double_the_difference([101]) == 10201

@pytest.mark.parametrize("input_val, expected", [
    ([1], 1),
    ([2], 0),
    ([3], 9),
    ([1, 1, 1], 3),
    ([1, 2, 3], 10),
])
def test_parametrized_cases(input_val, expected):
    """Quick check of various small combinations."""
    assert double_the_difference(input_val) == expected