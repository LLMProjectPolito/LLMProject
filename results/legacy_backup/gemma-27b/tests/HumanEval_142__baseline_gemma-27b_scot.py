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
        elif i % 4 == 0:
            new_lst.append(num**3)
        else:
            new_lst.append(num)
    return sum(new_lst)

def test_empty_list():
    assert sum_squares([]) == 0

def test_single_element():
    assert sum_squares([5]) == 5

def test_multiple_of_3():
    assert sum_squares([1, 2, 3]) == 1 + 2 + 9

def test_multiple_of_4():
    assert sum_squares([1, 2, 3, 4]) == 1 + 2 + 9 + 64

def test_multiple_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 9 + 64 + 5 + 36 + 7 + 512 + 81 + 10 + 11 + 144

def test_mixed_list():
    assert sum_squares([-1, -5, 2, -1, -5]) == (-1)**2 + (-5) + (2)**2 + (-1)**3 + (-5) == 1 - 5 + 4 - 1 - 5 == -6

def test_negative_numbers():
    assert sum_squares([-1, -2, -3, -4]) == (-1)**2 + (-2) + (-3)**2 + (-4)**3 == 1 - 2 + 9 - 64 == -56

def test_large_numbers():
    assert sum_squares([1000, 2000, 3000]) == 1000**2 + 2000 + 3000**2 == 1000000 + 2000 + 9000000 == 10002000

def test_all_multiples_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 9 + 4 + 5 + 36 == 57

def test_all_multiples_of_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 2 + 3 + 64 + 5 + 6 + 7 + 512 == 599