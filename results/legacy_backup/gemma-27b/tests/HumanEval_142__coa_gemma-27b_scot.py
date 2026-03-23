import pytest
import math


# Focus: Index-based Calculations
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
        else:
            total += num
    return total

def test_sum_squares_empty_list():
    assert sum_squares([]) == 0

def test_sum_squares_basic_example():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_mixed_indices():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1 + 2 + 9 + 64 + 5 + 36 + 7 + 512 + 81 + 10

def test_sum_squares_multiple_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 9 + 64 + 5 + 36 + 7 + 512 + 81 + 10 + 11 + 144

# Focus: Empty List/Null Input
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
        else:
            total += num
    return total

def test_sum_squares_empty_list():
    """Test with an empty list."""
    assert sum_squares([]) == 0

def test_sum_squares_null_list():
    """Test with None as input (should handle gracefully)."""
    try:
        sum_squares(None)
    except TypeError:
        assert True  # Expect a TypeError
    except Exception as e:
        assert False, f"Unexpected exception: {e}"

# Focus: Positive/Negative/Zero Integers
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
    for i in range(len(lst)):
        if i % 3 == 0:
            new_lst.append(lst[i]**2)
        elif i % 4 == 0 and i % 3 != 0:
            new_lst.append(lst[i]**3)
        else:
            new_lst.append(lst[i])
    return sum(new_lst)

def test_sum_squares_positive_integers():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1**2 + 2 + 3**2 + 4**3 + 5 + 6**2 + 7 + 8**3 + 9**2 + 10 + 11 + 12**2
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([1, 2, 3, 4]) == 1**2 + 2 + 3**2 + 4**3

def test_sum_squares_negative_integers():
    assert sum_squares([-1, -2, -3, -4, -5, -6]) == (-1)**2 + (-2) + (-3)**2 + (-4)**3 + (-5) + (-6)**2
    assert sum_squares([-1, -5, 2, -1, -5]) == -126
    assert sum_squares([-1, -2, -3]) == 6

def test_sum_squares_zero_integers():
    assert sum_squares([0, 0, 0, 0]) == 0
    assert sum_squares([0, 1, 0, 2]) == 1 + 8
    assert sum_squares([0, -1, 0, -2]) == 1 + 8