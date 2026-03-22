import pytest
from your_module import compare  # Replace your_module

def test_empty_arrays():
    assert compare([], []) == []

def test_single_match():
    assert compare([5], [5]) == [0]
    assert compare([5], [6]) == [1]
    assert compare([6], [5]) == [1]

def test_correct_guesses():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 5, 1]) == [0, 0, 0, 0, 0, 0]

def test_incorrect_guesses():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_mixed_guesses():
    assert compare([1, 5, 3, 7, 2], [1, 4, 3, 8, 2]) == [0, 1, 0, 1, 0]

def test_negative_scores_and_guesses():
    assert compare([-1, -2, -3], [-1, -2, -4]) == [0, 0, 1]
    assert compare([-1, -2, -3], [-2, -1, -3]) == [1, 1, 0]

def test_large_numbers():
    assert compare([1000, 2000, 3000], [1000, 2001, 3000]) == [0, 1, 0]

def test_zero_scores():
    assert compare([0, 0, 0], [1, 2, 3]) == [1, 2, 3]
    assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]

def test_equal_length_arrays():
    with pytest.raises(ValueError):
        compare([1, 2, 3], [1, 2])

    with pytest.raises(ValueError):
        compare([1, 2], [1, 2, 3])

def test_correct_guesses_suite2():
    assert compare([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [0, 0, 0, 0, 0]

def test_incorrect_guesses_suite2():
    assert compare([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]) == [5, 5, 5, 5, 5]

def test_mixed_guesses_suite2():
    assert compare([1, 2, 3, 4, 5], [1, 2, 4, 4, 3]) == [0, 0, 1, 0, 2]

def test_negative_scores_suite2():
    assert compare([-1, -2, -3], [-1, -2, -4]) == [0, 0, 1]

def test_zero_scores_suite2():
    assert compare([0, 0, 0], [0, 1, 2]) == [0, 1, 2]

def test_example_1_suite2():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

def test_example_2_suite2():
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_different_lengths_suite2():
    with pytest.raises(ValueError):
        compare([1, 2], [1])
    with pytest.raises(ValueError):
        compare([1], [1, 2])