import pytest

def test_compare_empty_lists():
    assert compare([], []) == []

def test_compare_single_element_correct():
        assert compare([5], [5]) == [0]

def test_compare_single_element_incorrect():
    assert compare([5], [6]) == [1]

def test_compare_positive_numbers_correct():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_compare_positive_numbers_incorrect():
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_compare_mixed_numbers_correct():
    assert compare([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [0, 0, 0, 0, 0]

def test_compare_mixed_numbers_incorrect():
    assert compare([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]) == [5, 5, 5, 5, 5]

def test_compare_example_1():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

def test_compare_example_2():
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_with_zeros():
    assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]

def test_compare_with_negative_numbers():
    assert compare([-1, -2, -3], [-1, -2, -3]) == [0, 0, 0]

def test_compare_with_mixed_negative_and_positive():
    assert compare([-1, 2, -3], [-1, 3, -2]) == [0, 1, 1]

def test_compare_large_numbers():
    assert compare([100, 200, 300], [100, 201, 300]) == [0, 1, 0]

def test_compare_different_lengths():
    with pytest.raises(ValueError):
        compare([1, 2], [1])