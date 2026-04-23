
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

def test_empty_list():
    """Verify that an empty list returns 0."""
    assert double_the_difference([]) == 0

def test_no_valid_elements():
    """Verify that lists with no valid odd positive integers return 0."""
    # All even
    assert double_the_difference([2, 4, 6, 8]) == 0
    # All negative
    assert double_the_difference([-1, -3, -5]) == 0
    # All floats
    assert double_the_difference([1.1, 3.3, 5.5]) == 0
    # Mixed invalid: negative odd, positive even, float odd
    assert double_the_difference([-3, 2, 5.0]) == 0
    # Zero (even)
    assert double_the_difference([0]) == 0

def test_valid_elements():
    """Verify that a list of valid odd positive integers returns the correct sum of squares."""
    # 1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35
    assert double_the_difference([1, 3, 5]) == 35
    # Single element
    assert double_the_difference([7]) == 49

def test_mixed_elements():
    """Verify a complex list with mixed types and values."""
    # Valid: 1, 3, 9 -> 1^2 + 3^2 + 9^2 = 1 + 9 + 81 = 91
    # Invalid: -1 (neg), 2 (even), 4.0 (float), 0 (even), -5 (neg)
    input_list = [1, 3, 2, 0, -1, 4.0, 9, -5]
    assert double_the_difference(input_list) == 91

@pytest.mark.parametrize("input_lst, expected", [
    ([1, 3, 2, 0], 10),
    ([-1, -2, 0], 0),
    ([9, -2], 81),
    ([0], 0),
])
def test_provided_examples(input_lst, expected):
    """Verify the specific examples provided in the problem description."""
    assert double_the_difference(input_lst) == expected

def test_large_numbers():
    """Verify the function handles larger integers correctly."""
    # 11^2 + 13^2 = 121 + 169 = 290
    assert double_the_difference([11, 13, 10, 12]) == 290