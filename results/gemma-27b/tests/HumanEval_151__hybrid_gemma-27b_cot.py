
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

def test_all_negative():
    assert double_the_difference([-1, -3, -5]) == 0

def test_mixed_positive_negative():
    assert double_the_difference([-1, 1, -2, 3]) == 10

def test_all_even():
    assert double_the_difference([2, 4, 6]) == 0

def test_all_odd():
    assert double_the_difference([1, 3, 5]) == 35

def test_mixed_odd_even():
    assert double_the_difference([1, 2, 3, 4, 5]) == 35

def test_zero_in_list():
    assert double_the_difference([0, 1, 2, 3]) == 10

def test_only_zero():
    assert double_the_difference([0]) == 0

def test_floats_in_list():
    assert double_the_difference([1.0, 2.5, 3.0]) == 10

def test_mixed_types():
    assert double_the_difference([1, "a", 3, 2.5, 5]) == 35

def test_large_numbers():
    assert double_the_difference([99, 101]) == 20002

def test_negative_and_zero():
    assert double_the_difference([-1, 0, -2]) == 0

def test_single_odd_number():
    assert double_the_difference([1]) == 1

def test_single_even_number():
    assert double_the_difference([2]) == 0

def test_example_1():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_example_2():
    assert double_the_difference([-1, -2, 0]) == 0

def test_example_3():
    assert double_the_difference([9, -2]) == 81

def test_single_odd():
    assert double_the_difference([1]) == 1

def test_single_even():
    assert double_the_difference([2]) == 0

def test_single_negative():
    assert double_the_difference([-1]) == 0

def test_example_4():
    assert double_the_difference([0]) == 0

def test_list_with_strings_and_floats():
    assert double_the_difference([1, "hello", 2.5, 3, "world"]) == 10

def test_list_with_boolean():
    assert double_the_difference([True, 1, False, 3]) == 10

def test_list_with_none():
    assert double_the_difference([1, None, 3]) == 10