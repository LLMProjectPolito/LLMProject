
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
# The function `compare` takes two lists, `game` and `guess`, as input. It calculates the absolute difference between each element in `guess` and the corresponding element in `game`. The result is a new list containing these absolute differences. If the guess is correct at a particular index, the difference will be 0.
# We need to test various scenarios including correct guesses, incorrect guesses with small and large differences, and edge cases like empty lists (although the problem description doesn't explicitly mention this, it's good practice to consider).

# STEP 2: PLAN
# Test cases:
# 1. Correct guesses: [1, 2, 3, 4, 5, 1] vs [1, 2, 3, 4, 2, -2]
# 2. Incorrect guesses with small differences: [0, 5, 0, 0, 0, 4] vs [4, 1, 1, 0, 0, -2]
# 3. Incorrect guesses with large differences: [1, 2, 3, 4, 5, 1] vs [1, 2, 3, 4, 6, 1]
# 4. Single element lists: [1] vs [1]
# 5. Single element lists with incorrect guess: [1] vs [2]
# 6. Lists with negative numbers: [1, -2, 3] vs [-1, 2, 3]

# Test function names: test_compare_correct, test_compare_incorrect_small, test_compare_incorrect_large, test_compare_single_element, test_compare_negative_numbers

# STEP 3: CODE
def test_compare_correct():
    assert compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) == [0,0,0,0,3,3]

def test_compare_incorrect_small():
    assert compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) == [4,4,1,0,0,6]

def test_compare_incorrect_large():
    assert compare([1,2,3,4,5,1],[1,2,3,4,6,1]) == [0,0,0,0,2,0]

def test_compare_single_element():
    assert compare([1],[1]) == [0]

def test_compare_single_element_incorrect():
    assert compare([1],[2]) == [1]

def test_compare_negative_numbers():
    assert compare([1, -2, 3], [-1, 2, 3]) == [0, 3, 0]