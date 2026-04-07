
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
        if isinstance(num, int) and num >= 0 and num % 2 != 0:
            sum_of_squares += num * num
    return sum_of_squares

def test_empty_list():
    assert double_the_difference([]) == 0

def test_positive_odd_numbers():
    assert double_the_difference([1, 3, 5]) == 1 + 9 + 25

def test_positive_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_mixed_positive_numbers():
    assert double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0

def test_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 0

def test_mixed_positive_and_negative():
    assert double_the_difference([1, -2, 3, -4]) == 1 + 9

def test_zero():
    assert double_the_difference([0]) == 0

def test_mixed_with_zero():
    assert double_the_difference([1, 0, 3, 0]) == 1 + 9

def test_floats():
    assert double_the_difference([1.0, 2.0, 3.0]) == 0

def test_mixed_types():
    assert double_the_difference([1, "a", 3, 2.5]) == 1 + 9

def test_large_numbers():
    assert double_the_difference([9, 11]) == 81 + 121

def test_single_odd_number():
    assert double_the_difference([5]) == 25

def test_single_even_number():
    assert double_the_difference([4]) == 0

def test_all_negative():
    assert double_the_difference([-1, -3, -5]) == 0

def test_example_1():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_example_2():
    assert double_the_difference([-1, -2, 0]) == 0

def test_example_3():
    assert double_the_difference([9, -2]) == 81

def test_example_4():
    assert double_the_difference([0]) == 0