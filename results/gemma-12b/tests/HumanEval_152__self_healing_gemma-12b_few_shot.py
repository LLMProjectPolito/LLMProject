
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
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 5, 1]
    expected = [0, 0, 0, 0, 0, 0]
    assert compare(game, guess) == expected

def test_compare_incorrect_guesses():
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 2, -2]
    expected = [0, 0, 0, 0, 3, 3]
    assert compare(game, guess) == expected

def test_compare_mixed_guesses():
    game = [0, 5, 0, 0, 0, 4]
    guess = [4, 1, 1, 0, 0, -2]
    expected = [4, 4, 1, 0, 0, 6]
    assert compare(game, guess) == expected

def test_compare_empty_lists():
    game = []
    guess = []
    expected = []
    assert compare(game, guess) == expected

def test_compare_single_element_lists():
    game = [5]
    guess = [6]
    expected = [1]
    assert compare(game, guess) == expected

def test_compare_single_element_correct():
    game = [5]
    guess = [5]
    expected = [0]
    assert compare(game, guess) == expected

def test_compare_negative_scores():
    game = [-1, -2, -3]
    guess = [-1, -2, -4]
    expected = [0, 0, 1]
    assert compare(game, guess) == expected

def test_compare_large_numbers():
    game = [1000, 2000, 3000]
    guess = [1000, 2001, 3000]
    expected = [0, 1, 0]
    assert compare(game, guess) == expected

def test_compare_different_lengths():
    game = [1, 2, 3]
    guess = [1, 2]
    with pytest.raises(ValueError):
        compare(game, guess)

def test_compare_different_types():
    game = [1, 2, 3]
    guess = ["1", "2", "3"]
    with pytest.raises(TypeError):
        compare(game, guess)