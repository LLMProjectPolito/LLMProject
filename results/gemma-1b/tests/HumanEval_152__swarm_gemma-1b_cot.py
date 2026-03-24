
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
from math import sqrt

def game():
    """
    A simple game where the goal is to guess the correct score.
    """
    def game_function(guess, score):
        """
        The function to be tested.
        """
        if guess == score:
            return 0
        else:
            return abs(guess - score)

    def get_results(game_function, guess, score):
        """
        Generates a list of results based on the game function.
        """
        results = []
        for i in range(len(game_function(guess, score))):
            results.append(abs(game_function(guess, score) - score))
        return results

    return get_results(game, 0, 0)

def test_results_valid_guess():
    """
    Test case where the guess matches the score.
    """
    results = get_results(game, 0, 0)
    assert results == [0]

def test_results_invalid_guess():
    """
    Test case where the guess is different from the score.
    """
    results = get_results(game, 0, 0)
    assert results == [abs(0 - 0)]

def test_results_all_invalid_guesses():
    """
    Test case where all guesses are invalid.
    """
    results = get_results(game, 0, 0)
    assert results == [0]

def test_results_empty_game():
    """
    Test case with an empty game.
    """
    results = get_results(game, 0, 0)
    assert results == []