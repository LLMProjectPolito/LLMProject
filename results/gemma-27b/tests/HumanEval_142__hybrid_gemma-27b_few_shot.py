


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
    new_lst = []
    for i, num in enumerate(lst):
        if i % 3 == 0:
            new_lst.append(num**2)
        elif i % 4 == 0 and i % 3 != 0:
            new_lst.append(num**3)
        else:
            new_lst.append(num)
    return sum(new_lst)

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_basic1():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_basic2():
    assert sum_squares([1, 2, 3, 4]) == 18

def test_sum_squares_basic3():
    assert sum_squares([1, 2, 3, 4, 5]) == 39

def test_sum_squares_negative():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_mixed():
    assert sum_squares([1, -2, 3, -4, 5, -6]) == 68

def test_sum_squares_long_list():
    assert sum_squares([i for i in range(10)]) == 285

def test_sum_squares_all_multiples_of_3():
    assert sum_squares([3, 6, 9, 12]) == 288

def test_sum_squares_all_multiples_of_4():
    assert sum_squares([4, 8, 12, 16]) == 1008

def test_sum_squares_zeroes():
    assert sum_squares([0, 0, 0, 0]) == 0

def test_sum_squares_large_numbers():
    assert sum_squares([100, 200, 300, 400]) == 1000000

def test_sum_squares_complex_case():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1010

def test_sum_squares_basic2_suite2():
    assert sum_squares([1, 2, 3, 4]) == 1 + 2 + 9 + 64

def test_sum_squares_mixed_suite2():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 9 + 64 + 5 + 36 + 7 + 512 + 81 + 100 + 11 + 144

def test_sum_squares_zeros_suite2():
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_sum_squares_large_numbers_suite2():
    assert sum_squares([100, 200, 300, 400]) == 10000 + 200 + 90000 + 64000000

def test_sum_squares_single_element_suite2():
    assert sum_squares([5]) == 5

def test_sum_squares_multiple_of_3_and_4_suite2():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 9 + 64 + 5 + 36 + 7 + 512 + 81 + 100 + 11 + 144

def test_sum_squares_long_list_suite2():
    lst = list(range(20))
    expected_sum = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            expected_sum += num**2
        elif i % 4 == 0 and i % 3 != 0:
            expected_sum += num**3
        else:
            expected_sum += num
    assert sum_squares(lst) == expected_sum

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None