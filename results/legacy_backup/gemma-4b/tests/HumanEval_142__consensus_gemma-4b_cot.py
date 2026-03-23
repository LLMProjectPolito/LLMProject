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
    assert sum_squares([1, -2, 3, -4, 5]) == 1 + 4 + 9 + (-64) + 25 == 1 + 4 + 9 - 64 + 25 == -25

def test_multiple_multiples_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1**2 + 2**2 + 3**2 + 4**3 + 5**2 + 6**2 + 7**2 + 8**3 + 9**2 == 1 + 4 + 9 + 64 + 25 + 36 + 49 + 512 + 81 == 781

def test_large_numbers():
    assert sum_squares([10, 20, 30, 40, 50]) == 10**2 + 20**2 + 30**2 + 40**3 + 50**2 == 100 + 400 + 900 + 64000 + 2500 == 70000

def test_list_with_zero():
    assert sum_squares([0, 1, 2, 3]) == 0 + 1**2 + 2**2 + 3**2 == 0 + 1 + 4 + 9 == 14

def test_list_with_duplicate_values():
    assert sum_squares([1, 1, 1, 1]) == 1**2 + 1**2 + 1**2 + 1**2 == 4