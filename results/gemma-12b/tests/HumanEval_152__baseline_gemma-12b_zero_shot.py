
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

def test_compare_empty_lists():
    assert compare([], []) == []

def test_compare_single_element_correct():
        assert compare([5], [5]) == [0]

def test_compare_single_element_incorrect():
    assert compare([5], [6]) == [1]

def test_compare_positive_numbers_correct():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_compare_positive_numbers_incorrect():
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_compare_mixed_numbers_correct():
    assert compare([1, 5, 3], [1, 5, 3]) == [0, 0, 0]

def test_compare_mixed_numbers_incorrect():
    assert compare([1, 5, 3], [2, 4, 6]) == [1, 1, 3]

def test_compare_zero_scores():
    assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]

def test_compare_zero_scores_incorrect():
    assert compare([0, 0, 0], [1, 2, 3]) == [1, 2, 3]

def test_compare_negative_scores():
    assert compare([-1, -2, -3], [-1, -2, -3]) == [0, 0, 0]

def test_compare_negative_scores_incorrect():
    assert compare([-1, -2, -3], [-2, -3, -4]) == [1, 1, 1]

def test_compare_mixed_positive_negative_correct():
    assert compare([1, -2, 3], [1, -2, 3]) == [0, 0, 0]

def test_compare_mixed_positive_negative_incorrect():
    assert compare([1, -2, 3], [2, -1, 4]) == [1, 1, 1]

def test_compare_example_1():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

def test_compare_example_2():
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_large_numbers():
    assert compare([100, 200, 300], [105, 195, 305]) == [5, 5, 5]

def test_compare_large_numbers_correct():
    assert compare([100, 200, 300], [100, 200, 300]) == [0, 0, 0]