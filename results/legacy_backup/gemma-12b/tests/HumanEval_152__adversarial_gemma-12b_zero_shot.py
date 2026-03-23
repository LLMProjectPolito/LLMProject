import pytest
from your_module import compare  # Replace your_module

def test_empty_arrays():
    assert compare([], []) == []

def test_single_element_arrays():
    assert compare([1], [1]) == [0]
    assert compare([1], [2]) == [1]

def test_correct_guesses():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_incorrect_guesses():
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_mixed_guesses():
    assert compare([1, 2, 3, 4], [1, 5, 3, 2]) == [0, 3, 0, 2]

def test_zero_scores():
    assert compare([0, 0, 0], [1, 2, 3]) == [1, 2, 3]

def test_negative_scores():
    assert compare([-1, -2, -3], [-1, -2, -4]) == [0, 0, 1]

def test_negative_guesses():
    assert compare([1, 2, 3], [-1, -2, -3]) == [2, 4, 6]

def test_mixed_positive_negative():
    assert compare([1, -2, 3], [1, -1, 4]) == [0, 1, 1]

def test_example_1():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

def test_example_2():
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_large_numbers():
    assert compare([100, 200, 300], [105, 195, 305]) == [5, 5, 5]

def test_equal_length():
    with pytest.raises(ValueError):
        compare([1, 2], [1])

def test_different_types():
    with pytest.raises(TypeError):
        compare([1, 2], ["a", "b"])