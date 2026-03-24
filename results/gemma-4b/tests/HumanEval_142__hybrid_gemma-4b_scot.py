


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
# The function `sum_squares` calculates a sum based on the elements of a list, applying different transformations based on the index.
# The transformations are:
#   - If the index is a multiple of 3, the element is squared.
#   - If the index is a multiple of 4 and not a multiple of 3, the element is cubed.
#   - Otherwise, the element remains unchanged.
# The function returns the sum of the transformed elements.
# We need to test various scenarios including empty lists, lists with single elements, lists with multiple elements, and cases where indices are multiples of 3, 4, or both.

# STEP 2: PLAN - List test functions names and scenarios.
# test_empty_list
# test_single_element_multiple_of_3
# test_single_element_multiple_of_4
# test_multiple_elements_no_multiples
# test_multiple_elements_multiple_of_3
# test_multiple_elements_multiple_of_4
# test_multiple_elements_multiple_of_3_and_4
# test_negative_numbers
# test_mixed_positive_and_negative

# STEP 3: CODE - Write the high-quality pytest suite.
def test_empty_list():
    assert sum_squares([]) == 0

def test_single_element_multiple_of_3():
    assert sum_squares([3]) == 9

def test_single_element_multiple_of_4():
    assert sum_squares([4]) == 64

def test_multiple_elements_no_multiples():
    assert sum_squares([1, 2, 3]) == 6

def test_multiple_elements_multiple_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 4 + 9 + 64 + 25 + 36

def test_multiple_elements_multiple_of_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 8 + 27 + 64 + 125 + 216 + 343 + 512

def test_multiple_elements_multiple_of_3_and_4():
    assert sum_squares([3, 4, 6, 8, 9, 12]) == 9 + 64 + 36 + 512 + 81 + 1296

def test_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -1 + (-5)**3 + 2**2 + (-1)**3 + (-5)**3

def test_mixed_positive_and_negative():
    assert sum_squares([1, -2, 3, -4, 5, -6]) == 1 + (-2)**3 + 3**2 + (-4)**3 + 5**2 + (-6)**3