
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

def test_compare_examples():
    """Test the examples provided in the docstring."""
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_empty_lists():
    """Test with empty lists."""
    assert compare([], []) == []

def test_compare_single_element():
    """Test with single element lists."""
    assert compare([5], [5]) == [0]
    assert compare([5], [2]) == [3]
    assert compare([10], [5]) == [5]
    assert compare([10], [-10]) == [20]

@pytest.mark.parametrize("game, guess, expected", [
    # All correct
    ([10, 20, 30], [10, 20, 30], [0, 0, 0]),
    ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
    # All incorrect
    ([1, 2, 3], [4, 5, 6], [3, 3, 3]),
    ([10, 20, 30], [15, 25, 35], [5, 5, 5]),
    # Negative values and mixed signs
    ([-1, -5], [-2, -10], [1, 5]),
    ([-1, 1], [1, -1], [2, 2]),
    ([-1, -5, -10], [-1, -2, -15], [0, 3, 5]),
    ([-1, -5], [1, 5], [2, 10]),
    ([-1, -10], [-5, 10], [4, 20]),
    ([1, -1, 2], [-1, 1, -2], [2, 2, 4]),
    # Large numbers
    ([1000000, 0], [0, 1000000], [1000000, 1000000]),
    ([1000000, 0], [2000000, -1000000], [1000000, 1000000]),
    # Zeros and boundary cases
    ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
    ([10, 20, 30], [0, 0, 0], [10, 20, 30]),
    ([0, 0, 0], [10, 20, 30], [10, 20, 30]),
    ([100, 200], [101, 199], [1, 1]),
])
def test_compare_parametrized(game, guess, expected):
    """Parametrized tests for various edge cases and value combinations."""
    assert compare(game, guess) == expected