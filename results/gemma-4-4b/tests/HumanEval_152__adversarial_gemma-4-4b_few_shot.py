
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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

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
        result.append(abs(guess[i] - game[i]))
    return result



@pytest.mark.parametrize(
    "game, guess, expected",
    [
        ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
        ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
        ([1, 2, 3], [1, 2, 3], [0, 0, 0]),
        ([5, 4, 3, 2, 1], [5, 4, 3, 2, 1], [0, 0, 0, 0, 0]),
        ([10, 20, 30], [5, 15, 25], [5, 5, 5]),
        ([1, 1, 1], [1, 1, 1], [0, 0, 0]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 1, 1, 1, 1]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [0, 0, 0, 0, 0]),
        ([1], [1], [0]),
        ([1], [2], [1]),
        ([1], [0], [1]),
        ([], [], []), #Test empty lists
        ([1,2], [3,4], [2,2])
    ],
)
def test_compare_valid_cases(game, guess, expected):
    assert compare(game, guess) == expected

@pytest.mark.parametrize(
    "game, guess, expected",
    [
        ([1, 2, 3, 4, 5, 1], [], []), #Test empty guess list
        ([], [1,2,3], []), #Test empty game list
        ([], [], []) #Test empty lists
    ],
)
def test_compare_empty_lists(game, guess, expected):
    assert compare(game, guess) == expected