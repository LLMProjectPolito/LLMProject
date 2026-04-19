
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

@pytest.mark.parametrize("game, guess, expected", [
    # Examples from docstring
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
    # Edge cases: Empty and Single element
    ([], [], []),
    ([10], [10], [0]),
    ([10], [5], [5]),
    ([10], [-5], [15]),
    # Functional cases
    ([10, 20, 30], [10, 20, 30], [0, 0, 0]),
    ([1, 2, 3], [4, 5, 6], [3, 3, 3]),
    ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
    # Negative values
    ([-1, -5, -10], [-1, -2, -15], [0, 3, 5]),
    ([-5, -10], [-10, -5], [5, 5]),
    ([-1, -2], [1, 2], [2, 4]),
    ([10, -10], [-10, 10], [20, 20]),
    # Large numbers and Floats
    ([1000000, -1000000], [2000000, 1000000], [1000000, 2000000]),
    ([0.5, 1.5], [1.0, 1.0], [0.5, 0.5]),
    ([1.5, 2.5], [1.0, 3.0], [0.5, 0.5]),
])
def test_compare(game, guess, expected):
    assert compare(game, guess) == expected

def test_compare_length_consistency():
    """Ensure the output length always matches the input length."""
    game = [1, 2, 3, 4, 5]
    guess = [6, 7, 8, 9, 10]
    result = compare(game, guess)
    assert len(result) == len(game)
    assert len(result) == len(guess)