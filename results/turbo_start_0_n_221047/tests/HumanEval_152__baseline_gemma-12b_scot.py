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
# 1. Both lists are empty.
# 2. Both lists have one element, and they are equal.
# 3. Both lists have one element, and they are not equal.
# 4. Both lists have multiple elements, and some are equal and some are not.
# 5. Both lists have multiple elements, and all are equal.
# 6. Both lists have multiple elements, and all are not equal.
# 7. One of the lists is empty, and the other is not. (Should raise an error)
# 8. Lists have different lengths. (Should raise an error)

# STEP 2: PLAN
# Test functions:
# - test_empty_lists: Both lists are empty.
# - test_single_equal: Both lists have one element, and they are equal.
# - test_single_not_equal: Both lists have one element, and they are not equal.
# - test_multiple_mixed: Both lists have multiple elements, and some are equal and some are not.
# - test_multiple_all_equal: Both lists have multiple elements, and all are equal.
# - test_multiple_all_not_equal: Both lists have multiple elements, and all are not equal.
# - test_different_lengths: Lists have different lengths.
# - test_one_list_empty: One of the lists is empty, and the other is not.

# STEP 3: CODE
class TestCompare:
    def test_empty_lists(self):
        assert compare([], []) == []

    def test_single_equal(self):
        assert compare([5], [5]) == [0]

    def test_single_not_equal(self):
        assert compare([5], [6]) == [1]

    def test_multiple_mixed(self):
        assert compare([1, 2, 3, 4, 5], [1, 2, 4, 4, 2]) == [0, 0, 1, 0, 3]

    def test_multiple_all_equal(self):
        assert compare([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [0, 0, 0, 0, 0]

    def test_multiple_all_not_equal(self):
        assert compare([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]) == [5, 5, 5, 5, 5]

    def test_different_lengths(self):
        with pytest.raises(IndexError):
            compare([1, 2, 3], [1, 2])

    def test_one_list_empty(self):
        with pytest.raises(IndexError):
            compare([1, 2, 3], [])