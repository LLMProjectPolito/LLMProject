
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
        if game[i] == guess[i]:
            result.append(0)
        else:
            result.append(abs(game[i] - guess[i]))
    return result

class TestCompare:
    def test_empty_lists(self):
        assert compare([], []) == []

    def test_equal_lists(self):
        assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    def test_different_lists(self):
        assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    def test_mixed_correct_and_incorrect(self):
        assert compare([1, 2, 3, 4, 5], [1, 2, 5, 4, 3]) == [0, 0, 2, 0, 2]

    def test_negative_numbers(self):
        assert compare([-1, -2, -3], [-1, -2, -4]) == [0, 0, 1]

    def test_zero_values(self):
        assert compare([0, 0, 0], [1, 2, 3]) == [1, 2, 3]

    def test_large_numbers(self):
        assert compare([1000, 2000, 3000], [1000, 2001, 2999]) == [0, 1, 1]

    def test_example_1(self):
        assert compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) == [0,0,0,0,3,3]

    def test_example_2(self):
        assert compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) == [4,4,1,0,0,6]

    def test_single_element_lists_correct(self):
        assert compare([5], [5]) == [0]

    def test_single_element_lists_incorrect(self):
        assert compare([5], [6]) == [1]

    def test_long_lists(self):
        game = list(range(100))
        guess = [x + 1 for x in range(100)]
        expected = [1] * 100
        assert compare(game, guess) == expected

    def test_all_incorrect(self):
        assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    def test_alternating_correct_incorrect(self):
        assert compare([1, 2, 3, 4, 5], [1, 5, 3, 2, 5]) == [0, 3, 0, 2, 0]

    def test_duplicate_values_in_game(self):
        assert compare([1, 1, 2, 3], [1, 2, 2, 3]) == [0, 1, 0, 0]

    def test_duplicate_values_in_guess(self):
        assert compare([1, 2, 3, 4], [1, 2, 2, 4]) == [0, 0, 1, 0]

    def test_compare_empty_lists(self):
        assert compare([], []) == []

    def test_compare_all_correct(self):
        assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    def test_compare_all_incorrect(self):
        assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    def test_compare_mixed_correct_incorrect(self):
        assert compare([1, 2, 3, 4], [1, 5, 3, 2]) == [0, 3, 0, 2]

    def test_compare_negative_numbers(self):
        assert compare([-1, -2, -3], [-1, -2, -4]) == [0, 0, 1]

    def test_compare_zero_values(self):
        assert compare([0, 0, 0], [1, 2, 3]) == [1, 2, 3]

    def test_compare_large_numbers(self):
        assert compare([100, 200, 300], [100, 201, 299]) == [0, 1, 1]

    def test_compare_different_lengths(self):
        with pytest.raises(IndexError):
            compare([1, 2], [1, 2, 3])