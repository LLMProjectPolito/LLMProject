
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
    ([10], [15], [5]),
    ([0], [10], [10]),
    ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
    ([1, 2, 3], [4, 5, 6], [3, 3, 3]),
    ([-1, -2, -3], [-1, -2, -3], [0, 0, 0]),
    ([-1, -2, -3], [1, 2, 3], [2, 4, 6]),
    ([-5, -2], [-2, -5], [3, 3]),
    ([10, -10], [-10, 10], [20, 20]),
    ([100, 200, 300], [50, 250, 350], [50, 50, 50]),
    ([-1, -5, -10], [-1, -2, -15], [0, 3, 5]),
    ([10, 20, 30], [15, 25, 35], [5, 5, 5]),
    ([10, 20, 30], [5, 15, 25], [5, 5, 5]),
])
def test_compare_parametrized(game, guess, expected):
    """Parametrized tests for various scenarios including docstring examples and edge cases."""
    assert compare(game, guess) == expected

def test_compare_floats():
    """Test with float values to ensure absolute difference handles them."""
    assert compare([1.5, 2.5], [1.0, 3.0]) == [0.5, 0.5]

def test_compare_large_numbers():
    """Test with very large integers."""
    assert compare([10**12], [0]) == [10**12]
    assert compare([10**9], [10**9 + 7]) == [7]
    assert compare([0], [10**9]) == [10**9]

def test_compare_large_lists():
    """Test with large lists to ensure performance and correctness."""
    game = list(range(1000))
    guess = [x + 1 for x in range(1000)]
    expected = [1] * 1000
    assert compare(game, guess) == expected