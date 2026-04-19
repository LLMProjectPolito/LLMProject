
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
    Implementation of the function to be tested.
    """
    if len(game) != len(guess):
        raise ValueError("Input arrays must be of equal length")
    
    return [abs(g - gu) for g, gu in zip(game, guess)]

class TestCompareFunction:
    """
    Blue Team QA Suite for the compare function.
    Focuses on boundary conditions, edge cases, and input validation.
    """

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
        # Edge Case: All correct guesses
        ([1, 2, 3], [1, 2, 3], [0, 0, 0]),
        # Edge Case: All incorrect guesses
        ([1, 2, 3], [10, 20, 30], [9, 18, 27]),
        # Edge Case: Negative numbers and mixed signs
        ([-1, -5, -10], [-1, -2, -15], [0, 3, 5]),
        ([-1, 1], [1, -1], [2, 2]),
        # Edge Case: Large integers
        ([10**12], [10**12 + 5], [5]),
        # Edge Case: Zeros
        ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
    ])
    def test_compare_valid_inputs(self, game, guess, expected):
        """Tests standard functionality and boundary values."""
        assert compare(game, guess) == expected

    def test_mismatched_lengths(self):
        """Tests that the function handles arrays of different lengths."""
        with pytest.raises(ValueError):
            compare([1, 2], [1, 2, 3])
        with pytest.raises(ValueError):
            compare([1, 2, 3], [1, 2])

    def test_non_numeric_inputs(self):
        """Tests that the function raises TypeError when non-numeric values are passed."""
        with pytest.raises(TypeError):
            compare([1, 2], ["1", "2"])
        with pytest.raises(TypeError):
            compare([None], [1])

    def test_non_iterable_inputs(self):
        """Tests that the function raises TypeError when inputs are not lists/iterables."""
        with pytest.raises(TypeError):
            compare(None, [1, 2])
        with pytest.raises(TypeError):
            compare(123, 456)

    def test_immutability(self):
        """Ensures the original input lists are not mutated by the function."""
        game = [1, 2, 3]
        guess = [4, 5, 6]
        game_copy = game[:]
        guess_copy = guess[:]
        
        compare(game, guess)
        
        assert game == game_copy, "The 'game' list was mutated"
        assert guess == guess_copy, "The 'guess' list was mutated"