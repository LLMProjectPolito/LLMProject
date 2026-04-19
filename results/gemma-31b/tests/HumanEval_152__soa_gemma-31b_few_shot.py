
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
    ([10], [20], [10]),
    ([10], [0], [10]),
    ([-1, -5, -10], [-1, -2, -15], [0, 3, 5]),
    ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
    ([100, 200, 300], [400, 500, 600], [300, 300, 300]),
    ([1.5, 2.5], [1.0, 3.0], [0.5, 0.5]),
])
def test_compare(game, guess, expected):
    assert compare(game, guess) == expected

def test_compare_different_lengths():
    """
    Depending on implementation, this might raise an error or 
    behave unexpectedly. Based on the prompt 'equal length', 
    we assume valid input, but we can test for consistency.
    """
    with pytest.raises(Exception):
        # This test assumes the function might fail or we are checking 
        # behavior for mismatched lengths if the implementation doesn't handle it.
        # If the function uses zip(), it might just truncate.
        # Given the prompt, we focus on the logic of absolute difference.
        pass