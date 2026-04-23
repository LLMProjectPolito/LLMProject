
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
    
    sum_of_squares = 0
    for num in lst:
        if isinstance(num, int) and num > 0 and num % 2 != 0:
            sum_of_squares += num * num
    return sum_of_squares


def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


# Pytest tests for double_the_difference
def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

def test_double_the_difference_positive_odd():
    assert double_the_difference([1, 3, 5]) == 35

def test_double_the_difference_mixed_positive_negative():
    assert double_the_difference([1, -2, 3, -4]) == 10  # 1 + 9 = 10

def test_double_the_difference_all_negative():
    assert double_the_difference([-1, -3, -5]) == 0

def test_double_the_difference_all_even():
    assert double_the_difference([2, 4, 6]) == 0

def test_double_the_difference_zero():
    assert double_the_difference([0, 1, 3]) == 10

def test_double_the_difference_with_zero():
    assert double_the_difference([1, 0, 3]) == 10

def test_double_the_difference_with_negative_zero():
    assert double_the_difference([-1, 0, 1]) == 2

def test_double_the_difference_with_non_integer():
    assert double_the_difference([1, 2.5, 3]) == 9
    
def test_double_the_difference_with_string():
    assert double_the_difference([1, "a", 3]) == 9

def test_double_the_difference_with_mixed_types():
    assert double_the_difference([1, 2, "3", 4]) == 10

def test_double_the_difference_large_numbers():
    assert double_the_difference([1000000, 2000001, 3000002]) == 1000000000000000000

# Pytest tests for is_palindrome
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True

def test_palindrome_with_spaces():
    assert is_palindrome('race car') == True

def test_palindrome_with_punctuation():
    assert is_palindrome('A man, a plan, a canal: Panama') == True

def test_palindrome_with_mixed_case():
    assert is_palindrome('Racecar') == True

def test_palindrome_with_numbers():
    assert is_palindrome('121') == True

def test_palindrome_with_non_alphanumeric():
    assert is_palindrome('.,!@#$%^&*()') == False


# Pytest tests for get_max
def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_max_single_element():
    assert get_max([5]) == 5

def test_max_negative_numbers():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed_positive_negative():
    assert get_max([-1, 2, -3, 4]) == 4