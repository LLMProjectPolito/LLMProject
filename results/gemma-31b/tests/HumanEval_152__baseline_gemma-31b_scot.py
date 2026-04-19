
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

# The function 'compare' is assumed to be defined in the environment as per instructions.

@pytest.mark.parametrize("game, guess, expected", [
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
])
def test_compare_provided_examples(game, guess, expected):
    """Test the function using the examples provided in the problem description."""
    assert compare(game, guess) == expected

def test_compare_all_correct():
    """Test scenario where all guesses are perfectly correct."""
    game = [10, 20, 30]
    guess = [10, 20, 30]
    assert compare(game, guess) == [0, 0, 0]

def test_compare_all_incorrect():
    """Test scenario where all guesses are incorrect."""
    game = [10, 20, 30]
    guess = [15, 25, 35]
    assert compare(game, guess) == [5, 5, 5]

def test_compare_empty_lists():
    """Test behavior with empty input lists."""
    assert compare([], []) == []

def test_compare_negative_values():
    """Test cases involving negative integers to ensure absolute difference is calculated."""
    # game: -1, guess: -5 -> |-1 - (-5)| = 4
    # game: -10, guess: 10 -> |-10 - 10| = 20
    # game: 5, guess: -5 -> |5 - (-5)| = 10
    game = [-1, -10, 5]
    guess = [-5, 10, -5]
    assert compare(game, guess) == [4, 20, 10]

def test_compare_single_element():
    """Test the function with lists containing only one element."""
    assert compare([100], [90]) == [10]
    assert compare([100], [100]) == [0]

def test_compare_large_numbers():
    """Test the function with very large integers."""
    game = [10**12, 2**64]
    guess = [10**12 + 500, 2**64 - 100]
    assert compare(game, guess) == [500, 100]

def test_compare_zero_values():
    """Test cases where values are zero."""
    assert compare([0, 0], [0, 0]) == [0, 0]
    assert compare([0, 0], [5, -5]) == [5, 5]