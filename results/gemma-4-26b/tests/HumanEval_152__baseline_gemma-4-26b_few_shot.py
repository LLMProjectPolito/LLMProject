
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

def test_compare_empty_lists():
    """Tests that empty lists return an empty list."""
    assert compare([], []) == []

def test_compare_identical_lists():
    """Tests that identical lists result in all zeros."""
    assert compare([10, 20, 30], [10, 20, 30]) == [0, 0, 0]
    assert compare([-1, -5, 0], [-1, -5, 0]) == [0, 0, 0]

def test_compare_negative_numbers():
    """Tests handling of negative integers and differences involving negatives."""
    # abs(-5 - (-2)) = 3
    # abs(-1 - 1) = 2
    # abs(2 - (-2)) = 4
    assert compare([-5, -1, 2], [-2, 1, -2]) == [3, 2, 4]

def test_compare_single_element():
    """Tests lists with a single element."""
    assert compare([10], [5]) == [5]
    assert compare([5], [10]) == [5]
    assert compare([0], [0]) == [0]

@pytest.mark.parametrize("game, guess, expected", [
    ([100, 200, 300], [0, 0, 0], [100, 200, 300]),
    ([0, 0, 0], [100, 200, 300], [100, 200, 300]),
    ([1, -1, 1, -1], [1, -1, 1, -1], [0, 0, 0, 0]),
    ([10, 20], [30, 40], [20, 20]),
])
def test_compare_parametrized(game, guess, expected):
    """Comprehensive parameterized test for various scenarios."""
    assert compare(game, guess) == expected

def test_compare_large_values():
    """Tests with large integer values."""
    assert compare([10**9, 0], [0, 10**9]) == [10**9, 10**9]