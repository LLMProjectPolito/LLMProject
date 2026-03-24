
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
    
    result = 0
    for num in lst:
        if isinstance(num, int) and num % 2 != 0:
            result += num * num
    return result

def test_empty_list():
    assert pytest.approx(double_the_difference([])) == 0

def test_positive_numbers():
    assert pytest.approx(double_the_difference([1, 3, 2, 0])) == 10
    assert pytest.approx(double_the_difference([9, -2])) == 81
    assert pytest.approx(double_the_difference([1, 3, 5])) == 0
    assert pytest.approx(double_the_difference([2, 4, 6])) == 0
    assert pytest.approx(double_the_difference([1, 3, 5, 7])) == 0

def test_negative_numbers():
    assert pytest.approx(double_the_difference([-1, -3, -2, -0])) == 0
    assert pytest.approx(double_the_difference([-1, -3, 2, 4])) == 1
    assert pytest.approx(double_the_difference([-1, -3, -5, -7])) == 0

def test_mixed_numbers():
    assert pytest.approx(double_the_difference([1, -3, 2, -0])) == 1
    assert pytest.approx(double_the_difference([9, -2, 5, 1])) == 25
    assert pytest.approx(double_the_difference([0, 1, 3, 5])) == 0

def test_single_element():
    assert pytest.approx(double_the_difference([5])) == 25
    assert pytest.approx(double_the_difference([0])) == 0
    assert pytest.approx(double_the_difference([-5])) == 25