import pytest

def test_empty_list():
    assert sum_squares([]) == 0

def test_example_1():
    assert sum_squares([1, 2, 3]) == 6

def test_example_2():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_list_with_only_multiples_of_3():
    assert sum_squares([3, 6, 9]) == 3**2 + 6**2 + 9**2

def test_list_with_only_multiples_of_4():
    assert sum_squares([4, 8, 12]) == 4**3 + 8**3 + 12**3

def test_list_with_multiples_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 3**2 + 4**3 + 5 + 6**2 + 7 + 8**3 + 9**2 + 10 + 11 + 12**3

def test_list_with_negative_numbers():
    assert sum_squares([-1, -2, -3, -4]) == -1 + -2 + (-3)**2 + (-4)**3

def test_list_with_zeros():
    assert sum_squares([0, 0, 0, 0]) == 0

def test_list_with_mixed_positive_and_negative():
    assert sum_squares([1, -2, 3, -4, 5, -6]) == 1 + (-2) + 3**2 + (-4)**3 + 5 + (-6)**2

def test_large_list():
    lst = list(range(20))
    expected_sum = sum(x**2 if i % 3 == 0 else x**3 if i % 4 == 0 and i % 3 != 0 else x for i, x in enumerate(lst))
    assert sum_squares(lst) == expected_sum

def test_list_with_single_element_multiple_of_3():
    assert sum_squares([3]) == 3**2

def test_list_with_single_element_multiple_of_4():
    assert sum_squares([4]) == 4**3

def test_list_with_single_element_not_multiple_of_3_or_4():
    assert sum_squares([5]) == 5

def test_list_with_decimal_numbers():
    with pytest.raises(TypeError):
        sum_squares([1.5, 2, 3])