


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

def test_empty_list():
    assert sum_squares([]) == 0

def test_list_with_one_element():
    assert sum_squares([5]) == 5

def test_list_with_multiple_elements_no_multiples():
    assert sum_squares([1, 2, 4, 5]) == 12

def test_list_with_multiples_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 9 + 4 + 5 + 36

def test_list_with_multiples_of_4():
    assert sum_squares([1, 2, 3, 4, 5, 8]) == 1 + 2 + 3 + 64 + 5 + 512

def test_list_with_multiples_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 8, 9, 12]) == 1 + 2 + 9 + 64 + 5 + 36 + 512 + 81 + 144

def test_list_with_negative_numbers():
    assert sum_squares([-1, -2, -3, -4, -5]) == -1 + -2 + 9 + -64 + -5

def test_list_with_mixed_positive_and_negative_numbers():
    assert sum_squares([-1, 2, -3, 4, -5]) == -1 + 2 + 9 + 64 + -5

def test_list_with_zeros():
    assert sum_squares([0, 0, 0, 0]) == 0

def test_large_list():
    lst = list(range(20))
    expected_sum = sum(lst)
    for i in range(len(lst)):
        if i % 3 == 0:
            expected_sum -= lst[i]
            expected_sum += lst[i]**2
        elif i % 4 == 0:
            expected_sum -= lst[i]
            expected_sum += lst[i]**3
    assert sum_squares(lst) == expected_sum

def test_list_with_duplicate_elements():
    assert sum_squares([1, 1, 1, 1, 1, 1]) == 1 + 1 + 1 + 1 + 1 + 1

def test_list_with_large_numbers():
    assert sum_squares([100, 200, 300, 400]) == 100 + 200 + 90000 + 64000000

def test_list_with_multiple_elements():
    assert sum_squares([1, 2, 3]) == 6

def test_list_with_negative_numbers_2():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_list_with_mixed_positive_and_negative_2():
    assert sum_squares([1, -2, 3, -4, 5, -6]) == 41

def test_index_multiple_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 9 + 4 + 5 + 36

def test_index_multiple_of_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 2 + 3 + 64 + 5 + 6 + 7 + 512

def test_index_multiple_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 9 + 64 + 5 + 6 + 7 + 512 + 81 + 10 + 11 + 144

def test_list_with_floats_converted_to_int():
    assert sum_squares([1.0, 2.0, 3.0]) == 6

def test_list_with_mixed_types():
    with pytest.raises(TypeError):
        sum_squares([1, "a", 3])

def test_long_list():
    lst = list(range(20))
    expected_sum = sum(lst)
    for i in range(len(lst)):
        if i % 3 == 0:
            expected_sum -= lst[i]
            expected_sum += lst[i]**2
        elif i % 4 == 0:
            expected_sum -= lst[i]
            expected_sum += lst[i]**3
    assert sum_squares(lst) == expected_sum

def test_list_with_all_multiples_of_3():
    assert sum_squares([3, 6, 9, 12]) == 9 + 36 + 81 + 144

def test_list_with_all_multiples_of_4():
    assert sum_squares([4, 8, 12, 16]) == 64 + 512 + 144 + 4096