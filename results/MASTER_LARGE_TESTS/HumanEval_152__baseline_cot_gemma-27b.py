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

def test_basic_cases():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_empty_input():
    assert compare([], []) == []

def test_single_element():
    assert compare([5], [5]) == [0]
    assert compare([5], [10]) == [5]

def test_all_correct_guesses():
    assert compare([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [0, 0, 0, 0, 0]

def test_all_incorrect_guesses():
    assert compare([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]) == [5, 5, 5, 5, 5]

def test_mixed_correct_and_incorrect():
    assert compare([1, 2, 3, 4, 5], [1, 2, 5, 4, 0]) == [0, 0, 2, 0, 5]

def test_large_numbers():
    assert compare([1000, 2000, 3000], [1000, 2001, 2999]) == [0, 1, 1]

def test_negative_numbers():
    assert compare([-1, -2, -3], [-1, -2, -5]) == [0, 0, 2]
    assert compare([-1, 2, -3], [1, -2, 3]) == [2, 4, 6]

def test_zero_values():
    assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]
    assert compare([0, 0, 0], [1, 2, 3]) == [1, 2, 3]

def test_different_lengths():
    with pytest.raises(IndexError):
        compare([1, 2], [1])
    with pytest.raises(IndexError):
        compare([1], [1, 2])