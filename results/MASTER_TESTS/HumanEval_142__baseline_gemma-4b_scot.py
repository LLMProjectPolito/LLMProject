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
# The function `sum_squares` calculates a sum based on the index of each element in the input list.
# The logic involves squaring elements at multiples of 3 and cubing elements at multiples of 4 (but not 3).
# The function should handle empty lists and lists with negative numbers correctly.
# We need to test various scenarios including empty lists, lists with positive and negative numbers, and lists with indices that are multiples of 3 and 4.

### STEP 2: PLAN
# Test cases:
# 1. Empty list: []
# 2. List with positive numbers and multiples of 3 and 4: [1, 2, 3]
# 3. List with negative numbers and multiples of 3 and 4: [-1, -5, 2, -1, -5]
# 4. List with only multiples of 3: [3, 6, 9]
# 5. List with only multiples of 4: [4, 8, 12]
# 6. List with mixed multiples of 3 and 4: [1, 4, 9, 16]
# 7. List with a single element: [5]
# 8. List with a single negative element: [-5]

### STEP 3: CODE
def test_empty_list():
    assert sum_squares([]) == 0

def test_positive_numbers():
    assert sum_squares([1, 2, 3]) == 6

def test_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_multiples_of_3():
    assert sum_squares([3, 6, 9]) == 99

def test_multiples_of_4():
    assert sum_squares([4, 8, 12]) == 364

def test_mixed_multiples():
    assert sum_squares([1, 4, 9, 16]) == 1 + 64 + 81 + 256

def test_single_element_positive():
    assert sum_squares([5]) == 25

def test_single_element_negative():
    assert sum_squares([-5]) == -125

def test_mixed_positive_negative():
    assert sum_squares([1, -4, 9, -16]) == 1 + (-64) + 81 + (-256)