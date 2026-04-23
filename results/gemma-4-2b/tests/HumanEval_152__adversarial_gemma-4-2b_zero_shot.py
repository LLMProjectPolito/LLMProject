
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

def test_empty_arrays():
    assert compare([], []) == []

def test_equal_arrays_correct_guesses():
    assert compare([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [0, 0, 0, 0, 0]

def test_equal_arrays_incorrect_guesses():
    assert compare([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == [4, 4, 4, 4, 4]

def test_example_1():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

def test_example_2():
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_mixed_values():
    assert compare([1, 5, 2, 8, 3, 9], [4, 2, 6, 1, 7, 5]) == [1, 3, 4, 7, 4, 4]

def test_negative_values():
    assert compare([-1, -2, -3, -4, -5, -1], [-1, -2, -3, -4, -2, -3]) == [0, 0, 0, 0, 3, 3]

def test_zero_values():
    assert compare([0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0]

def test_single_element_arrays():
    assert compare([5], [5]) == [0]
    assert compare([5], [10]) == [5]
    assert compare([5], [-5]) == [10]