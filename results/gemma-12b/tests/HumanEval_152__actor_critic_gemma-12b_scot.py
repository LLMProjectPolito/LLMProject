
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
    result = []
    for i in range(len(game)):
        if guess[i] == game[i]:
            result.append(0)
        else:
            result.append(abs(guess[i] - game[i]))
    return result

class TestCompare:
    @pytest.mark.parametrize("game, guess, expected", [
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [0, 0, 0, 0, 0]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [4, 2, 0, 2, 4]),
    ])
    def test_correct_guesses_incorrect_guesses(self, game, guess, expected):
        assert compare(game, guess) == expected

    def test_mixed_guesses(self):
        game = [1, 2, 3, 4, 5, 1]
        guess = [1, 2, 3, 4, 2, -2]
        expected = [0, 0, 0, 0, 3, 3]
        assert compare(game, guess) == expected

    def test_empty_lists(self):
        game = []
        guess = []
        expected = []
        assert compare(game, guess) == expected

    def test_single_element_lists_correct(self):
        game = [5]
        guess = [5]
        expected = [0]
        assert compare(game, guess) == expected

    def test_single_element_lists_incorrect(self):
        game = [5]
        guess = [6]
        expected = [1]
        assert compare(game, guess) == expected

    def test_negative_scores(self):
        game = [-1, -2, -3]
        guess = [-1, -2, -4]
        expected = [0, 0, 1]
        assert compare(game, guess) == expected

    def test_zero_scores(self):
        game = [0, 0, 0]
        guess = [0, 1, 0]
        expected = [0, 1, 0]
        assert compare(game, guess) == expected

    def test_large_scores(self):
        game = [1000, 2000, 3000]
        guess = [1001, 2000, 2999]
        expected = [1, 0, 1]
        assert compare(game, guess) == expected

    def test_large_difference(self):
        game = [1]
        guess = [1000]
        expected = [999]
        assert compare(game, guess) == expected

    def test_different_data_types(self):
        game = [1, 2, 3]
        guess = ["a", 2, 3]
        with pytest.raises(TypeError):
            compare(game, guess)

    def test_unequal_length_lists(self):
        game = [1, 2, 3]
        guess = [1, 2]
        with pytest.raises(IndexError):
            compare(game, guess)

    def test_none_values(self):
        game = [1, None, 3]
        guess = [1, None, 3]
        with pytest.raises(TypeError):
            compare(game, guess)

    def test_floating_point_numbers(self):
        game = [1.0, 2.5, 3.0]
        guess = [1.1, 2.5, 3.0]
        expected = [0.1, 0.0, 0.0]
        assert compare(game, guess) == pytest.approx(expected)