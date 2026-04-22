
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

# Note: The function 'compare' is assumed to be available in the namespace.
# If testing in a real environment, use: from solution import compare

@pytest.mark.parametrize("game, guess, expected", [
    # --- Provided Examples ---
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
    
    # --- Edge Cases: Empty and Single Element ---
    ([], [], []),
    ([10], [10], [0]),
    ([10], [5], [5]),
    ([10], [15], [5]),
    
    # --- Edge Cases: Zeros and Negatives ---
    ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
    ([-1, -5, 10], [-2, -10, 5], [1, 5, 5]),
    ([-10, 0], [10, 0], [20, 0]),
    
    # --- Edge Cases: Large Integers ---
    ([10**15], [0], [10**15]),
    ([10**15], [2 * 10**15], [10**15]),
])
def test_compare_logic(game, guess, expected):
    """Tests the core mathematical logic for various valid numeric scenarios."""
    assert compare(game, guess) == expected

def test_compare_mismatched_lengths():
    """
    Tests that the function raises a ValueError when input lengths do not match.
    The specification implies equal length; a robust implementation should 
    validate this rather than silently truncating via zip().
    """
    with pytest.raises(ValueError, match="equal length"):
        compare([1, 2, 3], [1, 2])
    
    with pytest.raises(ValueError, match="equal length"):
        compare([1, 2], [1, 2, 3])

def test_compare_invalid_types():
    """Tests that the function raises a TypeError when non-numeric values are provided."""
    with pytest.raises(TypeError):
        compare([1, "a"], [1, 2])
    
    with pytest.raises(TypeError):
        compare([1, 2], [1, None])
    
    with pytest.raises(TypeError):
        compare(["1", "2"], [1, 2])

def test_compare_none_inputs():
    """Tests that the function handles None inputs gracefully by raising TypeError."""
    with pytest.raises(TypeError):
        compare(None, [1, 2])
    
    with pytest.raises(TypeError):
        compare([1, 2], None)

def test_compare_float_precision():
    """
    Tests that the function handles floating point numbers.
    Uses pytest.approx to handle potential floating point arithmetic inaccuracies.
    """
    game = [1.5, 2.7, 0.0]
    guess = [1.0, 3.0, -0.5]
    expected = [0.5, 0.3, 0.5]
    
    result = compare(game, guess)
    assert result == pytest.approx(expected)

def test_compare_input_immutability():
    """
    Ensures that the function does not mutate the original input lists.
    A common bug in Python is modifying lists in-place.
    """
    game = [1, 2, 3]
    guess = [4, 5, 6]
    game_copy = list(game)
    guess_copy = list(guess)
    
    compare(game, guess)
    
    assert game == game_copy, "The 'game' input list was mutated!"
    assert guess == guess_copy, "The 'guess' input list was mutated!"