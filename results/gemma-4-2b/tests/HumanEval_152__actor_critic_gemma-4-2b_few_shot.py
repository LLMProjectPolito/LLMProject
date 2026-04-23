
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

def test_compare_basic():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]
    assert compare([1, 2, 3], [1, 2, 4]) == [0, 0, 1]

def test_compare_empty():
    assert compare([], []) == []
    assert compare([1], []) == []
    assert compare([], [1]) == []

def test_compare_single_element():
    assert compare([5], [5]) == [0]
    assert compare([5], [10]) == [5]
    assert compare([5], [-5]) == [10]

def test_compare_all_zeros():
    assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]
    assert compare([0, 0, 0], [1, 2, 3]) == [0, 0, 0]
    assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]

def test_compare_negative_numbers():
    assert compare([-1, -2, -3], [-1, -2, -3]) == [0, 0, 0]
    assert compare([-1, -2, -3], [-4, -5, -6]) == [3, 3, 3]
    assert compare([-1, -2, -3], [-1, -2, -3]) == [0, 0, 0]

def test_compare_mixed_positive_negative():
    assert compare([1, -2, 3], [1, -2, 3]) == [0, 0, 0]
    assert compare([1, -2, 3], [4, -5, 6]) == [3, 3, 3]
    assert compare([1, -2, 3], [1, -2, 3]) == [0, 0, 0]

def test_compare_large_numbers():
    assert compare([1000000, 2000000, 3000000], [1000000, 2000000, 3000000]) == [0, 0, 0]
    assert compare([1000000, 2000000, 3000000], [1000001, 2000001, 3000001]) == [1, 1, 1]
    assert compare([1000000, 2000000, 3000000], [1000000, 2000000, 3000000]) == [0, 0, 0]