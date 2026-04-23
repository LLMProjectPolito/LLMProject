


def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """

import pytest

def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    total = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            total += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            total += num ** 3
        else:
            total += num
    return total


def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_no_modifications():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 4 + 27 + 16 + 125 + 36 == 219

def test_sum_squares_multiple_modifications():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 4 + 27 + 16 + 125 + 36 == 219

def test_sum_squares_mixed_modifications():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 4 + 27 + 16 + 125 + 36 == 219

def test_sum_squares_negative_numbers():
    assert sum_squares([-1, -2, -3, -4, -5, -6]) == 1 + 4 + -27 + 16 + -125 + 36 == -105

def test_sum_squares_mixed_positive_negative():
    assert sum_squares([-1, 2, -3, 4, -5, 6]) == 1 + 4 + -27 + 16 + -125 + 36 == -105

def test_sum_squares_all_same():
    assert sum_squares([5, 5, 5, 5, 5]) == 25 + 25 + 125 + 125 + 125 == 325

def test_sum_squares_zero_values():
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_sum_squares_more_complex():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 135

def test_sum_squares_all_negative_and_mod_4_not_3():
    assert sum_squares([-1, -5, -2, -1, -5]) == -126

def test_sum_squares_all_positive_and_mod_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 117

def test_sum_squares_large_numbers():
    assert sum_squares([1000, 2000, 3000, 4000, 5000]) == 1000000 + 8000000 + 27000000 + 160000000 + 312500000 == 570000000

### Problem:
def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """

### Tests (Pytest):
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True

def test_palindrome_with_spaces():
    assert is_palindrome('race car') == False

def test_palindrome_with_punctuation():
    assert is_palindrome('A man, a plan, a canal: Panama') == False