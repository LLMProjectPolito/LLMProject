
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
    
    For example:
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0
    double_the_difference([1, 2, 3]) == 0
    double_the_difference([1, 2, 3, 5]) == 0
    double_the_difference([1, 2, 3, 5, 7]) == 0
    double_the_difference([1, 2, 3, 5, 7, 9]) == 0
    double_the_difference([1, 2, 3, 5, 7, 9, 11]) == 0
    double_the_difference([1, 2, 3, 5, 7, 9, 11, 13]) == 0
    double_the_difference([1, 2, 3, 5, 7, 9, 11, 13, 15]) == 0
    double_the_difference([1, 2, 3, 5, 7, 9, 11, 13, 15, 17]) == 0
    double_the_difference([1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 0
    double_the_difference([1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == 0
    double_the_difference([1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]) == 0
    double_the_difference([1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 0
    double_the_difference([1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]) == 0
    """
    if not lst:
        return 0
    
    result = 0
    for num in lst:
        if isinstance(num, int) and num % 2 != 0:
            result += num
    return result