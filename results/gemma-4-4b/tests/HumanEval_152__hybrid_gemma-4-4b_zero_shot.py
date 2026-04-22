
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
from typing import List


def compare(game: List[int], guess: List[int]) -> List[int]:
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
    if len(game) != len(guess):
        raise ValueError("Game and guess lists must have the same length.")
    
    results = []
    for i in range(len(game)):
        results.append(abs(game[i] - guess[i]))
    return results


@pytest.mark.parametrize(
    "game, guess, expected",
    [
        ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
        ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
        ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]),
        ([5, 4, 3, 2, 1], [5, 4, 3, 2, 1], [0, 0, 0, 0, 0]),
        ([1, 2, 3], [4, 5, 6], [3, 3, 3]),
        ([1, 2, 3], [1, 2, 3], [0, 0, 0]),
        ([1, 2, 3], [3, 2, 1], [2, 2, 2]),
        ([0], [0], [0]),
        ([1], [2], [1]),
        ([2], [1], [1]),
        ([], [], []),
        ([1, 2], [1, 2], [0, 0]),
        ([1, 2], [2, 1], [1, 1]),
    ],
)
def test_compare_basic(game, guess, expected):
    assert compare(game, guess) == expected


@pytest.mark.parametrize(
    "game, guess, expected",
    [
        ([10, 20, 30, 40, 50], [15, 25, 35, 45, 55], [5, 5, 5, 5, 5]),
        ([100, 200, 300], [100, 200, 300], [0, 0, 0]),
        ([1, 100, 1000], [1, 100, 1000], [0, 0, 0]),
    ],
)
def test_compare_larger_numbers(game, guess, expected):
    assert compare(game, guess) == expected


@pytest.mark.parametrize(
    "game, guess, expected",
    [
        ([-1, -2, -3], [-1, -2, -3], [0, 0, 0]),
        ([-1, 2, -3], [1, 2, -3], [2, 0, 0]),
        ([-1, 2, -3], [1, 2, 3], [2, 0, 0]),
    ],
)
def test_compare_negative_numbers(game, guess, expected):
    assert compare(game, guess) == expected

@pytest.mark.parametrize(
    "game, guess, expected",
    [
        ([1,2,3,4,5], [5,4,3,2,1], [4,4,4,4,4])
    ]
)
def test_compare_reverse_order(game, guess, expected):
    assert compare(game, guess) == expected

@pytest.mark.parametrize(
    "game, guess",
    [
        ([1, 2], [1]],  # Unequal lengths
    ),
)
def test_compare_unequal_lengths(game, guess):
    with pytest.raises(ValueError):
        compare(game, guess)