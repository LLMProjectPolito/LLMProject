
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
    If the input lists have different lengths, a ValueError is raised.
    
    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """
    if len(game) != len(guess):
        raise ValueError("Input lists must have the same length.")
    
    result = []
    for i in range(len(game)):
        if not isinstance(game[i], (int, float)) or not isinstance(guess[i], (int, float)):
            raise TypeError("Input lists must contain only numbers.")
        result.append(abs(game[i] - guess[i]))
    return result

def test_empty_lists():
    assert compare([], []) == []

def test_incorrect_guesses():
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_mixed_guesses():
    assert compare([1, 2, 3, 4, 5], [1, 2, 0, 4, 2]) == [0, 0, 3, 0, 3]

def test_negative_and_zero_values():
    assert compare([-1, 0, 1], [-1, 0, 1]) == [0, 0, 0]
    assert compare([-1, 0, 1], [1, -1, 2]) == [2, 1, 1]
    assert compare([0, -1, 0], [1, 0, -1]) == [1, 1, 1]

def test_large_numbers():
    assert compare([1000, 2000, 3000], [-1000, -2000, -3000]) == [2000, 4000, 6000]

def test_single_element_lists():
    assert compare([5], [5]) == [0]
    assert compare([5], [10]) == [5]

def test_positive_negative_differences():
    assert compare([1, -2, 3], [-1, 2, -3]) == [2, 4, 6]
    assert compare([-1, 2, -3], [1, -2, 3]) == [2, 4, 6]

def test_mixed_positive_negative_zero():
    assert compare([1, -2, 0, 5], [-1, 2, 1, -5]) == [2, 4, 1, 10]

def test_different_lengths():
    with pytest.raises(ValueError):
        compare([1, 2], [1, 2, 3])

def test_non_numeric_input():
    with pytest.raises(TypeError):
        compare([1, 2, "a"], [1, 2, 3])