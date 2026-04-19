
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

# The function 'compare' is assumed to be defined in the environment.

@pytest.mark.parametrize("game, guess, expected", [
    # --- Provided Docstring Examples ---
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
    
    # --- Edge Cases: List Size ---
    ([], [], []),                                      # Empty lists
    ([10], [10], [0]),                                 # Single element - match
    ([10], [5], [5]),                                  # Single element - difference
    ([5], [10], [5]),                                  # Single element - reverse difference
    
    # --- Value Scenarios ---
    ([10, 20, 30], [10, 20, 30], [0, 0, 0]),           # Identical lists
    ([1, 2, 3], [4, 5, 6], [3, 3, 3]),                 # Completely different
    ([1, 1, 1], [2, 3, 4], [1, 2, 3]),                 # Small differences
    
    # --- Negative Numbers and Zeros ---
    ([-1, -5, 0], [-1, -2, 2], [0, 3, 2]),             # Mixed signs
    ([-10, -20], [10, 20], [20, 40]),                  # Opposite signs
    ([0, 0, 0], [-5, 5, 0], [5, 5, 0]),                # Zeros vs signed
    ([-10, 10], [10, -10], [20, 20]),                  # Symmetric opposites
    
    # --- Large Integers ---
    ([10**12, 10**15], [10**12 + 5, 10**15 - 10], [5, 10]),
    ([1000000, 0], [2000000, -1000000], [1000000, 1000000]),
])
def test_compare_logic(game, guess, expected):
    """
    Test the core absolute difference logic across a wide spectrum of 
    numeric values and list sizes.
    """
    assert compare(game, guess) == expected

def test_compare_return_type():
    """
    Ensure that the function returns a list regardless of input values.
    """
    assert isinstance(compare([1], [2]), list)

def test_compare_output_length():
    """
    Verify that the output list length is strictly equal to the input list lengths.
    """
    game = [1, 2, 3, 4, 5]
    guess = [5, 4, 3, 2, 1]
    result = compare(game, guess)
    assert len(result) == len(game) == len(guess)

def test_compare_immutability():
    """
    Ensure the function is pure and does not mutate the original input lists.
    """
    game = [1, 2, 3]
    guess = [4, 5, 6]
    # Create deep copies for verification
    game_copy = game[:]
    guess_copy = guess[:]
    
    compare(game, guess)
    
    assert game == game_copy, "The 'game' list was mutated by the function"
    assert guess == guess_copy, "The 'guess' list was mutated by the function"