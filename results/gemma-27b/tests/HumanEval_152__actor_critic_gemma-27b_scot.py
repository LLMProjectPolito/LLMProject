
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
    
    Note: The function assumes that the input lists `game` and `guess` have the same length.
    Behavior with lists of different lengths is undefined.
    Be aware that very large numbers may cause integer overflow depending on the language's integer representation.
    
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

def test_all_correct_guesses():
    assert compare([1, 2, 3, 1000, 2000, 3000], [1, 2, 3, 1000, 2000, 3000]) == [0, 0, 0, 0, 0, 0]

def test_incorrect_guesses():
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_mixed_guesses():
    assert compare([1, 2, 3, 4, 5], [1, 2, 0, 4, 2]) == [0, 0, 3, 0, 3]

def test_mixed_signs():
    assert compare([-1, -2, -3, -4, -5], [-1, 2, -3, 4, -5]) == [0, 4, 0, 8, 0]

def test_zero_values():
    assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]

def test_large_differences():
    assert compare([1, 2, 3], [-1000, 1000, -1000]) == [1001, 998, 1003]

def test_large_list():
    game = list(range(100))
    guess = [x + 1 for x in range(100)]
    expected = [1] * 100
    assert compare(game, guess) == expected

def test_single_element_lists():
    assert compare([5], [5]) == [0]
    assert compare([5], [10]) == [5]

def test_large_numbers():
    assert compare([2**31 - 1, 2**31 - 1], [2**31 - 1, 2**31 - 1]) == [0, 0]
    assert compare([2**31 - 1, 2**31 - 1], [0, 0]) == [2**31 - 1, 2**31 - 1]

def test_mixed_large_numbers():
    assert compare([2**30, -2**30, 2**29], [-2**30, 2**30, -2**29]) == [2**31, 2**31, 2**30]