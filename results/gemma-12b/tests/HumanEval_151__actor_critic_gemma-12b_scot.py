
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
from your_module import double_the_difference  # Replace your_module

def test_empty_list():
    assert double_the_difference([]) == 0

def test_positive_odd_numbers():
    assert double_the_difference([1, 3, 5]) == 1**2 + 3**2 + 5**2

def test_positive_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_mixed_numbers():
    assert double_the_difference([1, 2, 3, 4, 5]) == 1**2 + 3**2 + 5**2

def test_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 0

def test_zero():
    assert double_the_difference([0]) == 0

def test_duplicate_numbers():
    assert double_the_difference([1, 1, 2]) == 1**2 + 1**2

def test_non_integer_numbers():
    assert double_the_difference([1.5, 2.5, 3.5]) == 1.5**2 + 2.5**2 + 3.5**2

def test_mixed_types():
    assert double_the_difference([1, 2.5, -3, 4, 5]) == 1**2 + 2.5**2 + 4**2 + 5**2

def test_invalid_input_type():
    with pytest.raises(TypeError):
        double_the_difference(123)

def test_non_numeric_values():
    with pytest.raises(TypeError):
        double_the_difference(["a", "b", "c"])