
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
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    sum_of_squares = 0
    for num in lst:
        if isinstance(num, int) and num >= 0 and num % 2 != 0:
            sum_of_squares += num * num
    return sum_of_squares

def test_empty_list():
    assert double_the_difference([]) == 0

def test_positive_odd_numbers():
    assert double_the_difference([1, 3, 5]) == 35

def test_positive_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_mixed_positive_numbers():
    assert double_the_difference([1, 2, 3, 4, 5]) == 35

def test_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 0

def test_mixed_positive_and_negative_numbers():
    assert double_the_difference([-1, 2, 3, -4, 5]) == 34

def test_zero():
    assert double_the_difference([0]) == 0

def test_mixed_numbers_with_zero():
    assert double_the_difference([0, 1, 2, 3, 4, 5]) == 35

def test_non_integer_numbers():
    assert double_the_difference([1.5, 2, 3.5, 4]) == 0

def test_mixed_integer_and_non_integer_numbers():
    assert double_the_difference([1, 2.5, 3, 4.5, 5]) == 35

def test_string_in_list():
    assert double_the_difference([1, "a", 3]) == 10

def test_boolean_in_list():
    assert double_the_difference([1, True, 3]) == 10
    assert double_the_difference([False, 1, 3]) == 10

def test_large_numbers():
    assert double_the_difference([1001, 1003]) == 2008010

def test_single_odd_number():
    assert double_the_difference([7]) == 49

def test_single_even_number():
    assert double_the_difference([8]) == 0

def test_none_in_list():
    assert double_the_difference([1, None, 3]) == 10
    assert double_the_difference([None]) == 0

def test_list_with_only_non_positive_numbers():
    assert double_the_difference([-1, -3, 0]) == 0

def test_very_large_list():
    large_list = list(range(1000))
    odd_numbers = [x for x in large_list if x % 2 != 0]
    expected_sum = sum(x * x for x in odd_numbers)
    assert double_the_difference(large_list) == expected_sum