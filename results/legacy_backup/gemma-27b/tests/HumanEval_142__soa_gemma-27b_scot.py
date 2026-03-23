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

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `sum_squares` takes a list of integers and modifies it based on the index of each element.
# Elements at indices that are multiples of 3 are squared.
# Elements at indices that are multiples of 4 but not 3 are cubed.
# Other elements remain unchanged.
# The function returns the sum of the modified list.
# Edge cases: empty list, list with negative numbers, list with mixed positive and negative numbers.

# STEP 2: PLAN - List test functions names and scenarios.
# test_empty_list: Test with an empty list.
# test_example_1: Test with the example list [1, 2, 3].
# test_example_2: Test with the example list [-1, -5, 2, -1, -5].
# test_multiples_of_3: Test with a list where all indices are multiples of 3.
# test_multiples_of_4: Test with a list where all indices are multiples of 4.
# test_mixed_indices: Test with a list containing a mix of indices that are multiples of 3, 4, and neither.
# test_negative_numbers: Test with a list containing only negative numbers.
# test_large_numbers: Test with a list containing large numbers.
# test_zeroes: Test with a list containing zeroes.
# test_single_element: Test with a list containing a single element.

# STEP 3: CODE - Write the high-quality pytest suite.
def test_empty_list():
    assert sum_squares([]) == 0

def test_example_1():
    assert sum_squares([1, 2, 3]) == 6

def test_example_2():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_multiples_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 9 + 4 + 5 + 36

def test_multiples_of_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 2 + 3 + 64 + 5 + 6 + 7 + 512

def test_mixed_indices():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 9 + 64 + 5 + 36 + 7 + 512 + 81 + 10 + 11 + 144

def test_negative_numbers():
    assert sum_squares([-1, -2, -3, -4]) == 1 + -2 + 9 + -64

def test_large_numbers():
    assert sum_squares([100, 200, 300, 400]) == 10000 + 200 + 90000 + 64000000

def test_zeroes():
    assert sum_squares([0, 0, 0, 0]) == 0

def test_single_element():
    assert sum_squares([5]) == 5

def test_single_element_multiple_of_3():
    assert sum_squares([5, 2, 3]) == 25 + 2 + 9

def test_single_element_multiple_of_4():
    assert sum_squares([5, 2, 3, 4]) == 25 + 2 + 9 + 64