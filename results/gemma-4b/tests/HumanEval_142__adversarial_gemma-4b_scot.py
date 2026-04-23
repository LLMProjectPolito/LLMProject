


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
# The function `sum_squares` calculates a sum based on the elements of a list, modifying them based on their index.
# The modification rules are:
#   - If the index is a multiple of 3, the element is squared.
#   - If the index is a multiple of 4 and not a multiple of 3, the element is cubed.
#   - Otherwise, the element remains unchanged.
# The function returns the sum of the modified (or unchanged) elements.
# We need to test various scenarios including empty lists, lists with single elements, lists with multiple elements, and cases where indices are multiples of 3, 4, or both.

# STEP 2: PLAN - List test functions names and scenarios.
# test_empty_list: Test with an empty list.
# test_single_element_multiple_of_3: Test with a single element that is a multiple of 3.
# test_single_element_multiple_of_4: Test with a single element that is a multiple of 4 but not 3.
# test_single_element_neither: Test with a single element that is neither a multiple of 3 nor 4.
# test_multiple_elements_mix: Test with a list containing a mix of elements that satisfy the conditions.
# test_negative_numbers: Test with a list containing negative numbers.
# test_zero: Test with a list containing zero.

# STEP 3: CODE - Write the high-quality pytest suite.
### CODE
def test_empty_list():
    assert sum_squares([]) == 0

def test_single_element_multiple_of_3():
    assert sum_squares([3]) == 9

def test_single_element_multiple_of_4():
    assert sum_squares([4]) == 64

def test_single_element_neither():
    assert sum_squares([5]) == 5

def test_multiple_elements_mix():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1**2 + 2**2 + 3**2 + 4**3 + 5**2 + 6**2  # 1 + 4 + 9 + 64 + 25 + 36 = 149
    assert sum_squares([-1,-5,2,-1,-5]) == -1**2 + (-5)**2 + 2**2 + (-1)**2 + (-5)**2 # 1 + 25 + 4 + 1 + 25 = 56

def test_negative_numbers():
    assert sum_squares([-1, -2, -3, -4, -5]) == (-1)**2 + (-2)**2 + (-3)**2 + (-4)**3 + (-5)**2 # 1 + 4 + 9 + -64 + 25 = -25

def test_zero():
    assert sum_squares([0, 1, 2, 3, 4]) == 0 + 1 + 4 + 9 + 64 # 78