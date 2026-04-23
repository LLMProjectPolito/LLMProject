
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
    Note: If the input lists are not of equal length, a ValueError is raised.
    """
    if len(game) != len(guess):
        raise ValueError("Input lists must have the same length.")
    result = []
    for i in range(len(game)):
        if game[i] == guess[i]:
            result.append(0)
        else:
            result.append(abs(game[i] - guess[i]))
    return result

def test_compare_example1():
    assert compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) == [0,0,0,0,3,3]

def test_compare_example2():
    assert compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) == [4,4,1,0,0,6]

def test_compare_with_empty_lists():
    assert compare([], []) == []

def test_compare_with_single_element():
    assert compare([5], [5]) == [0]
    assert compare([5], [2]) == [3]

def test_compare_with_mixed_elements():
    assert compare([1, 2, 3, 4], [1, 5, 3, 2]) == [0, 3, 0, 2]

def test_negative_numbers():
    assert compare([-1, -2, -3], [-1, -2, -4]) == [0, 0, 1]

def test_zero_values():
    assert compare([0, 0, 0], [1, 2, 3]) == [1, 2, 3]

def test_large_numbers():
    assert compare([1000, 2000, 3000], [1001, 1999, 3000]) == [1, 1, 0]

def test_different_signs():
    assert compare([10, -5, 0], [-10, 5, 0]) == [20, 10, 0]

def test_large_list():
    game = list(range(1000))
    guess = [x + 1 for x in range(1000)]
    assert compare(game, guess)[:10] == [1] * 10
    assert compare(game, guess)[990:] == [1] * 10

def test_different_lengths():
    with pytest.raises(ValueError) as excinfo:
        compare([1, 2], [1, 2, 3])
    assert str(excinfo.value) == "Input lists must have the same length."

def test_very_large_difference():
    assert compare([1, 2], [1000, 2000]) == [999, 1998]