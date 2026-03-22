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
    sum_of_squares = 0
    for num in lst:
        if isinstance(num, int) and num >= 0 and num % 2 != 0:
            sum_of_squares += num * num
    return sum_of_squares

def test_empty_list():
    assert double_the_difference([]) == 0

def test_negative_numbers():
    assert double_the_difference([-1, -2, 0]) == 0

def test_mixed_numbers():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_single_odd_number():
    assert double_the_difference([9]) == 81

def test_large_odd_numbers():
    assert double_the_difference([123456789]) == 123456789 * 123456789

def test_mixed_edge_case():
    assert double_the_difference([1, 3.14, -5, 7, 1001, -2, 999999999]) == 1 + 49 + 1002001000000000001