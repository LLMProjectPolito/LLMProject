import pytest

def test_empty_list():
    assert sum_squares([]) == 0

def test_list_with_one_element():
    assert sum_squares([5]) == 5

def test_list_with_multiple_elements():
    assert sum_squares([1, 2, 3]) == 6

def test_list_with_negative_elements():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_list_with_zeros():
    assert sum_squares([0, 0, 0, 0]) == 0

def test_list_with_mixed_positive_and_negative():
    assert sum_squares([1, -2, 3, -4, 5, -6]) == 49

def test_list_with_multiples_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 9 + 4 + 5 + 36

def test_list_with_multiples_of_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 2 + 3 + 64 + 5 + 6 + 7 + 512

def test_list_with_multiples_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 9 + 64 + 5 + 36 + 7 + 512 + 81 + 10 + 11 + 144

def test_large_list():
    lst = list(range(20))
    expected_sum = sum(lst)
    for i in range(len(lst)):
        if i % 3 == 0:
            expected_sum -= lst[i]
            expected_sum += lst[i]**2
        elif i % 4 == 0 and i % 3 != 0:
            expected_sum -= lst[i]
            expected_sum += lst[i]**3
    assert sum_squares(lst) == expected_sum

def test_list_with_floats():
    with pytest.raises(TypeError):
        sum_squares([1.0, 2.0, 3.0])

def test_list_with_strings():
    with pytest.raises(TypeError):
        sum_squares([1, "2", 3])