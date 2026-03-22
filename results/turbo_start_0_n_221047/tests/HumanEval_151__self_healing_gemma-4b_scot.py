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

def test_empty_list():
    assert double_the_difference([]) == 0

def test_only_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_only_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 0

def test_mixed_positive_and_negative():
    assert double_the_difference([1, -2, 3, -4]) == 1 + 9 == 10

def test_with_zero():
    assert double_the_difference([0, 1, 2]) == 1

def test_single_element():
    assert double_the_difference([5]) == 25

def test_multiple_odd_numbers():
    assert double_the_difference([1, 3, 5, 7]) == 1 + 9 + 25 + 49 == 84

def test_mixed_odd_and_even():
    assert double_the_difference([1, 2, 3, 4, 5]) == 1 + 9 + 25 == 35

def test_non_integer_values():
    assert double_the_difference([1, 2.5, 3]) == 1

def test_negative_and_non_integer_values():
    assert double_the_difference([-1, 2.5, -3]) == 0