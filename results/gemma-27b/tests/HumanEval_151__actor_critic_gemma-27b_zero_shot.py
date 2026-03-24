
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
        if isinstance(num, int) and num >= 0 and num % 2 != 0:
            sum_of_squares += num * num
    return sum_of_squares

def test_empty_list():
    assert double_the_difference([]) == 0

def test_odd_numbers():
    assert double_the_difference([1, 3, 5]) == 35

def test_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_mixed_numbers():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 0

def test_zero():
    assert double_the_difference([0]) == 0

def test_mixed_with_zero():
    assert double_the_difference([1, 0, 3, 0]) == 10

def test_ignores_floats():
    assert double_the_difference([1.0, 2.0, 3.0]) == 0

def test_float_that_would_be_odd():
    assert double_the_difference([3.0]) == 0

def test_mixed_integers_and_floats():
    assert double_the_difference([1, 2.0, 3]) == 10

def test_large_numbers():
    assert double_the_difference([99, 101]) == 20002

def test_single_odd_number():
    assert double_the_difference([5]) == 25

def test_single_even_number():
    assert double_the_difference([4]) == 0

def test_all_negative():
    assert double_the_difference([-1, -3, -5]) == 0

def test_string_input():
    assert double_the_difference(["1", "2", "3"]) == 0

def test_ignores_strings():
    assert double_the_difference([1, "2", 3]) == 10

def test_ignores_floats_and_strings():
    assert double_the_difference([1, "2", 3.0, 4]) == 17

def test_large_list():
    large_list = list(range(1, 1001))
    expected_sum = sum(x * x for x in large_list if x % 2 != 0)
    assert double_the_difference(large_list) == expected_sum

def test_very_large_numbers():
    assert double_the_difference([10**9 + 1, 10**9 + 2]) == (10**9 + 1)**2