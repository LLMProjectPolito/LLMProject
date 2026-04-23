
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
    total = 0
    for num in lst:
        if isinstance(num, int) and num > 0 and num % 2 != 0:
            total += num * num
    return total

test_cases = [
    (0, 0),
    (1, 1),
    (1, 3, 5),
    (1, 2, 3, 4, 5, 35),
    (-1, -2, -3, 0),
    (0, 0, 0, 0),
    (-1, -2, 0, 1, 3, 10),
    (1.5, 2, 3, 9),
    (1, 2.5, 3, "a", 9),
    (1, 1, 3, 3, 5, 45),
    (100, 200, 300, 140000),
    (-2, -4, -6, 0),
    (-1, 0, 1, 1),
]

def test_double_the_difference():
    for lst, expected in test_cases:
        assert double_the_difference(lst) == expected