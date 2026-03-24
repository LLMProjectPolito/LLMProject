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
        elif i % 4 == 0 and i % 3 != 0:
            new_lst.append(num**3)
        else:
            new_lst.append(num)
    return sum(new_lst)

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `sum_squares` modifies a list based on the index of each element.
# Elements at indices that are multiples of 3 are squared.
# Elements at indices that are multiples of 4 but not 3 are cubed.
# Other elements remain unchanged.
# The function returns the sum of the modified list.
# We need to test various scenarios, including empty lists, single-element lists,
# lists with multiples of 3 and 4, and lists with mixed positive and negative numbers.
# Edge cases include lists containing only multiples of 3 and 4, and larger lists
# to check for performance.

# STEP 2: PLAN - List test functions names and scenarios.
# 1. test_empty_list: Test with an empty list.
# 2. test_single_element_index_multiple_of_3: Test with a single element at index 0 (multiple of 3).
# 3. test_single_element_index_multiple_of_4_not_3: Test with a single element at index 4 (multiple of 4, not 3).
# 4. test_single_element_index_not_multiple_of_3_or_4: Test with a single element at index 1 (not multiple of 3 or 4).
# 5. test_example_1: Test the example [1, 2, 3].
# 6. test_example_2: Test the example [-1, -5, 2, -1, -5].
# 7. test_multiples_of_3: Test a list with only multiples of 3.
# 8. test_multiples_of_4_not_3: Test a list with only multiples of 4 (but not 3).
# 9. test_multiples_of_both_3_and_4: Test a list with only multiples of both 3 and 4.
# 10. test_large_list: Test with a large list to check performance.
# 11. test_mixed_positive_negative_indices_multiple_of_3: Test a list with mixed positive and negative numbers, focusing on indices that are multiples of 3.
# 12. test_mixed_positive_negative_indices_multiple_of_4_not_3: Test a list with mixed positive and negative numbers, focusing on indices that are multiples of 4 (but not 3).
# 13. test_mixed_positive_negative_indices_other: Test a list with mixed positive and negative numbers, focusing on indices that are not multiples of 3 or 4.

# STEP 3: CODE - Write the high-quality pytest suite.

def test_empty_list():
    assert sum_squares([]) == 0

def test_single_element_index_multiple_of_3():
    assert sum_squares([5]) == 25

def test_single_element_index_multiple_of_4_not_3():
    assert sum_squares([5]) == 125

def test_single_element_index_not_multiple_of_3_or_4():
    assert sum_squares([5]) == 5

def test_example_1():
    assert sum_squares([1, 2, 3]) == 1 + 4 + 9

def test_example_2():
    assert sum_squares([-1, -5, 2, -1, -5]) == 1 + 125 + 4 + 1 + 125

def test_multiples_of_3():
    assert sum_squares([3, 6, 9]) == 9 + 36 + 81

def test_multiples_of_4_not_3():
    assert sum_squares([4, 8, 12]) == 64 + 512 + 1728

def test_multiples_of_both_3_and_4():
    assert sum_squares([12, 24, 36]) == 144 + 13824 + 1296

def test_large_list():
    large_list = list(range(100))
    result = sum_squares(large_list)
    assert type(result) == int

def test_mixed_positive_negative_indices_multiple_of_3():
    assert sum_squares([1, 2, -3, 4, 5, -6]) == 1 + 4 + 9 + 16 + 25 + 36

def test_mixed_positive_negative_indices_multiple_of_4_not_3():
    assert sum_squares([1, -2, 3, -4, 5, -6]) == 1 + 8 + 9 + (-64) + 25 + 36

def test_mixed_positive_negative_indices_other():
    assert sum_squares([1, -2, 3, -4, 5, -6]) == 1 + (-2) + 9 + (-4) + 25 + (-6)