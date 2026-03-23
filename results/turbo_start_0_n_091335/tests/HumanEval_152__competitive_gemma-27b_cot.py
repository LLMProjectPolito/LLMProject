import pytest

def test_compare_empty_lists():
    assert compare([], []) == []

def test_compare_equal_lists():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_compare_different_lists():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

def test_compare_with_zeros():
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_negative_numbers():
    assert compare([-1, -2, -3], [-1, -2, -4]) == [0, 0, 1]

def test_compare_mixed_positive_negative():
    assert compare([1, -2, 3], [1, -1, 2]) == [0, 1, 1]

def test_compare_large_numbers():
    assert compare([100, 200, 300], [90, 210, 290]) == [10, 10, 10]

def test_compare_single_element():
    assert compare([5], [5]) == [0]

def test_compare_single_element_different():
    assert compare([5], [3]) == [2]

def test_compare_all_incorrect():
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_compare_long_lists():
    game = list(range(10))
    guess = [x + 1 for x in range(10)]
    expected = [1] * 10
    assert compare(game, guess) == expected