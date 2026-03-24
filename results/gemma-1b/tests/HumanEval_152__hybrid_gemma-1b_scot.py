
def compare(game,guess):
    """I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    
    
    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """

import pytest
import pandas as pd

def compare(game, guess):
    """
    Compares a guess to a set of scores in a game.

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
    ],
)
def test_compare_simple(game, guess, expected):
    assert compare(game, guess) == expected

@pytest.mark.parametrize(
    "game, guess, expected",
    [
        ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
        ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
        ([1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]),
    ],
)
def test_compare_with_errors(game, guess, expected):
    assert compare(game, guess) == expected

@pytest.mark.parametrize(
    "game, guess, expected",
    [
        ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
        ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
        ([1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]),
    ],
)
def test_compare_with_zero_score(game, guess, expected):
    assert compare(game, guess) == expected