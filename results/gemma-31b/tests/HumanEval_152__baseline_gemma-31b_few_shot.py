
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

def test_compare_provided_examples():
    """Tests the examples provided in the docstring."""
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_all_correct():
    """Tests cases where all guesses are exactly correct."""
    assert compare([10, 20, 30], [10, 20, 30]) == [0, 0, 0]
    assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]

def test_compare_all_incorrect():
    """Tests cases where no guesses are correct."""
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]
    assert compare([10, 10, 10], [0, 0, 0]) == [10, 10, 10]

def test_compare_empty_lists():
    """Tests behavior with empty input lists."""
    assert compare([], []) == []

def test_compare_single_element():
    """Tests lists containing only one element."""
    assert compare([5], [5]) == [0]
    assert compare([5], [10]) == [5]
    assert compare([5], [0]) == [5]

def test_compare_negative_numbers():
    """Tests absolute difference calculation with negative integers."""
    # |(-1) - (-1)| = 0
    # |(-5) - (-2)| = 3
    # |(2) - (-3)| = 5
    assert compare([-1, -5, 2], [-1, -2, -3]) == [0, 3, 5]
    # |(-10) - (10)| = 20
    assert compare([-10], [10]) == [20]

def test_compare_large_values():
    """Tests the function with larger integer values."""
    assert compare([1000000, 0], [0, 1000000]) == [1000000, 1000000]

def test_compare_mixed_signs():
    """Tests a mix of positive, negative, and zero values."""
    game = [0, -1, 1, -5, 5]
    guess = [1, 0, 0, -10, 10]
    # |0-1|=1, |-1-0|=1, |1-0|=1, |-5--10|=5, |5-10|=5
    assert compare(game, guess) == [1, 1, 1, 5, 5]