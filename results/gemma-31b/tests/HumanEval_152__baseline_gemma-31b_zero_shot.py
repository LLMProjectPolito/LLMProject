
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
    # Edge case: Empty lists
    ([], [], []),
    # Edge case: Single element - correct
    ([10], [10], [0]),
    # Edge case: Single element - incorrect
    ([10], [5], [5]),
    # Edge case: Single element - negative difference
    ([10], [15], [5]),
    # All correct guesses
    ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
    # All incorrect guesses
    ([1, 2, 3], [4, 5, 6], [3, 3, 3]),
    # Negative numbers in game and guess
    ([-1, -5, -10], [-1, -2, -15], [0, 3, 5]),
    # Large numbers
    ([1000000, 0], [0, 1000000], [1000000, 1000000]),
    # Mixed zeros and negatives
    ([0, 0, 0], [-1, 1, 0], [1, 1, 0]),
])
def test_compare(game, guess, expected):
    """Test the compare function with various scenarios including edge cases."""
    assert compare(game, guess) == expected

def test_compare_maintains_length():
    """Ensure the output array is always the same length as the input arrays."""
    game = [1, 2, 3]
    guess = [4, 5, 6]
    result = compare(game, guess)
    assert len(result) == len(game) == len(guess)