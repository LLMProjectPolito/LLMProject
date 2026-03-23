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
            total += num**2
        elif i % 4 == 0 and i % 3 != 0:
            total += num**3
    return total

def test_empty_list():
    assert sum_squares([]) == 0

def test_simple_list():
    assert sum_squares([1, 2, 3]) == 6

def test_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_mixed_positive_negative():
    assert sum_squares([1, -2, 3, -4, 5]) == 1 + 4 + 9 + (-64) + 25 == 1 + 4 + 9 - 64 + 25 == 1 + 4 + 9 - 64 + 25 == -25

def test_multiple_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1**2 + 2**2 + 3**2 + 4**2 + 5**2 + 6**2 == 1 + 4 + 9 + 16 + 25 + 36 == 91

def test_multiple_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1**2 + 2**2 + 3**2 + 4**2 + 5**2 + 6**2 + 7**2 + 8**2 == 1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 == 204

def test_multiple_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1**2 + 2**2 + 3**2 + 4**2 + 5**2 + 6**2 + 7**2 + 8**2 + 9**2 + 10**2 == 1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100 == 385

def test_large_numbers():
    assert sum_squares([100, 200, 300, 400, 500]) == 100**2 + 200**2 + 300**2 + 400**2 + 500**2 == 10000 + 40000 + 90000 + 160000 + 250000 == 550000