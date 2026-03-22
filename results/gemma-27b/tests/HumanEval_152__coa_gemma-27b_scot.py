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

def test_compare_mixed_correct_incorrect():
    assert compare([1, 2, 3, 4], [1, 5, 3, 0]) == [0, 3, 0, 4]

def test_compare_negative_values():
    assert compare([-1, -2, -3], [-1, -2, -3]) == [0, 0, 0]

def test_compare_negative_and_positive():
    assert compare([-1, 2, -3], [1, -2, 3]) == [2, 4, 6]

def test_compare_zero_values():
    assert compare([0, 0, 0], [1, -1, 0]) == [1, 1, 0]

def test_compare_large_values():
    assert compare([1000, 2000, 3000], [1001, 1999, 3000]) == [1, 1, 0]

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
        result.append(abs(game[i] - guess[i]))
    return result

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function 'compare' calculates the absolute difference between corresponding elements of two lists.
# Equivalence partitioning focuses on dividing the input data into partitions where the function behaves similarly.
# Key partitions: Correct guess (guess == game[i]), Incorrect guess (guess != game[i]).
# Edge cases: Empty lists, lists of different lengths (though the problem statement specifies equal length).

# STEP 2: PLAN - List test functions names and scenarios.
# test_compare_correct_guesses: Tests the scenario where all guesses are correct.
# test_compare_incorrect_guesses: Tests the scenario where all guesses are incorrect.
# test_compare_mixed_guesses: Tests a mix of correct and incorrect guesses.

# STEP 3: CODE - Write the high-quality pytest suite.

def test_compare_correct_guesses():
    game = [1, 2, 3, 4, 5]
    guess = [1, 2, 3, 4, 5]
    expected = [0, 0, 0, 0, 0]
    assert compare(game, guess) == expected

def test_compare_incorrect_guesses():
    game = [1, 2, 3, 4, 5]
    guess = [6, 7, 8, 9, 10]
    expected = [5, 5, 5, 5, 5]
    assert compare(game, guess) == expected

def test_compare_mixed_guesses():
    game = [1, 2, 3, 4, 5]
    guess = [1, 7, 3, 9, 5]
    expected = [0, 5, 0, 5, 0]
    assert compare(game, guess) == expected

# Focus: Error Handling/Invalid Input
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

def test_compare_invalid_input_different_lengths():
    """Test case for when the input lists have different lengths."""
    with pytest.raises(IndexError):
        compare([1, 2, 3], [1, 2])

def test_compare_invalid_input_non_list():
    """Test case for when the input is not a list."""
    with pytest.raises(TypeError):
        compare("123", [1, 2, 3])

def test_compare_invalid_input_list_with_non_numeric():
    """Test case for when the list contains non-numeric values."""
    with pytest.raises(TypeError):
        compare([1, 2, "a"], [1, 2, 3])