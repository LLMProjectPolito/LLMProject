
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
    Determines how far off each guess was from the actual game score.
    Returns an array of absolute differences.
    """
    return [abs(g - gu) for g, gu in zip(game, guess)]

@pytest.mark.parametrize("game, guess, expected", [
    # Provided examples
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
    
    # Edge Case: Empty lists
    ([], [], []),
    
    # Edge Case: Single element lists
    ([10], [10], [0]),
    ([10], [5], [5]),
    ([5], [10], [5]),
    
    # Edge Case: All guesses correct
    ([1, 2, 3], [1, 2, 3], [0, 0, 0]),
    
    # Edge Case: All guesses incorrect
    ([1, 1, 1], [2, 2, 2], [1, 1, 1]),
    
    # Edge Case: Negative numbers in both lists
    ([-1, -5, -10], [-1, -2, -15], [0, 3, 5]),
    
    # Edge Case: Mixed positive and negative numbers
    ([-10, 10], [10, -10], [20, 20]),
    
    # Edge Case: Large numbers
    ([1000000, 0], [2000000, -1000000], [1000000, 1000000]),
    
    # Edge Case: Zeroes
    ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
])
def test_compare(game, guess, expected):
    assert compare(game, guess) == expected

def test_compare_different_lengths():
    """
    The problem states arrays are of equal length, but it's good to 
    verify behavior if they aren't (zip stops at the shortest).
    """
    game = [1, 2, 3]
    guess = [1, 2]
    # zip will truncate to the shortest list
    assert compare(game, guess) == [0, 0]