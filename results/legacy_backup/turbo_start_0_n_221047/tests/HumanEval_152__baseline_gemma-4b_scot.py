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
# The function `compare` takes two lists, `game` and `guess`, as input. It calculates the absolute difference between each corresponding element in the two lists and returns a new list containing these differences. If the guess is correct for a particular match, the difference will be 0.
# We need to test various scenarios including correct guesses, incorrect guesses with small and large differences, and edge cases like empty lists (although the problem description doesn't explicitly mention this, it's good practice to consider).

# STEP 2: PLAN
# Test cases:
# 1. Correct guesses: [1, 2, 3, 4, 5, 1] vs [1, 2, 3, 4, 5, 1]
# 2. Correct guesses with some off by one: [0, 5, 0, 0, 0, 4] vs [4, 1, 1, 0, 0, -2]
# 3. Incorrect guesses with small differences: [1, 2, 3, 4, 5, 1] vs [1, 2, 3, 4, 2, -2]
# 4. Incorrect guesses with large differences: [1, 2, 3, 4, 5, 1] vs [1, 2, 3, 4, 6, -2]
# 5.  Edge case:  Empty lists (although not explicitly required, good to check)

# Test function names: test_compare_correct, test_compare_correct_off_by_one, test_compare_incorrect_small, test_compare_incorrect_large

# STEP 3: CODE
def test_compare_correct():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 5, 1]) == [0, 0, 0, 0, 0, 0]

def test_compare_correct_off_by_one():
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_incorrect_small():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

def test_compare_incorrect_large():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 6, -2]) == [0, 0, 0, 0, 1, 4]

def test_compare_empty_lists():
    assert compare([], []) == []