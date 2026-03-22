import pytest
from your_module import compare  # Replace your_module

def test_empty_lists():
    """Checks behavior with empty lists."""
    assert compare([], []) == []

def test_perfect_guesses():
    """Checks when all guesses are correct."""
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_incorrect_guesses():
    """Checks when all guesses are incorrect."""
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_mixed_guesses():
    """Checks a mix of correct and incorrect guesses."""
    assert compare([1, 2, 3, 4, 5], [1, 3, 3, 4, 6]) == [0, 1, 0, 0, 1]
    assert compare([1, 2, 3, 4, 5], [1, 3, 3, 4, 7]) == [0, 1, 0, 0, 2]

def test_single_element_lists():
    """Checks lists with only one element."""
    assert compare([5], [5]) == [0]
    assert compare([5], [6]) == [1]

def test_negative_numbers():
    """Checks lists containing negative numbers."""
    assert compare([-1, -2, -3], [-1, -2, -4]) == [0, 0, 1]
    assert compare([-1, -2, -3], [-1, -1, -4]) == [0, 1, 1]

def test_zero_scores():
    """Checks lists containing zero scores."""
    assert compare([0, 0, 0], [0, 1, 0]) == [0, 1, 0]

def test_large_numbers():
    """Checks lists containing large numbers."""
    assert compare([1000, 2000], [1000, 2500]) == [0, 500]

def test_equal_but_not_correct():
    """Checks when the guess and game are equal but not the correct value."""
    assert compare([2, 2], [2, 2]) == [0, 0]

def test_different_lengths():
    """Checks when the input lists have different lengths."""
    with pytest.raises(ValueError):
        compare([1, 2], [1])