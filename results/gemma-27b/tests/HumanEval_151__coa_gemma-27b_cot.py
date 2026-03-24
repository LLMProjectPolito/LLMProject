
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
import math


# Focus: Boundary Values
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
    if not lst:
        return 0
    
    total = 0
    for num in lst:
        if isinstance(num, int) and num >= 0 and num % 2 != 0:
            total += num * num
    return total

def test_empty_list():
    assert double_the_difference([]) == 0

def test_list_with_only_even_numbers():
    assert double_the_difference([2, 4, 6, 8]) == 0

def test_list_with_only_negative_numbers():
    assert double_the_difference([-1, -3, -5]) == 0

def test_list_with_zero():
    assert double_the_difference([0]) == 0

def test_list_with_one_odd_number():
    assert double_the_difference([1]) == 1

def test_list_with_one_even_number():
    assert double_the_difference([2]) == 0

# Focus: Invalid Input Handling
import pytest

def test_invalid_input_non_list():
    with pytest.raises(TypeError):
        double_the_difference("not a list")

def test_invalid_input_list_with_non_numeric():
    with pytest.raises(TypeError):
        double_the_difference([1, "a", 3])

def test_invalid_input_list_with_float():
    with pytest.raises(TypeError):
        double_the_difference([1, 2.5, 3])

# Focus: Logic Branches
import pytest

def test_empty_list():
    assert double_the_difference([]) == 0

def test_negative_and_non_integer_values():
    assert double_the_difference([-1, -2, 0, 2.5]) == 0

def test_mixed_odd_and_even_positive_integers():
    assert double_the_difference([1, 3, 2, 0]) == 10