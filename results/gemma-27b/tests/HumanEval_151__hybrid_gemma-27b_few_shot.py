
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
    
    total = 0
    for num in lst:
        if isinstance(num, int) and num >= 0 and num % 2 != 0:
            total += num * num
    return total

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


def test_empty_list():
    assert double_the_difference([]) == 0

def test_basic_example():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_negative_numbers():
    assert double_the_difference([-1, -2, 0]) == 0

def test_mixed_positive_and_negative():
    assert double_the_difference([9, -2]) == 81

def test_zero_only():
    assert double_the_difference([0]) == 0

def test_only_odd_numbers():
    assert double_the_difference([1, 3, 5]) == 35

def test_only_even_numbers():
    assert double_the_difference([2, 4, 6]) == 0

def test_float_numbers():
    assert double_the_difference([1.0, 2.5, 3]) == 9

def test_string_numbers():
    assert double_the_difference(['1', '2', '3']) == 0

def test_mixed_types():
    assert double_the_difference([1, '2', 3.0, -4, 5]) == 26

def test_large_numbers():
    assert double_the_difference([101, 203, 305]) == 10201 + 41209 + 93025

def test_single_odd_number():
    assert double_the_difference([7]) == 49

def test_single_even_number():
    assert double_the_difference([4]) == 0

def test_multiple_zeros_and_odds():
    assert double_the_difference([0, 1, 0, 3, 0, 5]) == 35

def test_all_odd_positive():
    assert double_the_difference([1, 3, 5]) == 35

def test_all_even_positive():
    assert double_the_difference([2, 4, 6]) == 0

def test_floats_and_integers():
    assert double_the_difference([1, 2.5, 3, 4.0, 5]) == 35

def test_strings_and_integers():
    assert double_the_difference([1, "a", 3, "b", 5]) == 35

def test_large_numbers():
    assert double_the_difference([101, 203, 305]) == 101**2 + 203**2 + 305**2

def test_mixed_types_and_values():
    assert double_the_difference([1, -2, 3.0, "hello", 5, 0, -7]) == 26

def test_only_one_odd_number():
    assert double_the_difference([2, 4, 6, 1, 8]) == 1

def test_multiple_zeros_and_odd():
    assert double_the_difference([0, 0, 1, 0, 3]) == 10

def test_large_list():
    large_list = list(range(100))
    expected_sum = sum(x*x for x in large_list if x % 2 != 0)
    assert double_the_difference(large_list) == expected_sum

# Palindrome tests
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

# Get Max tests
def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None