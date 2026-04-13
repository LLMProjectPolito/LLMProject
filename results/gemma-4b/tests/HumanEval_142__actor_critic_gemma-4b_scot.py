


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
            total += num**2
        elif i % 4 == 0 and i % 3 != 0:
            total += num**3
    return total

### SCoT Steps:

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `sum_squares` takes a list of integers as input and calculates a sum based on the index of each element.
# If the index is a multiple of 3, the element is squared. If the index is a multiple of 4 but not 3, the element is cubed.
# Otherwise, the element remains unchanged. The function returns the final sum.
# Edge cases: empty list, list with only one element, list with multiples of 3 and 4, list with only multiples of 3, list with only multiples of 4.

# STEP 2: PLAN - List test functions names and scenarios.
# test_empty_list
# test_single_element_list
# test_multiple_of_3
# test_multiple_of_4_not_3
# test_multiple_of_3_and_4
# test_negative_numbers
# test_mixed_positive_negative
# test_large_numbers

# STEP 3: CODE - Write the high-quality pytest suite.
def test_empty_list():
    assert sum_squares([]) == 0

def test_single_element_list():
    assert sum_squares([5]) == 25

def test_multiple_of_3():
    assert sum_squares([1, 2, 3]) == 6

def test_multiple_of_4_not_3():
    assert sum_squares([4, 2, 4]) == 64

def test_multiple_of_3_and_4():
    assert sum_squares([3, 4, 3]) == 3**2 + 4**3

def test_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_mixed_positive_negative():
    assert sum_squares([1, -2, 3, -4, 5]) == 1**2 + (-2)**3 + 3**2 + (-4)**3 + 5**2

def test_large_numbers():
    assert sum_squares([100, 200, 300]) == 100**2 + 200**3 + 300**2

def test_list_with_zeros():
    assert sum_squares([0, 1, 2, 3]) == 0 + 1**2 + 2**3 + 3**2

def test_list_with_only_multiples_of_3():
    assert sum_squares([3, 6, 9, 12]) == 3**2 + 6**2 + 9**2 + 12**2

def test_list_with_only_multiples_of_4():
    assert sum_squares([4, 8, 12, 16]) == 4**3 + 8**3 + 12**3 + 16**3