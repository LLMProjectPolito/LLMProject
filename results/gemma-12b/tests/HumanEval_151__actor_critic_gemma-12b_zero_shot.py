
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
    assert double_the_difference([1, 3, 5]) == 35

def test_mixed_positive_and_even_numbers():
    assert double_the_difference([1, 2, 3, 4, 5]) == 35

def test_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 0

def test_negative_and_positive_numbers():
    assert double_the_difference([-1, 1, -2, 2, 3]) == 19

def test_zero():
    assert double_the_difference([0]) == 0

def test_zero_and_odd():
    assert double_the_difference([0, 1, 3]) == 10

def test_zero_and_even():
    assert double_the_difference([0, 2, 4]) == 0

def test_all_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_single_odd_number():
    assert double_the_difference([7]) == 49

def test_single_negative_number():
    assert double_the_difference([-5]) == 0

def test_mixed_positive_negative_even_odd():
    assert double_the_difference([1, -2, 3, -4, 5, -6]) == 91

def test_large_numbers():
    assert double_the_difference([101, 203]) == 51410

def test_single_positive_number():
    assert double_the_difference([1]) == 1

def test_single_large_number():
    assert double_the_difference([9]) == 81

def test_non_integer_input():
    with pytest.raises(TypeError):
        double_the_difference([1.5, 2, 3.0])

def test_string_input():
    with pytest.raises(TypeError):
        double_the_difference(["a", 1, 2])

def test_boolean_input():
    with pytest.raises(TypeError):
        double_the_difference([True, 1, 2])

def test_list_input():
    with pytest.raises(TypeError):
        double_the_difference([[1], 1, 2])