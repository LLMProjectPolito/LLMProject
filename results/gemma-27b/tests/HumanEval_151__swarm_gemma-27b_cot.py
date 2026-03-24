
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

def test_empty_list():
    assert double_the_difference([]) == 0

def test_all_even():
    assert double_the_difference([2, 4, 6]) == 0

def test_all_negative():
    assert double_the_difference([-1, -3, -5]) == 0

def test_mixed_types():
    assert double_the_difference([1, 3.5, 2, "a"]) == 1

def test_negative_and_positive():
    assert double_the_difference([-1, 1, -2, 3]) == 1 + 9

def test_zero_and_odd():
    assert double_the_difference([0, 1, 0, 3]) == 1 + 9

def test_large_odd_number():
    assert double_the_difference([1001]) == 1001**2

def test_large_list():
    assert double_the_difference(list(range(1, 100, 2))) == sum([x**2 for x in range(1, 100, 2)])

def test_float_odd():
    assert double_the_difference([1.0, 3.0]) == 1 + 9

def test_edge_case_max_int():
    assert double_the_difference([2**31 - 1]) == (2**31 - 1)**2

def test_list_with_zero():
    assert double_the_difference([0, 1, 2, 3]) == 1 + 9

def test_list_with_mixed_positive_negative_and_non_integers():
    assert double_the_difference([-1, 2.5, 3, -4, 5.0, 7]) == 1 + 9 + 49

def test_list_with_large_and_small_numbers():
    assert double_the_difference([1, 2**31 - 1, -2**31, 3]) == 1 + (2**31 - 1)**2 + 9

def test_list_with_float_and_int():
    assert double_the_difference([1, 2.0, 3]) == 1 + 9

def test_list_with_string():
    assert double_the_difference([1, "a", 3]) == 1 + 9

def test_list_with_none():
    assert double_the_difference([1, None, 3]) == 1 + 9

def test_list_with_boolean():
    assert double_the_difference([1, True, 3]) == 1 + 1 + 9

def test_list_with_complex():
    assert double_the_difference([1, 1+1j, 3]) == 1 + 9

def test_list_with_only_non_integers():
    assert double_the_difference([1.5, 2.7, 3.1]) == 0

def test_list_with_min_int():
    assert double_the_difference([-2**31]) == 0