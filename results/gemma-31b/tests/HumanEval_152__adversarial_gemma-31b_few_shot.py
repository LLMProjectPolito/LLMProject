
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
    """Test the examples provided in the docstring to ensure basic functionality."""
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_all_correct():
    """Test cases where every guess is exactly correct."""
    assert compare([10, 20, 30], [10, 20, 30]) == [0, 0, 0]

def test_compare_all_incorrect():
    """Test cases where no guesses are correct."""
    assert compare([1, 1, 1], [2, 3, 4]) == [1, 2, 3]

def test_compare_negative_values():
    """
    Test handling of negative numbers. 
    Absolute difference between 5 and -5 should be 10.
    """
    assert compare([-1, -5, 2], [-1, -2, -3]) == [0, 3, 5]
    assert compare([5], [-5]) == [10]

def test_compare_empty_lists():
    """Test that empty lists return an empty list without crashing."""
    assert compare([], []) == []

def test_compare_single_element():
    """Test the boundary case of a single-element list."""
    assert compare([10], [10]) == [0]
    assert compare([10], [20]) == [10]

def test_compare_large_numbers():
    """Test with very large integers to ensure no overflow/precision issues."""
    assert compare([10**12], [10**12 + 5]) == [5]

@pytest.mark.parametrize("game, guess", [
    ([1, 2], [1]),       # Game longer than guess
    ([1], [1, 2]),       # Guess longer than game
])
def test_compare_unequal_lengths(game, guess):
    """
    Robustness check: The problem states lists are of equal length.
    A robust implementation should either handle this gracefully or 
    raise a specific error (like ValueError or IndexError).
    """
    # Depending on implementation, this might raise IndexError. 
    # We check that it doesn't return a misleading partial result.
    with pytest.raises((IndexError, ValueError)):
        compare(game, guess)

def test_compare_type_safety():
    """Test how the function handles non-integer inputs."""
    with pytest.raises(TypeError):
        compare([1, 2], ["1", "2"])