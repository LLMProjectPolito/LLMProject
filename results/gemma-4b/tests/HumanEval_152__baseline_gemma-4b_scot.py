
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
        result.append(abs(guess[i] - game[i]))
    return result

### SCoT Steps:

### STEP 1: REASONING
# The function `compare` takes two lists, `game` and `guess`, as input.
# It calculates the absolute difference between each element in `guess` and the corresponding element in `game`.
# It returns a new list containing these absolute differences.
# The goal is to test the function with various inputs to ensure it produces the correct output.
# We need to consider cases where the guesses are correct (difference of 0), and cases where they are incorrect.
# We should test with different lengths of lists and different values in the lists.

### STEP 2: PLAN
# Test cases:
# 1. Correct guesses: [1, 2, 3, 4, 5, 1] vs [1, 2, 3, 4, 2, -2]
# 2. Incorrect guesses: [0, 5, 0, 0, 0, 4] vs [4, 1, 1, 0, 0, -2]
# 3. Empty lists: [] vs []
# 4. Single element lists: [1] vs [1]
# 5. Mixed correct and incorrect: [1, 2, 3, 4, 5, 1] vs [1, 2, 3, 4, 6, 1]
# 6. Negative values: [1, -2, 3, -4, 5, -1] vs [1, -2, 3, -4, 5, -1]

### STEP 3: CODE
def test_compare_correct_guesses():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

def test_compare_incorrect_guesses():
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_empty_lists():
    assert compare([], []) == []

def test_compare_single_element_lists():
    assert compare([1], [1]) == [0]

def test_compare_mixed_correct_incorrect():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 6, 1]) == [0, 0, 0, 0, 1, 0]

def test_compare_negative_values():
    assert compare([1, -2, 3, -4, 5, -1], [1, -2, 3, -4, 5, -1]) == [0, 0, 0, 0, 0, 0]

def test_compare_different_lengths():
    with pytest.raises(IndexError):
        compare([1, 2, 3], [1, 2])