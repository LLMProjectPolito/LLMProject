
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
    
    # Edge case: Empty lists
    ([], [], []),
    
    # Edge case: Single element
    ([10], [10], [0]),
    ([10], [5], [5]),
    ([10], [15], [5]),
    ([10], [7], [3]),
    ([10], [13], [3]),
    
    # Edge case: All elements match
    ([1, 2, 3], [1, 2, 3], [0, 0, 0]),
    ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
    ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
    
    # Edge case: No elements match
    ([1, 2, 3], [4, 5, 6], [3, 3, 3]),
    
    # Edge case: Negative numbers and mixed signs
    ([-1, -5, 10], [-1, 5, -10], [0, 10, 20]),
    ([-1, -5, 10], [-2, 0, 5], [1, 5, 5]),
    ([0, 0, 0], [-1, 1, 0], [1, 1, 0]),
    ([0, 0, 0], [-1, -1, -1], [1, 1, 1]),
    ([-5, 5], [5, -5], [10, 10]),
    ([-1, -5, -10], [-1, -5, -10], [0, 0, 0]),
    ([-1, -5, -10], [1, 5, 10], [2, 10, 20]),
    ([1, 5, 10], [-1, -5, -10], [2, 10, 20]),
    ([5, -5, 0], [-5, 5, 0], [10, 10, 0]),
    
    # Edge case: Large numbers
    ([1000000, 0], [2000000, -1000000], [1000000, 1000000]),
    ([1000000, 0], [0, 1000000], [1000000, 1000000]),
    
    # Edge case: Floating point
    ([1.5, 2.5], [1.0, 3.0], [0.5, 0.5]),
])
def test_compare(game, guess, expected):
    """Tests the compare function with various inputs including 
    provided examples, empty lists, single elements, negative numbers, 
    and large integers."""
    assert compare(game, guess) == expected

def test_compare_output_length():
    """Ensures that the output list length is always equal to the input length."""
    game = [1, 2, 3, 4, 5]
    guess = [5, 4, 3, 2, 1]
    result = compare(game, guess)
    assert len(result) == len(game)
    assert len(result) == len(guess)

def test_compare_type_consistency():
    """Ensures the returned object is a list."""
    result = compare([1, 2], [3, 4])
    assert isinstance(result, list)
    assert len(result) == 2

def test_compare_immutability():
    """Ensures the original input lists are not mutated by the function."""
    game = [1, 2, 3]
    guess = [4, 5, 6]
    game_copy = game[:]
    guess_copy = guess[:]
    
    compare(game, guess)
    
    assert game == game_copy
    assert guess == guess_copy