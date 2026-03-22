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
    total = 0
    for num in lst:
        if isinstance(num, int) and num > 0 and num % 2 != 0:
            total += num * num
    return total

def test_double_the_difference_empty_list():
    assert double_the_difference([]) == 0

def test_double_the_difference_positive_odd_numbers():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_double_the_difference_negative_numbers():
    assert double_the_difference([-1, -2, 0]) == 0

def test_double_the_difference_mixed_numbers():
    assert double_the_difference([9, -2]) == 81

def test_double_the_difference_single_zero():
    assert double_the_difference([0]) == 0

def test_double_the_difference_single_positive_odd():
    assert double_the_difference([1]) == 1

def test_double_the_difference_single_negative_odd():
    assert double_the_difference([-1]) == 0

def test_double_the_difference_with_zeros_and_odds():
    assert double_the_difference([1, 0, 3, 0, 5]) == 1 + 9 + 25 == 35

def test_double_the_difference_large_numbers():
    assert double_the_difference([1001, 1003]) == 1001*1001 + 1003*1003

def test_double_the_difference_with_negative_and_positive_odds():
    assert double_the_difference([-1, 3, -5, 7]) == 1 + 9 + 25 + 49 == 84

def test_double_the_difference_non_integer_values():
    assert double_the_difference([1.5, 2, 3]) == 0

def test_double_the_difference_mixed_types():
    assert double_the_difference([1, "a", 3, 2.5]) == 1 + 9 == 10