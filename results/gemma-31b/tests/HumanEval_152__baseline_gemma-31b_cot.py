
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
    # Provided examples
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
    
    # Edge Case: Empty lists
    ([], [], []),
    
    # Edge Case: All correct guesses
    ([10, 20, 30], [10, 20, 30], [0, 0, 0]),
    
    # Edge Case: All incorrect guesses
    ([10, 20, 30], [11, 19, 31], [1, 1, 1]),
    
    # Edge Case: Negative numbers in both arrays
    ([-1, -5, -10], [-1, -2, -15], [0, 3, 5]),
    
    # Edge Case: Mixed positive and negative numbers
    ([5, -5, 0], [-5, 5, 0], [10, 10, 0]),
    
    # Edge Case: Single element lists
    ([100], [100], [0]),
    ([100], [0], [100]),
    ([0], [100], [100]),
    
    # Edge Case: Large values
    ([1000000, -1000000], [0, 0], [1000000, 1000000]),
    
    # Edge Case: Zeros
    ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
])
def test_compare(game, guess, expected):
    """
    Tests the compare function to ensure it correctly calculates the absolute 
    difference between game scores and guesses.
    """
    assert compare(game, guess) == expected

def test_compare_type_consistency():
    """
    Ensure the output is a list and maintains the same length as the input.
    """
    game = [1, 2, 3]
    guess = [4, 5, 6]
    result = compare(game, guess)
    assert isinstance(result, list)
    assert len(result) == len(game)