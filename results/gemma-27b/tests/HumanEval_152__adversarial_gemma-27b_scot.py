
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
        result.append(abs(game[i] - guess[i]))
    return result

def test_empty_lists():
    assert compare([], []) == []

def test_single_element_correct():
    assert compare([5], [5]) == [0]

def test_single_element_incorrect():
    assert compare([5], [2]) == [3]

def test_positive_numbers_all_correct():
    assert compare([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [0, 0, 0, 0, 0]

def test_positive_numbers_some_incorrect():
    assert compare([1, 2, 3, 4, 5], [1, 2, 3, 4, 2]) == [0, 0, 0, 0, 3]

def test_negative_numbers_all_correct():
    assert compare([-1, -2, -3, -4, -5], [-1, -2, -3, -4, -5]) == [0, 0, 0, 0, 0]

def test_negative_numbers_some_incorrect():
    assert compare([-1, -2, -3, -4, -5], [-1, -2, -3, -4, -2]) == [0, 0, 0, 0, 3]

def test_mixed_numbers_all_correct():
    assert compare([-1, 2, -3, 4, -5], [-1, 2, -3, 4, -5]) == [0, 0, 0, 0, 0]

def test_mixed_numbers_some_incorrect():
    assert compare([-1, 2, -3, 4, -5], [-1, 2, -3, 4, -2]) == [0, 0, 0, 0, 3]

def test_large_differences():
    assert compare([1, 2, 3], [100, 200, 300]) == [99, 198, 297]

def test_example_1():
    assert compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) == [0,0,0,0,3,3]

def test_example_2():
    assert compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) == [4,4,1,0,0,6]