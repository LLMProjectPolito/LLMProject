
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
    Determines if a person correctly guessed the results of a number of matches.
    Returns an array denoting the absolute difference between the guess and the score.
    """
    return [abs(g - s) for g, s in zip(game, guess)]

class TestCompareFunction:
    """
    Comprehensive test suite for the compare function.
    """

    @pytest.mark.parametrize("game, guess, expected", [
        # Provided examples
        ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
        ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
        # All correct guesses
        ([10, 20, 30, 40], [10, 20, 30, 40], [0, 0, 0, 0]),
        # All incorrect guesses
        ([1, 1, 1], [2, 3, 4], [1, 2, 3]),
        ([10, 20, 30], [0, 0, 0], [10, 20, 30]),
        # Mixed positive and negative values
        ([-1, -5, -10], [-1, -2, -15], [0, 3, 5]),
        ([-1, -5, 2], [-1, -10, -2], [0, 5, 4]),
        # Zeros
        ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
        # Single element lists
        ([10], [10], [0]),
        ([10], [7], [3]),
        ([10], [13], [3]),
        ([5], [2], [3]),
        # Large values
        ([10**12, 0], [10**12 + 500, -10**12], [500, 10**12]),
        ([1000000, 5000000], [900000, 6000000], [100000, 1000000]),
        # Large negative differences
        ([-100, 100], [100, -100], [200, 200]),
    ])
    def test_standard_cases(self, game, guess, expected):
        """Test a variety of standard input scenarios including examples and edge values."""
        assert compare(game, guess) == expected

    def test_empty_lists(self):
        """Test behavior with empty input lists."""
        assert compare([], []) == []

    def test_floating_point_values(self):
        """Test with floats to ensure absolute difference works for non-integers."""
        game = [1.5, 2.0, 3.7]
        guess = [1.0, 2.5, 3.7]
        # Use pytest.approx for float comparisons to avoid precision issues
        assert compare(game, guess) == pytest.approx([0.5, 0.5, 0.0])

    def test_mismatched_lengths(self):
        """
        Test behavior when input lists are of different lengths.
        The zip function in the implementation should truncate to the shortest list.
        """
        game = [1, 2, 3]
        guess = [1, 2]
        assert compare(game, guess) == [0, 0]
        
        game_short = [1, 2]
        guess_long = [1, 2, 3]
        assert compare(game_short, guess_long) == [0, 0]

    def test_input_immutability(self):
        """Ensure the original lists are not mutated by the function."""
        game = [1, 2, 3]
        guess = [4, 5, 6]
        game_copy = list(game)
        guess_copy = list(guess)
        
        compare(game, guess)
        
        assert game == game_copy
        assert guess == guess_copy