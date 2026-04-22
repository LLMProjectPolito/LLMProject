
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

def test_compare_provided_examples():
    """Tests the examples provided in the problem description."""
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_all_matches():
    """Tests when all guesses are exactly correct."""
    assert compare([10, 20, 30], [10, 20, 30]) == [0, 0, 0]
    assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]

def test_compare_no_matches():
    """Tests when no guesses match the scores."""
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_compare_negative_numbers():
    """Tests handling of negative numbers in both game scores and guesses."""
    # |(-5) - (-2)| = 3
    # |(-10) - 10| = 20
    # |5 - (-5)| = 10
    assert compare([-5, -10, 5], [-2, 10, -5]) == [3, 20, 10]

def test_compare_empty_lists():
    """Tests the edge case of empty input lists."""
    assert compare([], []) == []

def test_compare_single_element():
    """Tests lists containing only one element."""
    assert compare([100], [100]) == [0]
    assert compare([100], [90]) == [10]
    assert compare([100], [110]) == [10]

def test_compare_large_integers():
    """Tests with very large integer values to ensure no overflow/precision issues."""
    assert compare([10**12], [10**12 + 500]) == [500]

@pytest.mark.parametrize("game, guess, expected", [
    ([1, 2, 3], [1, 2, 3], [0, 0, 0]),
    ([1, 2, 3], [4, 5, 6], [3, 3, 3]),
    ([0, 0, 0], [1, -1, 2], [1, 1, 2]),
    ([10, -10, 0], [5, 5, 5], [5, 15, 5]),
    ([1, -1, 1], [-1, 1, -1], [2, 2, 2]),
    ([5, 5, 5], [5, 4, 6], [0, 1, 1]),
])
def test_compare_parametrized(game, guess, expected):
    """Comprehensive parametrized test covering various mixed scenarios."""
    assert compare(game, guess) == expected