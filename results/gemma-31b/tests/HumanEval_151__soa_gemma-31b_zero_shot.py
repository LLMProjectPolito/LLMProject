
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
    ([1, 3, 2, 0], 10),        # 1^2 + 3^2 = 10
    ([-1, -2, 0], 0),          # Negatives and evens ignored
    ([9, -2], 81),             # 9^2 = 81
    ([0], 0),                  # Even ignored
    ([], 0),                   # Empty list
    ([1, 5, 7], 1 + 25 + 49),  # All odd: 75
    ([2, 4, 6], 0),            # All even
    ([-1, -3, -5], 0),         # All negative odd
    ([1.5, 2.5, 3.5], 0),      # All non-integers
    ([1, 2.0, 3], 10),         # 2.0 is a float, but is it an integer? 
                               # Prompt says "Ignore numbers that are... not integers"
                               # Usually means type(x) is not int.
    ([1, 3, -5, 2.2, 5], 35),  # 1^2 + 3^2 + 5^2 = 1 + 9 + 25 = 35
    ([101], 10201),            # Large odd number
    ([0, 0, 0], 0),            # Multiple zeros
])
def test_double_the_difference(lst, expected):
    assert double_the_difference(lst) == expected

def test_double_the_difference_non_numeric():
    """
    Testing behavior with non-numeric types if the function is expected 
    to handle them via the 'not integers' rule.
    """
    # Depending on implementation, this might raise TypeError or be ignored.
    # Given "Ignore numbers that are... not integers", we assume non-ints are skipped.
    try:
        assert double_the_difference([1, "3", None, 3]) == 10
    except TypeError:
        # If the function doesn't handle non-numeric types, this is acceptable 
        # unless the spec explicitly requires handling strings/None.
        pass