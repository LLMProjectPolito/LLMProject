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
    for i in range(len(lst)):
        if i % 3 == 0 and i % 4 != 0:
            total += lst[i] ** 2
        elif i % 3 != 0 and i % 4 == 0:
            total += lst[i] ** 3
    return total

def test_sum_squares_positive():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([1, 2, 3, 4]) == 16
    assert sum_squares([-1, -5, 2, -1, -5]) == -126
    assert sum_squares([]) == 0
    
def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -3

def test_get_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4