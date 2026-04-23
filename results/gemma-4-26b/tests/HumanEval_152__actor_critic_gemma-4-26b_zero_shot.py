
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

def compare(game, guess):
    """
    Determines how far off each guess was from the actual scores.
    Returns an array of absolute differences.
    """
    return [abs(g - gu) for g, gu in zip(game, guess)]

@pytest.mark.parametrize("game, guess, expected", [
    # Provided examples
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
    
    # Edge Case: Empty lists
    ([], [], []),
    
    # Edge Case: Single element
    ([10], [10], [0]),
    ([10], [7], [3]),
    
    # Edge Case: All zeros
    ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
    
    # Edge Case: Negative numbers
    ([-5, -10, 5], [-2, -15, -5], [3, 5, 10]),
    
    # Edge Case: Large numbers
    ([1000000], [0], [1000000]),
    ([500, 500], [1000, 0], [500, 500]),
])
def test_compare(game, guess, expected):
    """Tests the compare function with various scenarios including examples, 
    empty inputs, single elements, negatives, and large values."""
    assert compare(game, guess) == expected