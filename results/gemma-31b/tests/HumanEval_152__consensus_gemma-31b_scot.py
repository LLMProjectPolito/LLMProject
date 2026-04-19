
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
    ([10, 20, 30], [10, 20, 30], [0, 0, 0]),
    ([1, 1, 1], [2, 2, 2], [1, 1, 1]),
    ([1, 1, 1], [2, 3, 4], [1, 2, 3]),
    ([-1, -5], [-2, -3], [1, 2]),
    ([-5, -10], [-10, -5], [5, 5]),
    ([10, -10], [-10, 10], [20, 20]),
    ([10], [10], [0]),
    ([10], [5], [5]),
    ([0], [10], [10]),
    ([1000000], [2000000], [1000000]),
    ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
    ([1, -1, 2], [-1, 1, -2], [2, 2, 4]),
    ([5, 10], [15, 0], [10, 10]),
    ([100, 200, 300], [101, 199, 300], [1, 1, 0]),
    ([-1, -5, -10], [-1, -2, -15], [0, 3, 5]),
    ([100, 200, 300], [-100, -200, -300], [200, 400, 600]),
    ([1, 2], [3, 4], [2, 2]),
    ([5, 5, 5], [4, 6, 5], [1, 1, 0]),
])
def test_compare_valid_inputs(game, guess, expected):
    """Test the compare function with various valid inputs including edge cases."""
    assert compare(game, guess) == expected

def test_compare_large_numbers():
    """Test the compare function with very large integers."""
    game = [10**12, -10**12]
    guess = [10**12 + 50, -10**12 - 50]
    expected = [50, 50]
    assert compare(game, guess) == expected

def test_compare_floats():
    """Test the compare function with floating point numbers."""
    assert compare([1.5, 2.0], [1.0, 3.5]) == [0.5, 1.5]