import pytest

def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    """
    if not lst:
        return 0
    
    result = 0
    for num in lst:
        if isinstance(num, int) and num % 2 != 0:
            result += num * num
    return result

def test_double_the_difference_positive_numbers():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0
    
def test_empty_list():
    assert double_the_difference([]) == 0
    
def test_mixed_positive_and_negative():
    assert double_the_difference([-1, 2, -3, 4]) == 25
    
def test_all_zeros():
    assert double_the_difference([0, 0, 0]) == 0
    
def test_single_odd_number():
    assert double_the_difference([1]) == 1
    
def test_single_even_number():
    assert double_the_difference([2]) == 4
    
def test_single_negative_number():
    assert double_the_difference([-1]) == 1
    
def test_large_numbers():
    assert double_the_difference([1000, 2000, 3000]) == 10000000