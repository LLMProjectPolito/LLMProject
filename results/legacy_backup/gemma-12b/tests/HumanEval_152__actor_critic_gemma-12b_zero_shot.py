import pytest
from your_module import compare  # Replace your_module

def test_compare_correct_guesses():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 5, 1]) == [0, 0, 0, 0, 0, 0]

def test_compare_mixed_guesses():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

def test_compare_all_incorrect_guesses():
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_empty_lists():
    assert compare([], []) == []

def test_compare_single_element_lists_same():
    assert compare([5], [5]) == [0]

def test_compare_single_element_lists_different():
    assert compare([1], [2]) == [1]

def test_compare_lists_with_zero_values_same():
    assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]

def test_compare_lists_with_zero_values_different():
    assert compare([0, 0, 0], [1, 2, 3]) == [1, 2, 3]

def test_compare_negative_scores():
    assert compare([-1, -2, -3], [-1, -2, -4]) == [0, 0, 1]

def test_compare_unequal_length_lists_shorter():
    with pytest.raises(ValueError):
        compare([1, 2], [1])

def test_compare_unequal_length_lists_longer():
    with pytest.raises(ValueError):
        compare([1], [1, 2])

def test_compare_lists_with_duplicate_values_differing():
    assert compare([1, 1, 2], [1, 3, 2]) == [0, 2, 0]

def test_compare_same_values_different_lengths():
    assert compare([1, 1, 1], [1, 1]) == [0, 0, 1]

def test_compare_large_lists():
    large_list_1 = list(range(100))
    large_list_2 = list(range(100))
    assert compare(large_list_1, large_list_2) == [0] * 100

def test_compare_lists_with_mixed_positive_and_negative_numbers():
    assert compare([-1, 2, -3, 4], [-1, 2, -3, 5]) == [0, 0, 0, 1]