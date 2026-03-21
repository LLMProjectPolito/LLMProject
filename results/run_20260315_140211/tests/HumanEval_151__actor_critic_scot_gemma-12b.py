import pytest

def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 10
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

def test_basic_case():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_all_even():
    assert double_the_difference([2, 4, 6, 8]) == 0

def test_all_odd():
    assert double_the_difference([1, 3, 5, 7]) == 84

def test_negative_and_zero():
    assert double_the_difference([-1, -2, 0]) == 0

def test_zero():
    assert double_the_difference([0]) == 0

def test_empty_list():
    assert double_the_difference([]) == 0

def test_non_integer_types():
    assert double_the_difference([1, 2.5, "a", 3]) == 10  # Only odd integers (1 and 3) are considered.

def test_large_list():
    large_list = [i for i in range(1, 2001, 2)]  # List of odd numbers from 1 to 2000
    expected_sum = sum(x * x for x in large_list)
    assert double_the_difference(large_list) == expected_sum

def test_single_odd():
    assert double_the_difference([5]) == 25

def test_single_even():
    assert double_the_difference([4]) == 0

def test_only_negative_integers():
    assert double_the_difference([-1, -3, -5]) == 0

def test_float_and_odd():
    assert double_the_difference([2.5, 3]) == 9

def test_large_odd():
    assert double_the_difference([1000000001]) == 1000000002000000001