import pytest
import math


# Focus: Boundary Values
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

def test_compare_empty_lists():
    assert compare([], []) == []

def test_compare_all_correct():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_compare_all_incorrect():
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_compare_mixed():
    assert compare([1, 2, 3, 4, 5], [1, 2, 0, 4, 6]) == [0, 0, 3, 0, 1]

def test_compare_negative_values():
    assert compare([-1, -2, -3], [-1, -2, -3]) == [0, 0, 0]

def test_compare_negative_and_positive():
    assert compare([-1, 2, -3], [1, -2, 3]) == [2, 4, 6]

def test_compare_zero_values():
    assert compare([0, 0, 0], [1, -1, 0]) == [1, 1, 0]

# Focus: Equivalence Partitioning
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

def test_equivalence_partitioning_correct_guesses():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_equivalence_partitioning_incorrect_guesses():
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_equivalence_partitioning_mixed_guesses():
    assert compare([1, 2, 3, 4, 5], [1, 2, 0, 4, 2]) == [0, 0, 3, 0, 3]

# Focus: Error Handling/Invalid Input
import pytest

def test_compare_invalid_input_different_lengths():
    """Test case for when the input lists have different lengths."""
    with pytest.raises(ValueError):
        compare([1, 2, 3], [1, 2])

def test_compare_invalid_input_non_list():
    """Test case for when the input is not a list."""
    with pytest.raises(TypeError):
        compare("123", [1, 2, 3])
    with pytest.raises(TypeError):
        compare([1, 2, 3], "123")

def test_compare_invalid_input_non_numeric():
    """Test case for when the input list contains non-numeric values."""
    with pytest.raises(TypeError):
        compare([1, 2, "a"], [1, 2, 3])
    with pytest.raises(TypeError):
        compare([1, 2, 3], [1, 2, "a"])