
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
from your_module import compare  # Replace your_module

def test_compare_correct_guesses():
    """Test case where all guesses are correct."""
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 5, 1]
    expected = [0, 0, 0, 0, 0, 0]
    assert compare(game, guess) == expected

def test_compare_incorrect_guesses():
    """Test case where some guesses are incorrect."""
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 2, -2]
    expected = [0, 0, 0, 0, 3, 3]
    assert compare(game, guess) == expected

def test_compare_all_incorrect_guesses():
    """Test case where all guesses are incorrect."""
    game = [0, 5, 0, 0, 0, 4]
    guess = [4, 1, 1, 0, 0, -2]
    expected = [4, 4, 1, 0, 0, 6]
    assert compare(game, guess) == expected

def test_compare_empty_arrays():
    """Test case with empty arrays."""
    game = []
    guess = []
    expected = []
    assert compare(game, guess) == expected

def test_compare_single_element_arrays():
    """Test case with single element arrays."""
    game = [5]
    guess = [6]
    expected = [1]
    assert compare(game, guess) == expected

def test_compare_single_element_correct():
    """Test case with single element arrays, correct guess."""
    game = [5]
    guess = [5]
    expected = [0]
    assert compare(game, guess) == expected

def test_compare_negative_scores():
    """Test case with negative scores."""
    game = [-1, -2, -3]
    guess = [-1, -2, 0]
    expected = [0, 0, 3]
    assert compare(game, guess) == expected

def test_compare_mixed_scores():
    """Test case with mixed positive and negative scores."""
    game = [-1, 2, -3, 4]
    guess = [-1, 1, -3, 5]
    expected = [0, 2, 0, 1]
    assert compare(game, guess) == expected

def test_compare_large_numbers():
    """Test case with large numbers to check for overflow issues."""
    game = [1000000, 2000000]
    guess = [1000000, 2000001]
    expected = [0, 1]
    assert compare(game, guess) == expected

def test_compare_different_lengths():
    """Test case to ensure the function handles different lengths gracefully (should raise an error)."""
    game = [1, 2, 3]
    guess = [1, 2]
    with pytest.raises(ValueError):
        compare(game, guess)

def test_compare_invalid_input_types():
    """Test case to ensure the function handles invalid input types gracefully (should raise an error)."""
    game = [1, 2, 3]
    guess = ["a", 2, 3]
    with pytest.raises(TypeError):
        compare(game, guess)