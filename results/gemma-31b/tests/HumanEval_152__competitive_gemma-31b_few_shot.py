
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
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
    ([], [], []),
    ([10], [10], [0]),
    ([10], [5], [5]),
    ([5], [10], [5]),
    ([-1, -2, -3], [-1, -5, 0], [0, 3, 3]),
    ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
    ([100, 200], [300, 400], [200, 200]),
    ([1000000], [0], [1000000]),
])
def test_compare(game, guess, expected):
    assert compare(game, guess) == expected

def test_compare_different_lengths():
    # Depending on implementation, this might raise an IndexError or return a partial list.
    # Given the prompt says "equal length", we test the behavior if they aren't.
    # If the function uses zip(), it will truncate to the shortest.
    # If it uses range(len(game)), it might crash.
    # Since the prompt specifies equal length, we primarily focus on valid inputs,
    # but we can check for basic stability.
    with pytest.raises(Exception):
        # This is a safety check; if the function doesn't handle it, 
        # it's expected to fail based on the "equal length" constraint.
        # However, usually, we only test the defined contract.
        pass