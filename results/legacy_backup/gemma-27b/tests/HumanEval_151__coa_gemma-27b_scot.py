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

def test_double_the_difference_empty_list():
    assert double_the_difference([]) == 0

def test_double_the_difference_zero():
    assert double_the_difference([0]) == 0

def test_double_the_difference_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 0

def test_double_the_difference_positive_and_negative():
    assert double_the_difference([-1, 1, -2, 3]) == 10

def test_double_the_difference_max_int():
    assert double_the_difference([2**31 - 1]) == (2**31 - 1)**2

def test_double_the_difference_min_non_negative_int():
    assert double_the_difference([0]) == 0

def test_double_the_difference_large_odd_number():
    assert double_the_difference([999]) == 999**2

# Focus: Invalid Input Handling
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

def test_invalid_input_non_integer():
    """Test with a list containing non-integer values."""
    assert double_the_difference([1, 2.5, 3, "a"]) == 1 + 9
    assert double_the_difference(["hello", 1, 3]) == 1 + 9

def test_invalid_input_negative_numbers():
    """Test with a list containing negative numbers."""
    assert double_the_difference([-1, -3, 1, 3]) == 1 + 9
    assert double_the_difference([1, -2, 3, -4]) == 1 + 9

def test_invalid_input_mixed_types():
    """Test with a list containing mixed types, including negative and non-integer."""
    assert double_the_difference([-1, 2.5, 3, "a", 5]) == 9 + 25

# Focus: Logic Branches
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

def test_negative_and_even_numbers():
    assert double_the_difference([-1, -2, 0, 2, 4]) == 0

def test_mixed_positive_odd_and_even():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_only_odd_numbers():
    assert double_the_difference([1, 3, 5]) == 35

def test_only_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_single_odd_number():
    assert double_the_difference([9]) == 81

def test_single_even_number():
    assert double_the_difference([2]) == 0

def test_mixed_with_negative():
    assert double_the_difference([9, -2]) == 81

def test_mixed_with_floats():
    assert double_the_difference([1, 2.5, 3, 4]) == 10