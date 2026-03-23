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
    if len(game) != len(guess):
        raise ValueError("Input lists must have the same length.")
    result = []
    for i in range(len(game)):
        result.append(abs(game[i] - guess[i]))
    return result

def test_correct_guesses():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_all_incorrect_guesses():
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_mixed_guesses():
    assert compare([1, 2, 3, 4, 5], [1, 4, 3, 0, 5]) == [0, 2, 0, 4, 0]

def test_empty_lists():
    assert compare([], []) == []

def test_negative_numbers():
    assert compare([-1, -2, -3], [-1, 0, -4]) == [0, 2, 1]

def test_zero_values():
    assert compare([0, 0, 0], [0, 1, 2]) == [0, 1, 2]

def test_different_lengths():
    with pytest.raises(ValueError):
        compare([1, 2], [1, 2, 3])