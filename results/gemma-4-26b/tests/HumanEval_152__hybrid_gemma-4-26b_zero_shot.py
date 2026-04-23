
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

def compare(game, guess):
    """
    Determines how far off each guess was from the actual game scores.
    Returns a list of absolute differences.
    """
    return [abs(g - gu) for g, gu in zip(game, guess)]

@pytest.mark.parametrize("game, guess, expected", [
    # Docstring Examples
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
    
    # Edge Case: Empty lists
    ([], [], []),
    
    # Edge Case: Single element lists
    ([10], [10], [0]),
    ([10], [5], [5]),
    ([10], [15], [5]),
    
    # Case: All elements are identical (Perfect guesses)
    ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
    
    # Case: All elements are completely different
    ([1, 2, 3], [10, 20, 30], [9, 18, 27]),
    
    # Case: Zeros
    ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
    ([0, 0, 0], [5, -5, 5], [5, 5, 5]),
    
    # Case: Negative numbers
    ([-1, -5, -10], [-2, 5, 10], [1, 10, 20]),
    ([-10, -20], [-10, -20], [0, 0]),
    
    # Case: Large integers
    ([10**6, 0], [2*10**6, -10**6], [10**6, 10**6]),
])
def test_compare_logic(game, guess, expected):
    """Tests the core logic across various integer scenarios including negatives, zeros, and large values."""
    assert compare(game, guess) == expected

def test_compare_floating_point():
    """Tests the function with floating point numbers to ensure precision handling."""
    game = [1.5, 2.0, 3.75]
    guess = [1.0, 2.5, 3.0]
    expected = [0.5, 0.5, 0.75]
    # Use pytest.approx for floating point comparisons to avoid precision issues
    assert compare(game, guess) == pytest.approx(expected)

def test_compare_mismatched_lengths():
    """
    Tests behavior when lengths are unequal. 
    Based on the implementation using zip(), it should truncate to the shortest list.
    """
    game = [1, 2, 3]
    guess = [1, 2]
    expected = [0, 0]
    assert compare(game, guess) == expected

def test_compare_immutability():
    """Ensures the original input lists are not mutated by the function."""
    game = [1, 2, 3]
    guess = [4, 5, 6]
    game_copy = game[:]
    guess_copy = guess[:]
    
    compare(game, guess)
    
    assert game == game_copy
    assert guess == guess_copy

def test_compare_type_error():
    """Tests that the function handles non-numeric types by raising a TypeError."""
    with pytest.raises(TypeError):
        compare([1, "a"], [1, 2])

def test_compare_large_input_size():
    """Tests the function with a larger dataset to ensure performance and correctness."""
    size = 1000
    game = list(range(size))
    guess = [x + 1 for x in range(size)]
    expected = [1] * size
    assert compare(game, guess) == expected