
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
    assert double_the_difference([-1, -2, -3]) == 0

def test_mixed_positive_negative():
    assert double_the_difference([-1, 1, -2, 3]) == 10

def test_all_even():
    assert double_the_difference([2, 4, 6]) == 0

def test_all_odd():
    assert double_the_difference([1, 3, 5]) == 35

def test_zero_in_list():
    assert double_the_difference([0, 1, 2, 3]) == 10

def test_only_zero():
    assert double_the_difference([0]) == 0

def test_floats_in_list():
    assert double_the_difference([1.0, 2.5, 3.0]) == 10

def test_negative_floats_in_list():
    assert double_the_difference([-1.0, -2.5, -3.0]) == 0

def test_type_error():
    with pytest.raises(TypeError):
        double_the_difference([1, "a", 3])

def test_large_numbers_significant_difference():
    assert double_the_difference([99, 101]) == 20002

def test_single_odd_number():
    assert double_the_difference([1]) == 1

def test_single_even_number():
    assert double_the_difference([2]) == 0

def test_negative_and_zero():
    assert double_the_difference([-1, 0]) == 0

def test_large_difference():
    assert double_the_difference([1, 100]) == 20002

def test_single_negative_odd_number():
    assert double_the_difference([-1]) == 0

def test_floats_with_non_zero_result():
    assert double_the_difference([1.5, 2.5, 3.5]) == 0

def test_large_list():
    assert double_the_difference([1, 2, 3, 4, 5, -1, -2, 0, 7, 9]) == 1 + 9 + 25 + 49 + 81