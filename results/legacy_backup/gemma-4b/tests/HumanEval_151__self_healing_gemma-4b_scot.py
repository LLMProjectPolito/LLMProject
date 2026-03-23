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
        if isinstance(num, int) and num % 2 != 0:
            total += num * num
    return total

def test_empty_list():
    assert double_the_difference([]) == 0

def test_positive_odd_integers():
    assert double_the_difference([1, 3, 5]) == 35

def test_negative_odd_integers():
    assert double_the_difference([-1, -3, -5]) == 35

def test_mixed_positive_negative_odd_integers():
    assert double_the_difference([1, -3, 5, -7]) == 85

def test_list_with_zero():
    assert double_the_difference([0]) == 0

def test_list_with_non_integer_values():
    assert double_the_difference([1.5, 3, "a"]) == 0

def test_list_with_only_negative_numbers():
    assert double_the_difference([-1, -2, -3]) == 0

def test_list_with_single_odd_number():
    assert double_the_difference([1]) == 1

def test_list_with_single_even_number():
    assert double_the_difference([2]) == 0

def test_list_with_single_zero():
    assert double_the_difference([0]) == 0

def test_example_1():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_example_2():
    assert double_the_difference([-1, -2, 0]) == 0

def test_example_3():
    assert double_the_difference([9, -2]) == 81