
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
    # Provided examples from docstring
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
    
    # Edge cases: Empty lists
    ([], [], []),
    
    # Edge cases: Single element
    ([10], [10], [0]),
    ([10], [5], [5]),
    ([10], [15], [5]),
    
    # All elements match or are identical
    ([1, 2, 3], [1, 2, 3], [0, 0, 0]),
    ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
    ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
    
    # No elements match
    ([1, 1, 1], [2, 2, 2], [1, 1, 1]),
    
    # Negative numbers and mixed signs
    ([-1, -5, -10], [-2, 5, 10], [1, 10, 20]),
    ([0, -1, 1], [1, 1, -1], [1, 2, 2]),
    ([-1, -5, 2], [-2, 5, -2], [1, 10, 4]),
    ([5, -5], [-5, 5], [10, 10]),
    ([1, -1, 0], [-1, 1, 0], [2, 2, 0]),
    
    # Large numbers
    ([1000000, 0], [0, 1000000], [1000000, 1000000]),
    ([10**12, 0], [10**12 + 5, -5], [5, 5]),
    
    # Input as tuples (ensuring robustness for iterables)
    ((1, 2), (3, 4), [2, 2]),
])
def test_compare(game, guess, expected):
    """Tests the compare function with various scenarios including docstring examples,
    edge cases, negative numbers, and large values."""
    assert compare(game, guess) == expected

def test_compare_type_consistency():
    """Verify that the output is always a list."""
    result = compare([1, 2], [3, 4])
    assert isinstance(result, list)

def test_compare_length_consistency():
    """Verify that the output length matches the input length."""
    game = [1, 2, 3, 4, 5]
    guess = [5, 4, 3, 2, 1]
    assert len(compare(game, guess)) == len(game)