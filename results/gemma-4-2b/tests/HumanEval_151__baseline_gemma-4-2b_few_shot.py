
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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

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
        if isinstance(num, int) and num > 0:
            sum_of_squares += num * num
    return sum_of_squares

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('') == True

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([5, 1, 9, 2]) == 9

def test_get_max_empty():
    assert get_max([]) is None

def test_double_the_difference_basic():
    assert double_the_difference([1, 3, 2, 0]) == 10
    assert double_the_difference([-1, -2, 0]) == 0
    assert double_the_difference([9, -2]) == 81
    assert double_the_difference([0]) == 0

def test_double_the_difference_mixed():
    assert double_the_difference([1, 3, 5, 7]) == 1 + 9 + 25 + 49 == 84
    assert double_the_difference([2, 4, 6]) == 0
    assert double_the_difference([1, 2, 3, 4, 5]) == 1 + 9 + 25 + 49 == 84

def test_double_the_difference_negative():
    assert double_the_difference([-1, -3, -5]) == 0

def test_double_the_difference_zero():
    assert double_the_difference([0, 0, 0]) == 0

def test_double_the_difference_mixed_positive_negative():
    assert double_the_difference([1, -2, 3, -4, 5]) == 1 + 9 + 25 == 35

def test_double_the_difference_non_integer():
    assert double_the_difference([1.5, 2, 3]) == 0