import pytest

def test_compare_empty_lists():
    assert compare([], []) == []

def test_compare_correct_guesses():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_compare_incorrect_guesses():
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_compare_mixed_guesses():
    assert compare([1, 2, 3, 4, 5], [1, 2, 4, 4, 5]) == [0, 0, 1, 0, 0]

def test_compare_negative_scores_and_guesses():
    assert compare([-1, -2, -3], [-1, -2, -4]) == [0, 0, 1]

def test_compare_zero_scores_and_guesses():
    assert compare([0, 0, 0], [0, 1, 2]) == [0, 1, 2]

def test_compare_large_numbers():
    assert compare([100, 200, 300], [100, 205, 300]) == [0, 5, 0]

def test_compare_example_1():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

def test_compare_example_2():
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_single_element_lists():
    assert compare([5], [5]) == [0]
    assert compare([5], [6]) == [1]

def test_compare_different_data_types():
    with pytest.raises(TypeError):
        compare([1, 2, 3], [1, 2, "a"])
    with pytest.raises(TypeError):
        compare([1, 2, "a"], [1, 2, 3])
    with pytest.raises(TypeError):
        compare([1, 2, 3], [1, 2, 3.5])
    with pytest.raises(TypeError):
        compare([1, 2, 3.5], [1, 2, 3])