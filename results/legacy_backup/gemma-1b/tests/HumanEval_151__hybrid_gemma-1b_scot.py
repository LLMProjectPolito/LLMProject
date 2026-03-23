import pytest
from typing import List

def double_the_difference(lst: List[int]) -> int:
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

def double_the_difference(lst: List[int]) -> int:
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