import pytest

def compare(game, guess):
    results = []
    for i in range(len(game)):
        if game[i] == guess:
            results.append(0)
        else:
            results.append(abs(guess - game[i]))
    return results

def test_compare_correct_guess():
    assert compare([1, 2, 3, 4, 5, 1], 1) == [0, 0, 0, 0, 3, 3]

def test_compare_incorrect_guess():
    assert compare([0, 5, 0, 0, 0, 4], 4) == [4, 4, 1, 0, 0, 6]

def test_compare_empty_arrays():
    assert compare([], []) == []

def test_compare_single_element_arrays():
    assert compare([1], 1) == [0]