
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
    """Test the examples provided in the docstring."""
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_empty_lists():
    """Test behavior with empty input lists."""
    assert compare([], []) == []

def test_compare_single_element():
    """Test lists with a single element."""
    assert compare([10], [10]) == [0]
    assert compare([10], [5]) == [5]
    assert compare([5], [10]) == [5]
    assert compare([-1], [1]) == [2]

def test_compare_all_correct():
    """Test cases where all guesses are exactly correct."""
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]
    assert compare([-1, -5, 0], [-1, -5, 0]) == [0, 0, 0]

def test_compare_all_incorrect():
    """Test cases where no guesses are correct."""
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]
    assert compare([0, 0, 0], [1, -1, 2]) == [1, 1, 2]

def test_compare_negative_values():
    """Test various combinations of negative scores and guesses."""
    # Both negative: abs(-5 - (-2)) = abs(-3) = 3
    assert compare([-5], [-2]) == [3]
    # Both negative: abs(-2 - (-5)) = abs(3) = 3
    assert compare([-2], [-5]) == [3]
    # Mixed: abs(-1 - 1) = 2
    assert compare([-1], [1]) == [2]
    # Mixed: abs(1 - (-1)) = 2
    assert compare([1], [-1]) == [2]

def test_compare_large_values():
    """Test with very large integers to ensure no overflow/precision issues."""
    large_val = 10**15
    assert compare([large_val], [0]) == [large_val]
    assert compare([large_val], [large_val + 100]) == [100]

def test_compare_floats():
    """Test if the function handles floating point numbers correctly."""
    # Using pytest.approx for float comparisons to avoid precision errors
    result = compare([1.5, 2.7], [1.0, 3.0])
    assert result == pytest.approx([0.5, 0.3])

@pytest.mark.parametrize("game, guess, expected", [
    ([10, 20], [10, 20], [0, 0]),
    ([10, 20], [12, 18], [2, 2]),
    ([0, 0], [-5, 5], [5, 5]),
    ([100, -100], [50, -50], [50, 50]),
])
def test_compare_parametrized(game, guess, expected):
    """General parameterized tests for various scenarios."""
    assert compare(game, guess) == expected