import pytest
from your_module import sum_squares  # Replace your_module

def test_empty_list():
    assert sum_squares([]) == 0

def test_basic_list():
    assert sum_squares([1, 2, 3]) == 14

def test_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -1 - 25 + 4 - 1 - 25 == -48

def test_mixed_positive_negative():
    assert sum_squares([1, -2, 3, -4, 5, -6]) == 1 - 4 + 9 - 16 + 25 - 36 == -21

def test_multiples_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 4 + 9 + 16 + 25 + 36 == 91

def test_multiples_of_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 == 204

def test_multiples_of_both():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 12]) == 1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 144 == 429

def test_large_numbers():
    assert sum_squares([10, 20, 30, 40]) == 100 + 400 + 900 + 1600 == 2000

def test_zeroes():
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_single_element_multiple_of_3():
    assert sum_squares([3]) == 9

def test_single_element_multiple_of_4():
    assert sum_squares([4]) == 16

def test_single_element_neither():
    assert sum_squares([5]) == 25

def test_list_with_floats_raises_typeerror():
    with pytest.raises(TypeError):
        sum_squares([1.0, 2.0, 3.0])

def test_list_with_strings_raises_typeerror():
    with pytest.raises(TypeError):
        sum_squares(["a", "b", "c"])

def test_list_with_multiples_of_3_suite2():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 4 + 9 + 16 + 25 + 36 == 91

def test_list_with_multiples_of_4_suite2():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8]) == 1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 == 204

def test_list_with_multiples_of_both_3_and_4_suite2():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 + 81 + 100 + 121 + 144 == 646

def test_list_with_negative_numbers_suite2():
    assert sum_squares([-1, -5, 2, -1, -5]) == -1 - 25 + 4 - 1 - 25 == -48

def test_list_with_mixed_positive_and_negative_suite2():
    assert sum_squares([-1, 2, -3, 4, -5, 6]) == -1 + 4 - 9 + 16 - 25 + 36 == 21

def test_list_with_zeros_suite2():
    assert sum_squares([0, 1, 2, 3, 4, 5]) == 0 + 1 + 4 + 9 + 16 + 25 == 55

def test_large_list_suite2():
    large_list = list(range(1, 21))
    expected_sum = 0
    for i, num in enumerate(large_list):
        expected_sum += num**2
    assert sum_squares(large_list) == expected_sum

def test_list_with_duplicates_suite2():
    assert sum_squares([1, 1, 1, 1, 1, 1]) == 1 + 1 + 1 + 1 + 1 + 1 == 6

def test_list_with_only_multiples_of_3_suite2():
    assert sum_squares([3, 6, 9, 12]) == 9 + 36 + 81 + 144 == 270

def test_list_with_only_multiples_of_4_suite2():
    assert sum_squares([4, 8, 12, 16]) == 16 + 64 + 144 + 256 == 480

def test_list_with_large_numbers_suite2():
    assert sum_squares([100, 200, 300, 400]) == 10000 + 40000 + 90000 + 160000 == 290000