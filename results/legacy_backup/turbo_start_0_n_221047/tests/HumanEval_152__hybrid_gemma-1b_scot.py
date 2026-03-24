import pytest
import pandas as pd

def compare(game, guess):
    """
    Compares a guess to a set of scores.

    Args:
        game (list): A list of scores.
        guess (list): A list of guesses.

    Returns:
        list: A list of how far off each guess was.
    """
    results = []
    for i in range(len(game)):
        score = game[i]
        guess = guess[i]
        results.append(abs(score - guess))
    return results

@pytest.mark.parametrize(
    "game, guess, expected",
    [
        ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
        ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
        ([1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]),
        ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
        ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
        ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
        ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
        ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
        ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
    ]
)

def compare(game, guess):
    """
    Compares a guess to a set of scores.

    Args:
        game (list): A list of scores.
        guess (list): A list of guesses.

    Returns:
        list: A list of how far off each guess was.
    """
    results = []
    for i in range(len(game)):
        score = game[i]
        guess = guess[i]
        results.append(abs(score - guess))
    return results

if __name__ == '__main__':
    pytest.main(["-v"])