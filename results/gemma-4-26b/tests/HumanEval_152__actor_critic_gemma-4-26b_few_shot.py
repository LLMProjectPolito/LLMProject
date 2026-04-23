
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
import math

# Note: The implementation of compare() is assumed to be provided elsewhere.
# We assume it raises ValueError for length mismatches and TypeError for 
# non-numeric inputs or non-iterable arguments.

@pytest.mark.parametrize("game, guess, expected", [
    # Docstring Examples
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
    
    # Standard Scenarios
    ([10, 20, 30], [10, 20, 30], [0, 0, 0]),      # All correct
    ([1, 1, 1], [2, 2, 2], [1, 1, 1]),            # All wrong
    ([10], [5], [5]),                             # Single element (wrong)
    ([10], [10], [0]),                            # Single element (correct)
    ([-5, -1], [-2, 5], [3, 6]),                  # Negative numbers
    ([5, -5, 0], [-5, 5, 0], [10, 10, 0]),        # Mixed signs
    ([], [], []),                                 # Empty lists
    
    # Floating Point Numbers
    ([1.5, 2.5, 3.0], [1.0, 3.0, 3.0], [0.5, 0.5, 0.0]),
    ([0.1, 0.2], [0.3, 0.4], [0.2, 0.2]),
])
def test_compare_valid_scenarios(game, guess, expected):
    """
    Tests all valid input scenarios, including integers, floats, 
    negatives, and empty lists.
    """
    assert compare(game, guess) == pytest.approx(expected)


def test_compare_special_floats():
    """
    Tests behavior with special floating point values like infinity and NaN.
    """
    # Test Infinity
    inf_result = compare([float('inf')], [1])
    assert inf_result == [float('inf')]

    # Test NaN (NaN != NaN, so we must check using math.isnan)
    nan_result = compare([float('nan')], [1])
    assert math.isnan(nan_result[0])


def test_compare_iterable_types():
    """
    Tests whether the function accepts other iterables like tuples and range objects.
    """
    assert compare((1, 2, 3), (1, 2, 3)) == [0, 0, 0]  # Tuples
    assert compare(range(3), [1, 2, 3]) == [0, 0, 0]   # Range objects


def test_compare_booleans():
    """
    Tests how the function handles boolean values. 
    Since bool is a subclass of int, True should be treated as 1 and False as 0.
    """
    assert compare([True, False], [1, 0]) == [0, 0]
    assert compare([True, True], [0, 0]) == [1, 1]


def test_compare_mismatched_lengths():
    """
    Tests that a ValueError is raised when the input lists 
    have different lengths.
    """
    with pytest.raises(ValueError):
        compare([1, 2], [1, 2, 3])
    
    with pytest.raises(ValueError):
        compare([1, 2, 3], [1, 2])


def test_compare_non_numeric_or_non_iterable_types():
    """
    Tests that a TypeError is raised when the lists contain 
    non-numeric elements or when the arguments themselves are not iterable.
    """
    # Non-numeric elements inside the list
    with pytest.raises(TypeError):
        compare([1, "two", 3], [1, 2, 3])
    
    with pytest.raises(TypeError):
        compare([1, 2, 3], [1, None, 3])
    
    # Non-iterable arguments
    with pytest.raises(TypeError):
        compare(None, [1, 2, 3])
    
    with pytest.raises(TypeError):
        compare([1, 2, 3], 5)