
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
        if game[i] == guess[i]:
            result.append(0)
        else:
            result.append(abs(game[i] - guess[i]))
    return result

# STEP 1: REASONING
# The function `compare` takes two lists, `game` and `guess`, as input and returns a new list.
# The new list contains the absolute difference between the corresponding elements of `game` and `guess` if they are not equal,
# and 0 if they are equal.
# We need to test the following scenarios:
# 1. Empty lists
# 2. Lists with equal elements
# 3. Lists with different elements
# 4. Lists with negative elements
# 5. Lists with zero elements

# STEP 2: PLAN
# Test functions:
# - test_empty_lists: Test with empty lists as input.
# - test_equal_lists: Test with lists containing equal elements.
# - test_different_lists: Test with lists containing different elements.
# - test_negative_elements: Test with lists containing negative elements.
# - test_zero_elements: Test with lists containing zero elements.
# - test_mixed_elements: Test with lists containing a mix of positive, negative, and zero elements.
# - test_example_1: Test with the first example provided in the problem description.
# - test_example_2: Test with the second example provided in the problem description.

# STEP 3: CODE
class TestCompare:
    def test_empty_lists(self):
        assert compare([], []) == []

    def test_equal_lists(self):
        assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    def test_different_lists(self):
        assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    def test_negative_elements(self):
        assert compare([-1, -2, -3], [-4, -5, -6]) == [3, 3, 3]

    def test_zero_elements(self):
        assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]

    def test_mixed_elements(self):
        assert compare([1, -2, 0], [4, -5, 2]) == [3, 3, 2]

    def test_example_1(self):
        assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

    def test_example_2(self):
        assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]