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

def test_edge_case_multiple_of_12():
    assert sum_squares([12]) == 12**2

def test_list_with_floats_converted_to_int():
    assert sum_squares([1.0, 2.0, 3.0, 4.0]) == 1 + 2 + 9 + 64

def test_list_with_mixed_types_int_and_float():
    assert sum_squares([1, 2.0, 3, 4.0]) == 1 + 2 + 9 + 64