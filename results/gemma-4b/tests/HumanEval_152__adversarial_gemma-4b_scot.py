
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
# The function `compare` takes two lists, `game` and `guess`, as input. It calculates the absolute difference between each corresponding element in the two lists and returns a new list containing these differences.
# The goal is to test the function with various inputs, including edge cases like empty lists, lists with different lengths (though the problem description states they should be equal), and lists with both correct and incorrect guesses.
# Constraints: The input lists are assumed to be of equal length. The function should handle negative and positive differences correctly.

# STEP 2: PLAN
# Test cases:
# 1. Basic test case with correct guesses.
# 2. Test case with some incorrect guesses.
# 3. Test case with all incorrect guesses.
# 4. Test case with empty lists (although the problem states they are equal length, it's good to test).
# 5. Test case with a single element in both lists.
# 6. Test case with negative numbers in the lists.

# Test function names:
# test_compare_correct_guesses
# test_compare_incorrect_guesses
# test_compare_all_incorrect
# test_compare_empty_lists
# test_compare_single_element
# test_compare_negative_numbers

# STEP 3: CODE
def test_compare_correct_guesses():
    assert compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) == [0,0,0,0,3,3]

def test_compare_incorrect_guesses():
    assert compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) == [4,4,1,0,0,6]

def test_compare_all_incorrect():
    assert compare([1,2,3,4,5,1],[5,4,3,2,1,0]) == [4,2,0,0,0,6]

def test_compare_empty_lists():
    assert compare([], []) == []

def test_compare_single_element():
    assert compare([5], [5]) == [0]
    assert compare([5], [6]) == [1]

def test_compare_negative_numbers():
    assert compare([-1, -2, -3], [-1, -2, -3]) == [0, 0, 0]
    assert compare([-1, -2, -3], [-4, -1, -2]) == [3, 1, 1]