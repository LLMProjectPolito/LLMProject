def compare(game, guess):
    """Compares game scores with guesses and returns the difference."""

    if not isinstance(game, list) or not isinstance(guess, list):
        raise TypeError("Game and guess must be lists.")

    if len(game) != len(guess):
        raise ValueError("Game and guess arrays must have the same length.")

    if not game:  # Handle empty input
        return []

    differences = []
    for i in range(len(game)):
        try:
            diff = abs(game[i] - guess[i])
            differences.append(diff)
        except TypeError:
            # Handle non-numeric types gracefully.  Could also return an error value.
            differences.append(float('inf'))  # Or some other indicator of error

    return differences


import pytest

def test_compare_basic():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_empty():
    assert compare([], []) == []

def test_compare_all_zeros():
    assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]

def test_compare_different_lengths():
    with pytest.raises(ValueError):
        compare([1, 2], [1])

def test_compare_type_error():
    with pytest.raises(TypeError):
        compare([1, 2], "hello")

def test_compare_mixed_types():
    assert compare([1, 2, "a"], [1, 2, 3]) == [0, 0, float('inf')]

def test_compare_large_numbers():
    assert compare([1000000, 2000000], [1000000, 2000001]) == [0, 1]