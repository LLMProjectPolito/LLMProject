
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
    if not lst:
        return 0
    
    sum_of_squares = 0
    for num in lst:
        if isinstance(num, int) and num > 0 and num % 2 != 0:
            sum_of_squares += num * num
    return sum_of_squares

def test_empty_list():
    assert double_the_difference([]) == 0

def test_positive_odd_numbers():
    assert double_the_difference([1, 3, 5]) == 35

def test_mixed_positive_and_negative():
    assert double_the_difference([1, -3, 5]) == 35

def test_only_negative_numbers():
    assert double_the_difference([-1, -3, -5]) == 0

def test_only_positive_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_zero_in_list():
    assert double_the_difference([0, 1, 3]) == 10

def test_mixed_positive_negative_and_zero():
    assert double_the_difference([1, -2, 0, 3]) == 10

def test_large_odd_numbers():
    assert double_the_difference([1000000001, 1000000003]) == 2000000006

def test_negative_and_zero_and_positive_odd():
    assert double_the_difference([-1, 0, 1, 2, 3]) == 10

def test_non_integer_values():
    assert double_the_difference([1.5, 2, 3]) == 0

def test_strings_in_list():
    assert double_the_difference(["a", "b", "c"]) == 0

def test_mixed_types():
    assert double_the_difference([1, "a", 3, 2.5]) == 0

def test_all_zeros():
    assert double_the_difference([0,0,0]) == 0

def test_single_positive_odd():
    assert double_the_difference([5]) == 25

def test_single_negative_odd():
    assert double_the_difference([-5]) == 25

def test_only_negative_numbers_and_positive_odd():
    assert double_the_difference([-1, -3, 5]) == 0

def test_only_positive_even_numbers_and_positive_odd():
    assert double_the_difference([2, 4, 6, 1]) == 0

def test_only_positive_even_numbers_and_negative_odd():
    assert double_the_difference([2, 4, 6, -1]) == 0

def test_only_positive_even_numbers_and_zero():
    assert double_the_difference([2, 4, 6, 0]) == 0

def test_only_positive_even_numbers_and_positive_odd_and_zero():
    assert double_the_difference([2, 4, 6, 1, 0]) == 0

def test_only_positive_even_numbers_and_positive_odd_and_negative_odd():
    assert double_the_difference([2, 4, 6, 1, -1]) == 0

def test_only_positive_even_numbers_and_positive_odd_and_zero_and_negative_odd():
    assert double_the_difference([2, 4, 6, 1, 0, -1]) == 0

def test_only_positive_even_numbers_and_positive_odd_and_zero_and_negative_odd_and_positive_odd():
    assert double_the_difference([2, 4, 6, 1, 0, -1, 3]) == 0

def test_only_positive_even_numbers_and_positive_odd_and_zero_and_negative_odd_and_positive_odd_and_negative_odd():
    assert double_the_difference([2, 4, 6, 1, 0, -1, 3, -5]) == 0

def test_only_positive_even_numbers_and_positive_odd_and_zero_and_negative_odd_and_positive_odd_and_negative_odd_and_positive_odd():
    assert double_the_difference([2, 4, 6, 1, 0, -1, 3, -5, 7]) == 0