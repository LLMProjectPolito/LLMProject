
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
    
    For example:
    double_the_difference([1, 3, 2, 0]) == 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    if not lst:
        return 0
    
    total = 0
    for num in lst:
        if isinstance(num, int) and num % 2 != 0:
            total += num * num
    return total

def test_double_the_difference_basic():
    # Test with a basic list of integers, including odd, even, and zero.
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_double_the_difference_negative():
    # Test with a list containing only negative numbers and zero.
    assert double_the_difference([-1, -2, 0]) == 0

def test_double_the_difference_mixed():
    # Test with a list containing a positive odd number and a negative even number.
    assert double_the_difference([9, -2]) == 81

def test_double_the_difference_zero():
    # Test with a list containing only zero.
    assert double_the_difference([0]) == 0

def test_double_the_difference_empty():
    # Test with an empty list.
    assert double_the_difference([]) == 0

def test_double_the_difference_with_floats():
    # Test with a list containing floats.  Floats should be ignored.
    assert double_the_difference([1.0, 3.0, 2.5, 0.0]) == 0

def test_double_the_difference_with_strings():
    # Test with a list containing strings. Strings should be ignored.
    assert double_the_difference(['1', '3', '2', '0']) == 0

def test_double_the_difference_with_mixed_types():
    # Test with a list containing a mix of integers, floats, and strings.
    assert double_the_difference([1, 3, 2.5, '0']) == 10

def test_double_the_difference_with_large_numbers():
    # Test with a list containing large odd numbers.
    assert double_the_difference([101, 103, 105]) == 101**2 + 103**2 + 105**2

def test_double_the_difference_with_all_even():
    # Test with a list containing only even numbers.
    assert double_the_difference([2, 4, 6, 8]) == 0

def test_double_the_difference_with_all_negative():
    # Test with a list containing only negative numbers.
    assert double_the_difference([-1, -3, -5]) == 0

def test_double_the_difference_with_single_odd():
    # Test with a list containing only a single odd number.
    assert double_the_difference([5]) == 25

def test_double_the_difference_with_larger_list():
    # Test with a larger list of odd numbers.  Use a smaller range for easier debugging.
    expected = sum(x**2 for x in range(1, 21, 2))
    assert double_the_difference(list(range(1, 21, 2))) == expected

def test_double_the_difference_with_none():
    # Test with a list containing None.  None should be ignored.
    assert double_the_difference([1, None, 3]) == 10