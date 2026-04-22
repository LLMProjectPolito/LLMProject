
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
    s = s.lower()
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
        if isinstance(num, int) and num >= 0 and num % 2 != 0:
            sum_of_squares += num * num
    return sum_of_squares



def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('Racecar') == True  # Test case-insensitivity
    assert is_palindrome('A man, a plan, a canal: Panama') == False # Test with spaces and punctuation
    assert is_palindrome('121') == True # Test with numbers
    assert is_palindrome('12321') == True # Test with longer numbers
    assert is_palindrome('madam') == True

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_get_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_get_max_single():
    assert get_max([5]) == 5

def test_get_max_all_same():
    assert get_max([7, 7, 7]) == 7

def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

def test_double_the_difference_mixed():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_double_the_difference_negative():
    assert double_the_difference([-1, -2, 0]) == 0

def test_double_the_difference_only_negative():
    assert double_the_difference([-1, -3]) == 0

def test_double_the_difference_only_zero():
    assert double_the_difference([0]) == 0

def test_double_the_difference_only_positive_even():
    assert double_the_difference([2, 4, 6]) == 0

def test_double_the_difference_only_positive_odd():
    assert double_the_difference([1, 3, 5]) == 35

def test_double_the_difference_mixed_types():
    assert double_the_difference([1, "a", 3, 2.5, 5]) == 34

def test_double_the_difference_large_numbers():
    assert double_the_difference([1000000, 1000001, 2000000]) == 2000000000001