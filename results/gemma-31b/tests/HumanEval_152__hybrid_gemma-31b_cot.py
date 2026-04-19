
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
    # Provided examples
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
    
    # Edge Case: Empty lists
    ([], [], []),
    
    # Edge Case: Single element lists
    ([10], [10], [0]),
    ([10], [5], [5]),
    ([10], [15], [5]),
    ([10], [-10], [20]),
    ([5], [10], [5]),
    
    # Case: All correct guesses
    ([1, 2, 3], [1, 2, 3], [0, 0, 0]),
    
    # Case: All incorrect guesses
    ([1, 2, 3], [4, 5, 6], [3, 3, 3]),
    ([1, 1, 1], [2, 2, 2], [1, 1, 1]),
    
    # Case: Negative numbers and mixed signs
    ([-1, -2, -3], [-1, -5, 0], [0, 3, 3]),
    ([-1, -2, -3], [-1, -4, -1], [0, 2, 2]),
    ([1, 2, 3], [-1, -2, -3], [2, 4, 6]),
    ([10, -10, 0], [-10, 10, 0], [20, 20, 0]),
    ([-5, -10], [5, 10], [10, 20]),
    
    # Case: Large numbers
    ([1000000, 0], [2000000, -1000000], [1000000, 1000000]),
    ([1000000, 0], [0, 1000000], [1000000, 1000000]),
    
    # Case: Zeros
    ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
    ([0, 0], [1, -1], [1, 1]),
])
def test_compare(game, guess, expected):
    """
    Tests the compare function with a comprehensive set of scenarios including 
    provided examples, empty lists, single elements, negative numbers, 
    mixed signs, and large values.
    """
    assert compare(game, guess) == expected

def test_compare_type_consistency():
    """Ensure the return type is always a list."""
    result = compare([1], [2])
    assert isinstance(result, list)

def test_compare_length_consistency():
    """Ensure the length of the output list matches the length of the input lists."""
    game = [1, 2, 3, 4, 5]
    guess = [6, 7, 8, 9, 10]
    assert len(compare(game, guess)) == len(game) == len(guess)

def test_compare_immutability():
    """Ensure the original input lists are not modified by the function."""
    game = [1, 2, 3]
    guess = [4, 5, 6]
    game_copy = list(game)
    guess_copy = list(guess)
    
    compare(game, guess)
    
    assert game == game_copy, "The 'game' list was modified in-place."
    assert guess == guess_copy, "The 'guess' list was modified in-place."

def test_compare_different_lengths():
    """
    Sanity check for mismatched input lengths. 
    While the problem specifies equal length, the function should handle 
    it gracefully (either via truncation or raising an error).
    """
    try:
        result = compare([1, 2], [1])
        assert isinstance(result, list)
    except IndexError:
        # IndexError is an acceptable response to invalid input constraints
        pass