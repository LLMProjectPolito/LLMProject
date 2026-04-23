
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

# The function to be tested (placeholder for the implementation)
# def compare(game, guess):
#     ...

@pytest.mark.parametrize("game, guess, expected", [
    # Provided examples
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
    
    # Basic functionality
    ([10, 20, 30], [10, 20, 30], [0, 0, 0]),  # Perfect match
    ([10, 20, 30], [15, 25, 35], [5, 5, 5]),  # All different
    
    # Negative numbers (Crucial for absolute difference logic)
    ([-1, -5, 10], [-2, 5, -10], [1, 10, 20]),
    ([-10, -20], [-10, -20], [0, 0]),
    
    # Single element lists
    ([1], [1], [0]),
    ([1], [10], [9]),
    ([1], [-9], [10]),
    
    # Zeros
    ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
    ([0], [5], [5]),
])
def test_compare_functional_correctness(game, guess, expected):
    """Tests standard valid inputs including negatives and zeros."""
    assert compare(game, guess) == expected

def test_compare_empty_lists():
    """Tests the behavior when both lists are empty."""
    assert compare([], []) == []

def test_compare_mismatched_lengths():
    """
    Tests that the function handles (or raises an error for) 
    lists of unequal length.
    """
    # Depending on implementation, this should ideally raise a ValueError
    with pytest.raises(ValueError, match=".*length.*"):
        compare([1, 2, 3], [1, 2])

def test_compare_invalid_types():
    """Tests that the function handles non-integer/non-list inputs gracefully."""
    # Testing with None
    with pytest.raises(TypeError):
        compare(None, [1, 2])
    
    # Testing with strings inside the list
    with pytest.raises(TypeError):
        compare([1, "a"], [1, 2])

def test_compare_large_integers():
    """Tests the function with very large integers to ensure no overflow issues."""
    large_val1 = 10**18
    large_val2 = 10**18 + 7
    assert compare([large_val1], [large_val2]) == [7]

def test_compare_float_inputs():
    """
    Tests if the function handles floats. 
    If the requirement is strictly integers, this should be documented.
    If it supports floats, we check for precision.
    """
    # If the function is intended to be generic for numbers:
    assert compare([1.5, 2.5], [1.0, 3.0]) == [0.5, 0.5]