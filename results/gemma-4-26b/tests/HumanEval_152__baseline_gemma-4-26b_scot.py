
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
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
])
def test_compare_provided_examples(game, guess, expected):
    """Validates the examples provided in the problem description."""
    assert compare(game, guess) == expected

def test_compare_empty_lists():
    """Verifies that empty input lists return an empty list."""
    assert compare([], []) == []

def test_compare_all_matches():
    """Verifies that identical lists result in all zeros."""
    game = [10, 20, 30, 40]
    guess = [10, 20, 30, 40]
    assert compare(game, guess) == [0, 0, 0, 0]

def test_compare_single_element():
    """Tests the function with a single element list."""
    assert compare([10], [5]) == [5]
    assert compare([5], [10]) == [5]
    assert compare([5], [5]) == [0]

def test_compare_negative_and_positive_mix():
    """Tests logic with negative numbers to ensure absolute difference is correct."""
    # |(-5) - (-2)| = |-3| = 3
    # |(-5) - 5| = |-10| = 10
    # |5 - (-2)| = |7| = 7
    game = [-5, -5, 5]
    guess = [-2, 5, -2]
    expected = [3, 10, 7]
    assert compare(game, guess) == expected

def test_compare_large_values():
    """Tests the function with large integer values."""
    game = [10**9, 0]
    guess = [10**9 + 7, -10**9]
    expected = [7, 10**9]
    assert compare(game, guess) == expected

def test_compare_zeros():
    """Tests scenarios involving zeros."""
    game = [0, 0, 0]
    guess = [0, 5, -5]
    expected = [0, 5, 5]
    assert compare(game, guess) == expected

def test_compare_all_mismatches():
    """Tests a scenario where no guesses are correct."""
    game = [1, 2, 3]
    guess = [4, 5, 6]
    expected = [3, 3, 3]
    assert compare(game, guess) == expected