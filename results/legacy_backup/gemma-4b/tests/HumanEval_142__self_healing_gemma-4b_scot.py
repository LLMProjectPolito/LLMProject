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
# The function `sum_squares` takes a list of integers as input and modifies it in place based on the index.
# It squares elements at multiples of 3 and cubes elements at multiples of 4 (but not 3).
# The function returns the sum of the modified elements.
# The function should handle empty lists correctly.
# The function should handle negative numbers correctly.

# STEP 2: PLAN - List test functions names and scenarios.
# test_empty_list
# test_single_element_multiple_of_3
# test_single_element_multiple_of_4
# test_multiple_elements_mix_of_multiples_of_3_and_4
# test_negative_numbers
# test_mixed_positive_and_negative_numbers
# test_large_numbers

# STEP 3: CODE - Write the high-quality pytest suite.
###
def test_empty_list():
    assert sum_squares([]) == 0

def test_single_element_multiple_of_3():
    assert sum_squares([3]) == 9

def test_single_element_multiple_of_4():
    assert sum_squares([4]) == 64

def test_multiple_elements_mix_of_multiples_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1**2 + 2**2 + 3**2 + 4**3 + 5**2 + 6**2  # 1 + 4 + 9 + 64 + 25 + 36 = 139
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1 + 4 + 9 + 64 + 25 + 36 + 49 + 512 + 81 # 1 + 4 + 9 + 64 + 25 + 36 + 49 + 512 + 81 = 791

def test_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -1**2 + (-5)**2 + 2**2 + (-1)**2 + (-5)**2  # 1 + 25 + 4 + 1 + 25 = 56
    assert sum_squares([-4, -3, -2, -1]) == (-4)**3 + (-3)**3 + (-2)**3 + (-1)**3 # -64 -27 -8 -1 = -100

def test_mixed_positive_and_negative_numbers():
    assert sum_squares([1, -2, 3, -4, 5, -6]) == 1**2 + (-2)**2 + 3**2 + (-4)**3 + 5**2 + (-6)**2 # 1 + 4 + 9 + (-64) + 25 + 36 = 31
    assert sum_squares([-1, 2, -3, 4, -5, 6]) == (-1)**2 + 2**2 + (-3)**2 + 4**3 + (-5)**2 + 6**2 # 1 + 4 + 9 + 64 + 25 + 36 = 139

def test_large_numbers():
    assert sum_squares([100, 200, 300]) == 100**2 + 200**2 + 300**2 # 10000 + 40000 + 90000 = 140000
    assert sum_squares([4, 8, 12]) == 4**2 + 8**2 + 12**2 # 16 + 64 + 144 = 224