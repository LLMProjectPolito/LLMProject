import pytest
from your_module import compare  # Replace your_module

def test_empty_arrays():
    assert compare([], []) == []

def test_single_match():
    assert compare([5], [5]) == [0]
    assert compare([5], [3]) == [2]
    assert compare([5], [2]) == [3]

def test_multiple_matches_correct_guesses():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 5, 1]) == [0, 0, 0, 0, 0, 0]

def test_multiple_matches_incorrect_guesses():
    assert compare([1, 2, 3, 4, 5, 1], [2, 1, 4, 3, 6, 0]) == [1, 1, 1, 1, 1, 1]

def test_mixed_correct_and_incorrect_guesses():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

def test_zero_scores():
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]
    assert compare([0, 0, 0], [1, 2, 3]) == [1, 2, 3]
    assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]

def test_negative_scores_and_guesses():
    assert compare([-1, -2, -3], [-2, -1, -4]) == [1, 1, 1]
    assert compare([-1, -2, -3], [-2, -1, -3]) == [1, 1, 0]

def test_large_numbers():
    assert compare([100, 200, 300], [100, 205, 290]) == [0, 5, 10]
    assert compare([1000, 2000, 3000], [1000, 2001, 3000]) == [0, 1, 0]

def test_different_lengths_raises_error():
    with pytest.raises(ValueError):
        compare([1, 2, 3], [1, 2])

def test_non_numeric_input():
    with pytest.raises(TypeError):
        compare([1, 2, 3], ['a', 'b', 'c'])
    with pytest.raises(TypeError):
        compare(['a', 'b', 'c'], [1, 2, 3])

def test_mixed_numeric_and_non_numeric_input():
    with pytest.raises(TypeError):
        compare([1, 2, 3], [1, 'a', 3])

def test_mixed_guesses():
    assert compare([1, 2, 3, 4, 5], [1, 3, 2, 6, 4]) == [0, 1, 1, 2, 1]