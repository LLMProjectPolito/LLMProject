
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

# The function 'compare' is already defined in the environment.
# We are writing the test suite to detect bugs in it.

@pytest.mark.parametrize("game, guess, expected", [
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
])
def test_docstring_examples(game, guess, expected):
    """Verify the function works with the examples provided in the docstring."""
    assert compare(game, guess) == expected

def test_empty_lists():
    """Verify that empty lists return an empty list."""
    assert compare([], []) == []

def test_identical_lists():
    """Verify that identical lists result in a list of zeros."""
    game = [10, 20, 30, 40]
    guess = [10, 20, 30, 40]
    assert compare(game, guess) == [0, 0, 0, 0]

def test_negative_values():
    """Verify absolute difference logic with negative numbers."""
    # -5 - (-2) = -3 -> abs = 3
    # -1 - 5 = -6 -> abs = 6
    # 2 - (-3) = 5 -> abs = 5
    game = [-5, -1, 2]
    guess = [-2, 5, -3]
    assert compare(game, guess) == [3, 6, 5]

def test_single_element():
    """Verify the function works with single-element lists."""
    assert compare([10], [15]) == [5]
    assert compare([10], [10]) == [0]
    assert compare([10], [5]) == [5]

def test_large_integers():
    """Verify the function handles very large integers."""
    game = [10**18, 10**15]
    guess = [10**18 + 50, 10**15 - 50]
    assert compare(game, guess) == [50, 50]

def test_floating_point():
    """Verify the function handles floating point numbers."""
    game = [1.5, 2.0, 3.7]
    guess = [1.0, 2.5, 3.7]
    # Using pytest.approx for float comparisons to avoid precision issues
    result = compare(game, guess)
    assert result == pytest.approx([0.5, 0.5, 0.0])

def test_mismatched_lengths():
    """
    Check behavior when lists are of different lengths.
    Depending on implementation (zip vs range), it might truncate or raise IndexError.
    This test documents the current behavior.
    """
    game = [1, 2, 3]
    guess = [1, 2]
    
    # If the implementation uses zip(), it will truncate to the shortest list.
    # If it uses range(len(game)), it will raise IndexError.
    # We check if it handles it gracefully or raises an error.
    try:
        result = compare(game, guess)
        # If it doesn't crash, it should at least be a list
        assert isinstance(result, list)
    except IndexError:
        # IndexError is also an acceptable outcome for mismatched inputs 
        # given the 'equal length' constraint in the prompt.
        pass