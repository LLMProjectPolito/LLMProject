
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

# The function is assumed to be available in the namespace.
# Since the prompt forbids redefining it, we assume it is imported or defined above.

@pytest.mark.parametrize("game, guess, expected", [
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
])
def test_compare_docstring_examples(game, guess, expected):
    """Tests the specific examples provided in the docstring."""
    assert compare(game, guess) == expected

def test_compare_empty():
    """Tests that empty lists return an empty list."""
    assert compare([], []) == []

def test_compare_single_element():
    """Tests lists containing only one element."""
    assert compare([10], [7]) == [3]
    assert compare([5], [5]) == [0]
    assert compare([5], [10]) == [5]

def test_compare_identical():
    """Tests that identical lists result in all zeros."""
    game = [10, 20, 30, 40]
    guess = [10, 20, 30, 40]
    assert compare(game, guess) == [0, 0, 0, 0]

def test_compare_negative_values():
    """Tests the absolute difference logic with negative numbers."""
    # Case 1: Both negative
    # |-5 - (-2)| = |-3| = 3
    # |-10 - (-10)| = 0
    assert compare([-5, -10], [-2, -10]) == [3, 0]
    
    # Case 2: One negative, one positive
    # |5 - (-5)| = 10
    # |-5 - 5| = 10
    assert compare([5, -5], [-5, 5]) == [10, 10]

def test_compare_all_zeros():
    """Tests behavior when inputs consist entirely of zeros."""
    assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]
    assert compare([0, 0, 0], [1, 2, 3]) == [1, 2, 3]

def test_compare_large_integers():
    """Tests the function with large integer values."""
    large_val = 10**12
    assert compare([large_val, 0], [0, large_val]) == [large_val, large_val]

def test_compare_alternating_signs():
    """Tests a mix of positive, negative, and zero values."""
    game = [1, -1, 0, 5]
    guess = [-1, 1, 0, -5]
    # |1 - (-1)| = 2
    # |-1 - 1| = 2
    # |0 - 0| = 0
    # |5 - (-5)| = 10
    assert compare(game, guess) == [2, 2, 0, 10]