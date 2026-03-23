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

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `compare` takes two lists, `game` and `guess`, as input.
# It calculates the absolute difference between each corresponding element in the two lists.
# It returns a new list containing these absolute differences.
# If the guess is correct for a particular match, the difference is 0.
# The function should handle lists of any length.
# Edge cases: empty lists, lists of length 1, lists with identical values, lists with large differences.

# STEP 2: PLAN - List test functions names and scenarios.
# test_compare_empty_lists
# test_compare_equal_lists
# test_compare_identical_lists
# test_compare_mixed_lists
# test_compare_single_element_lists
# test_compare_large_differences
# test_compare_zero_differences

# STEP 3: CODE - Write the high-quality pytest suite.
def test_compare_empty_lists():
    assert compare([], []) == []

def test_compare_equal_lists():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_compare_identical_lists():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_compare_mixed_lists():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_single_element_lists():
    assert compare([5], [5]) == [0]
    assert compare([5], [6]) == [1]

def test_compare_large_differences():
    assert compare([1, 2, 3], [1, 100, 3]) == [0, 98, 0]
    assert compare([100, 2, 3], [1, 100, 3]) == [99, 0, 0]

def test_compare_zero_differences():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]