
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

def compare(game, guess):
    """
    Compares two arrays of scores and guesses, returning an array indicating the difference between each guess and the score.

    Args:
        game (list[int]): The array of actual scores.
        guess (list[int]): The array of guessed scores.

    Returns:
        list[int]: An array of the same length as the input arrays, where each element represents the absolute difference
                   between the corresponding score and guess. If the guess is correct, the value is 0.
                   Returns an empty list if either input array is empty.
                   Raises ValueError if the input arrays are not of equal length.

    Raises:
        ValueError: If the input arrays `game` and `guess` have different lengths.
    """

    if len(game) != len(guess):
        raise ValueError("Input arrays must be of equal length.")

    return [0 if game[i] == guess[i] else abs(game[i] - guess[i]) for i in range(len(game))]


### Tests (Pytest):
def test_compare_basic():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_empty_arrays():
    assert compare([], []) == []

def test_compare_unequal_length_arrays():
    with pytest.raises(ValueError) as excinfo:
        compare([1, 2, 3], [1, 2])
    assert str(excinfo.value) == "Input arrays must be of equal length."

def test_compare_all_correct():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_compare_all_incorrect():
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_compare_negative_numbers():
    assert compare([-1, -2, -3], [-1, -2, -4]) == [0, 0, 1]

def test_compare_zero_values():
    assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]

def test_compare_single_element_arrays():
    assert compare([5], [5]) == [0]
    assert compare([5], [6]) == [1]