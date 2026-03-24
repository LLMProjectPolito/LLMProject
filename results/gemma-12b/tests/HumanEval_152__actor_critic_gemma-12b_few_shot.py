
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
    Compares two lists of numbers (scores and guesses) and returns a list
    indicating the difference between each guess and the corresponding score.

    Args:
        game (list[float | int]): A list of numbers representing the actual scores.
        guess (list[float | int]): A list of numbers representing the guesses.

    Returns:
        list[float | int]: A list of the same length as the inputs, where each
                           element represents the absolute difference between the
                           corresponding score and guess.  If the guess is correct,
                           the value is 0.

    Raises:
        TypeError: If either input is not a list, or if any element within the lists
                   is not a number (int or float).
        ValueError: If the input lists have different lengths.

    Examples:
        compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
        compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]
        compare([1.5, 2.0, 3.5], [1, 2, 4]) == [0.5, 0.0, 0.5]
    """

    # Type and Length Validation
    if not isinstance(game, list) or not isinstance(guess, list):
        raise TypeError("Inputs must be lists.")

    if len(game) != len(guess):
        raise ValueError("Input lists must have the same length.")

    for items in [game, guess]:
        for item in items:
            if not isinstance(item, (int, float)):
                raise TypeError("All elements in the lists must be numbers (int or float).")

    result = []
    for g, s in zip(game, guess):
        if g == s:
            result.append(0)
        else:
            result.append(abs(g - s))
    return result


### Tests (Pytest):
def test_compare_basic():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_floats():
    assert compare([1.5, 2.0, 3.5], [1, 2, 4]) == [0.5, 0.0, 0.5]

def test_compare_empty():
    assert compare([], []) == []

def test_compare_type_error():
    with pytest.raises(TypeError):
        compare([1, 2, 3], "not a list")
    with pytest.raises(TypeError):
        compare([1, 2, "a"], [1, 2, 3])

def test_compare_value_error():
    with pytest.raises(ValueError):
        compare([1, 2, 3], [1, 2])

def test_compare_negative_numbers():
    assert compare([-1, -2, -3], [-1, -2, -4]) == [0, 0, 1]

def test_compare_mixed_types():
    assert compare([1, 2.0, 3], [1.0, 2, 3.0]) == [0.0, 0.0, 0.0]