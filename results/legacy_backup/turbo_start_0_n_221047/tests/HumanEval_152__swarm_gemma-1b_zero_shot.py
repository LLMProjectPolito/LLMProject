import pytest
import math

def compare(game, guess):
    result = []
    for i in range(len(game)):
        if game[i] == guess:
            result.append(0)
        else:
            result.append(abs(guess - game[i]))
    return result

def test_compare_valid_guess():
    game = [1, 2, 3, 4, 5]
    guess = 3
    assert compare(game, guess) == [0, 0, 0, 0, 0]

def test_compare_invalid_guess():
    game = [1, 2, 3, 4, 5]
    guess = 6
    assert compare(game, guess) == [0, 0, 0, 0, 0]

def test_compare_empty_game():
    game = []
    guess = 3
    assert compare(game, guess) == []

def test_compare_single_element_game():
    game = [5]
    guess = 5
    assert compare(game, guess) == [0]