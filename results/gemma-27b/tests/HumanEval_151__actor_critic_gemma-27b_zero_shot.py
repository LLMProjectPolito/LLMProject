
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
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    if not lst:
        return 0
    
    sum_of_squares = 0
    for num in lst:
        if isinstance(num, int) and num % 2 != 0 and num >= 0:
            sum_of_squares += num * num
    return sum_of_squares

def test_empty_list():
    assert double_the_difference([]) == 0

def test_positive_odd_numbers():
    assert double_the_difference([1, 3, 5]) == 35

def test_mixed_positive_numbers():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_mixed_positive_and_negative():
    assert double_the_difference([1, -2, 3, -4]) == 10

def test_zero():
    assert double_the_difference([0]) == 0

def test_floats():
    assert double_the_difference([1.0, 2.0, 3.0]) == 0

def test_mixed_integers_and_floats():
    assert double_the_difference([1, 2.0, 3]) == 10

def test_large_numbers():
    assert double_the_difference([99, 101]) == 9801 + 10201

def test_single_odd_number():
    assert double_the_difference([5]) == 25

def test_non_numeric_input():
    assert double_the_difference(["a", 1, 2]) == 1

def test_mixed_data_types():
    assert double_the_difference([1, 2.0, "a", 3]) == 10

def test_large_list():
    large_list = list(range(1, 1001, 2))  # List of odd numbers from 1 to 999
    expected_sum = sum(x * x for x in large_list)
    assert double_the_difference(large_list) == expected_sum

def test_only_negative_odd_numbers():
    assert double_the_difference([-1, -3, -5]) == 0