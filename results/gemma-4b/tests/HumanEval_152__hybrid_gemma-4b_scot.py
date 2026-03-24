
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

# STEP 1: REASONING
# The function `compare` takes two lists, `game` and `guess`, as input. It calculates the absolute difference between each corresponding element in the two lists and returns a new list containing these differences. If the guess is correct for a particular match, the difference should be 0.
# We need to test various scenarios including:
# 1. Correct guesses: All guesses are correct.
# 2. Mixed correct and incorrect guesses: Some guesses are correct, some are incorrect.
# 3. All incorrect guesses: All guesses are incorrect.
# 4. Empty lists: Handle the case where either or both input lists are empty. (Although the problem description doesn't explicitly state this, it's good practice to consider edge cases).
# 5. Lists of different lengths:  The problem description states that the lists are of equal length, but it's good to test this assumption.

# STEP 2: PLAN
# Test functions:
# - test_correct_guesses: Tests the case where all guesses are correct.
# - test_mixed_guesses: Tests the case where some guesses are correct and some are incorrect.
# - test_all_incorrect_guesses: Tests the case where all guesses are incorrect.
# - test_empty_lists: Tests the case where both lists are empty.
# - test_unequal_lengths: Tests the case where the lists have different lengths (should raise an error).

# STEP 3: CODE
#
def test_correct_guesses():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_mixed_guesses():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_all_incorrect_guesses():
    assert compare([1, 2, 3, 4, 5, 1], [5, 6, 7, 8, 9, 10]) == [4, 4, 4, 4, 4, 9]

def test_empty_lists():
    assert compare([], []) == []

def test_unequal_lengths():
    with pytest.raises(IndexError):
        compare([1, 2, 3], [1, 2])