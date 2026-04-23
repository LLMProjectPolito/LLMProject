
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
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]

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


# --- Tests for is_palindrome ---
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True
    assert is_palindrome('b') == True

def test_palindrome_mixed_case():
    assert is_palindrome('Madam') == True

def test_palindrome_with_spaces():
    assert is_palindrome('  race car  ') == True

def test_palindrome_with_punctuation():
    assert is_palindrome('.,;?!') == True

def test_palindrome_with_non_alphanumeric():
    assert is_palindrome('121') == True
    assert is_palindrome('12321') == True

# --- Tests for get_max ---
def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) is None

def test_max_single_element():
    assert get_max([5]) == 5

def test_max_negative():
    assert get_max([-1, -2, -3]) is None

def test_max_mixed():
    assert get_max([-1, 0, 1]) == 1

def test_max_duplicate():
    assert get_max([1, 1, 1]) == 1

# --- Tests for double_the_difference ---
def test_double_the_difference_basic():
    assert double_the_difference([1, 3, 2, 0]) == 10

def test_double_the_difference_negative():
    assert double_the_difference([-1, -2, 0]) == 0

def test_double_the_difference_negative_and_positive():
    assert double_the_difference([9, -2]) == 81

def test_double_the_difference_zero():
    assert double_the_difference([0]) == 0

def test_double_the_difference_empty():
    assert double_the_difference([]) == 0

def test_double_the_difference_mixed_types():
    assert double_the_difference([1, "a", 2, 0]) == 5

def test_double_the_difference_all_negative():
    assert double_the_difference([-1, -2, -3]) == 0

def test_double_the_difference_all_positive():
    assert double_the_difference([1, 2, 3]) == 14

def test_double_the_difference_large_numbers():
    assert double_the_difference([100, 200, 300]) == 100000