import pytest

@pytest.mark.parametrize("input_list, expected_result", [
    ([1, 3, 5, 0], False),
    ([1, 3, -2, 1], False),
    ([1, 2, 3, 7], False),
    ([2, 4, -5, 3, 5, 7], True),
    ([1], False),
    ([-1, 1], True),
    ([0, 0, 0], False),
    ([10, -10, 5], True),
    ([0, 0], False),
    ([1, -1, 2, -2], True),
    ([-5, 0, 5], True),
    ([10, -10, 20], True),
])
def test_pairs_sum_to_zero(input_list, expected_result):
    assert pairs_sum_to_zero(input_list) == expected_result

def test_pairs_sum_to_zero_empty_list():
    assert pairs_sum_to_zero([]) == False

def test_pairs_sum_to_zero_single_element_list():
    assert pairs_sum_to_zero([5]) == False

def test_pairs_sum_to_zero_list_with_duplicates():
    assert pairs_sum_to_zero([1, 1, 1, 1]) == False

def test_pairs_sum_to_zero_list_with_negative_numbers():
    assert pairs_sum_to_zero([-1, -2, -3]) == False

def test_pairs_sum_to_zero_large_list():
    large_list = [i for i in range(-100, 100)]
    assert pairs_sum_to_zero(large_list) == True

def test_pairs_sum_to_zero_duplicate_elements():
    assert pairs_sum_to_zero([1, 1, -1, -1]) == True

def test_pairs_sum_to_zero_all_zeros():
    assert pairs_sum_to_zero([0, 0, 0, 0]) == False