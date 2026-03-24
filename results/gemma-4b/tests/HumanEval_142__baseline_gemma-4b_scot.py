


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

### STEP 1: REASONING
# The function `sum_squares` calculates a sum based on the index of each element in a list.
# The index plays a crucial role in determining whether an element is squared or cubed.
# We need to test various scenarios including empty lists, lists with single elements, lists with multiple elements, and lists with different index multiples of 3 and 4.
# We should cover edge cases like an empty list and lists with negative numbers.

### STEP 2: PLAN
# Test cases:
# 1. Empty list: []
# 2. List with single element: [5]
# 3. List with multiple elements and index 3 is a multiple of 3: [1, 2, 3]
# 4. List with multiple elements and index 4 is a multiple of 4 and not 3: [1, 2, 3, 4]
# 5. List with multiple elements and index 6 is a multiple of 3: [1, 2, 3, 4, 5, 6]
# 6. List with multiple elements and index 8 is a multiple of 4 and not 3: [1, 2, 3, 4, 5, 6, 7, 8]
# 7. List with negative numbers: [-1, -5, 2, -1, -5]
# 8. List with mixed positive and negative numbers: [1, -2, 3, -4, 5]

### STEP 3: CODE
def test_empty_list():
    assert sum_squares([]) == 0

def test_single_element_list():
    assert sum_squares([5]) == 25

def test_multiple_elements_index_3_multiple():
    assert sum_squares([1, 2, 3]) == 6

def test_multiple_elements_index_4_multiple_not_3():
    assert sum_squares([1, 2, 3, 4]) == 64

def test_multiple_elements_index_6_multiple():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 91

def test_multiple_elements_index_8_multiple_not_3():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 182

def test_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_mixed_positive_negative():
    assert sum_squares([1, -2, 3, -4, 5]) == 35