
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

# The function is assumed to be defined as:
# def compare(game, guess):
#     return [abs(g - gu) for g, gu in zip(game, guess)]

@pytest.mark.parametrize("game, guess, expected", [
    # Provided examples
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
    
    # Edge Case: Empty lists
    ([], [], []),
    
    # Edge Case: Single element lists
    ([10], [10], [0]),
    ([10], [20], [10]),
    ([10], [0], [10]),
    
    # Edge Case: All correct guesses
    ([1, 2, 3], [1, 2, 3], [0, 0, 0]),
    
    # Edge Case: All incorrect guesses
    ([1, 2, 3], [4, 5, 6], [3, 3, 3]),
    
    # Edge Case: Negative numbers
    ([-1, -2, -3], [-1, -4, -1], [0, 2, 2]),
    ([-5, 5], [5, -5], [10, 10]),
    
    # Edge Case: Large numbers
    ([1000000, 0], [2000000, -1000000], [1000000, 1000000]),
    
    # Edge Case: Zeroes
    ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
    ([0, 0, 0], [1, -1, 0], [1, 1, 0]),
])
def test_compare_scenarios(game, guess, expected):
    """Test various integer scenarios including basic functionality and edge cases."""
    assert compare(game, guess) == expected

def test_compare_floats():
    """Verify that the function handles floating point numbers correctly."""
    game = [1.5, 2.7, 3.0]
    guess = [1.0, 3.2, 3.0]
    expected = [0.5, 0.5, 0.0]
    # Use pytest.approx to handle floating point precision issues
    assert compare(game, guess) == pytest.approx(expected)

def test_compare_mismatched_lengths():
    """
    Verify behavior when input lists have different lengths.
    Since the implementation uses zip(), it should truncate to the shortest list.
    """
    # Game longer than guess
    assert compare([1, 2, 3], [1, 2]) == [0, 0]
    # Guess longer than game
    assert compare([1, 2], [1, 2, 3]) == [0, 0]
    # One list empty
    assert compare([1, 2, 3], []) == []
    assert compare([], [1, 2, 3]) == []