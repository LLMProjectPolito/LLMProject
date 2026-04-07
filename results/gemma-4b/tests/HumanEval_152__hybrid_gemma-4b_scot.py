
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
# The function `compare` takes two lists, `game` and `guess`, as input. It calculates the absolute difference between each element in `guess` and the corresponding element in `game`. It returns a new list containing these absolute differences.
# The function should handle cases where the guess is correct (difference is 0) and where the guess is incorrect (difference is the absolute value of the difference).
# Edge cases to consider: empty lists, lists of different lengths (although the problem states they are equal length, it's good to consider).

# STEP 2: PLAN
# Test cases:
# 1. Correct guesses: [1, 2, 3, 4, 5, 1] vs [1, 2, 3, 4, 2, -2]
# 2. Mixed correct and incorrect guesses: [0, 5, 0, 0, 0, 4] vs [4, 1, 1, 0, 0, -2]
# 3. All incorrect guesses: [1, 2, 3, 4, 5, 1] vs [5, 6, 7, 8, 9, 10]
# 4. Empty lists: [] vs []
# 5. Single element lists: [1] vs [1]
# 6. Single element correct guess: [1] vs [1]
# 7. Single element incorrect guess: [1] vs [2]

# Test function names:
# test_correct_guesses
# test_mixed_guesses
# test_all_incorrect_guesses
# test_empty_lists
# test_single_element_lists
# test_single_element_correct_guess
# test_single_element_incorrect_guess


# STEP 3: CODE
def test_correct_guesses():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

def test_mixed_guesses():
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_all_incorrect_guesses():
    assert compare([1, 2, 3, 4, 5, 1], [5, 6, 7, 8, 9, 10]) == [4, 4, 4, 4, 4, 4]

def test_empty_lists():
    assert compare([], []) == []

def test_single_element_lists():
    assert compare([1], [1]) == [0]

def test_single_element_correct_guess():
    assert compare([1], [1]) == [0]

def test_single_element_incorrect_guess():
    assert compare([1], [2]) == [1]