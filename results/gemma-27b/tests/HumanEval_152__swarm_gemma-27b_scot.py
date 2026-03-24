
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

def test_negative_values():
    assert compare([-1, -2, -3], [-1, -2, -3]) == [0, 0, 0]

def test_mixed_positive_negative():
    assert compare([1, -2, 3], [-1, 2, 3]) == [2, 4, 0]

def test_large_differences():
    assert compare([1, 2, 3], [10, -5, 0]) == [9, 7, 3]

def test_zero_values():
    assert compare([0, 0, 0], [1, 2, 3]) == [1, 2, 3]

def test_all_correct():
    assert compare([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [0, 0, 0, 0, 0]

def test_all_incorrect():
    assert compare([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]) == [5, 5, 5, 5, 5]

def test_single_element():
    assert compare([5], [5]) == [0]

def test_single_element_incorrect():
    assert compare([5], [10]) == [5]

def test_large_lists():
    game = list(range(1000))
    guess = [x + 1 for x in range(1000)]
    expected = [1] * 1000
    assert compare(game, guess) == expected

def test_edge_case_max_int():
    game = [2**31 - 1]
    guess = [-2**31]
    assert compare(game, guess) == [2**31 + 1]

def test_edge_case_large_numbers():
    assert compare([1000, 2000, 3000], [1001, 1999, 3000]) == [1, 1, 0]

def test_edge_case_identical_negative_numbers():
    assert compare([-5, -5, -5], [-5, -5, -5]) == [0, 0, 0]

def test_edge_case_one_correct_many_incorrect():
    assert compare([1, 2, 3, 4, 5], [1, 7, 3, 9, 5]) == [0, 5, 0, 5, 0]

def test_edge_case_large_difference():
    assert compare([100], [-100]) == [200]

@pytest.mark.parametrize("game, guess, expected", [
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]),
])
def test_examples(game, guess, expected):
    assert compare(game, guess) == expected