import pytest
from your_module import compare  # Replace your_module

def test_empty_arrays():
    assert compare([], []) == []

def test_single_element_arrays():
    assert compare([1], [1]) == [0]
    assert compare([1], [2]) == [1]

def test_basic_correct_guesses():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_basic_incorrect_guesses():
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_mixed_correct_and_incorrect_guesses():
    assert compare([1, 2, 3, 4], [1, 5, 3, 2]) == [0, 3, 0, 2]

def test_example_1():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

def test_example_2():
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_negative_scores_and_guesses():
    assert compare([-1, -2, -3], [-1, -2, -4]) == [0, 0, 1]

def test_zero_scores_and_guesses():
    assert compare([0, 0, 0], [0, 1, 2]) == [0, 1, 2]

def test_large_numbers():
    assert compare([1000, 2000, 3000], [1000, 2001, 3000]) == [0, 1, 0]

def test_different_lengths_raises_error():
    with pytest.raises(ValueError):
        compare([1, 2], [1])

def test_non_numeric_input():
    with pytest.raises(TypeError):
        compare([1, 2], ['a', 'b'])
    with pytest.raises(TypeError):
        compare([1, 2], [1, 'a'])
    with pytest.raises(TypeError):
        compare(['a', 'b'], [1, 2])