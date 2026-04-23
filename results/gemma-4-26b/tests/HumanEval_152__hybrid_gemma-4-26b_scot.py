
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

# Note: The function 'compare' is assumed to be imported or defined in the environment.

@pytest.mark.parametrize("game, guess, expected", [
    # Docstring Examples
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
    
    # Exact Matches (All zeros)
    ([10, 20, 30, 40], [10, 20, 30, 40], [0, 0, 0, 0]),
    ([100, 200], [100, 200], [0, 0]),
    
    # Complete Mismatches
    ([1, 2, 3], [4, 5, 6], [3, 3, 3]),
    ([10, 20, 30], [40, 30, 20], [30, 10, 10]),
    
    # Mixed Signs and Zeros
    ([-5, 5, -1], [5, -5, -3], [10, 10, 2]), # Mixed signs
    ([5, -5], [-5, 5], [10, 10]),           # Mixed signs
    ([0, 0, 0], [0, 5, -5], [0, 5, 5]),     # Zeros
    ([1, -1, 0], [1, 1, -1], [0, 2, 1]),    # Mixed signs/zeros
    ([0, 0, 0], [1, 2, 3], [1, 2, 3]),      # Zeros vs positive
])
def test_compare_logic_scenarios(game, guess, expected):
    """Tests core logic including docstring examples, exact matches, mismatches, and sign variations."""
    assert compare(game, guess) == expected

def test_compare_empty_input():
    """Tests that empty input lists return an empty list."""
    assert compare([], []) == []

def test_compare_single_element():
    """Tests the function with lists containing only one element."""
    assert compare([10], [7]) == [3]
    assert compare([10], [10]) == [0]
    assert compare([10], [13]) == [3]

def test_compare_large_integers():
    """Tests the function with very large integers to ensure no overflow/precision issues."""
    # Test 10^12 scale
    assert compare([10**12, 0], [10**12 + 5, -10**12]) == [5, 10**12]
    # Test 10^15 scale
    assert compare([10**15], [10**15 + 7]) == [7]

def test_compare_floating_point():
    """Tests that the function handles float inputs correctly."""
    game = [1.5, 2.0, 0.0]
    guess = [1.0, 2.5, -0.5]
    # |1.5-1.0|=0.5, |2.0-2.5|=0.5, |0.0-(-0.5)|=0.5
    assert compare(game, guess) == [0.5, 0.5, 0.5]