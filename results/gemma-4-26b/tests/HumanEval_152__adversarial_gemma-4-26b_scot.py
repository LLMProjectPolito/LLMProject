
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

def test_compare_provided_examples():
    """Verify the examples provided in the docstring."""
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_all_correct():
    """If all guesses are correct, the result should be all zeros."""
    game = [10, 20, 30, 40]
    guess = [10, 20, 30, 40]
    assert compare(game, guess) == [0, 0, 0, 0]

def test_compare_empty_lists():
    """An empty input should return an empty list."""
    assert compare([], []) == []

def test_compare_negative_numbers():
    """Test absolute difference with negative integers."""
    # abs(-5 - (-10)) = 5
    # abs(-5 - 5) = 10
    # abs(5 - (-5)) = 10
    game = [-5, -5, 5]
    guess = [-10, 5, -5]
    assert compare(game, guess) == [5, 10, 10]

def test_compare_single_element():
    """Test the boundary case of a single element."""
    assert compare([100], [90]) == [10]
    assert compare([5], [5]) == [0]

def test_compare_large_numbers():
    """Test with very large integers."""
    large_val = 10**15
    game = [large_val, 0]
    guess = [large_val + 7, 10]
    assert compare(game, guess) == [7, 10]

def test_compare_floats():
    """Test with floating point numbers using approx for precision."""
    game = [1.5, 2.2, 0.0]
    guess = [1.0, 2.5, -0.5]
    expected = [0.5, 0.3, 0.5]
    # We use pytest.approx because float subtraction can lead to precision errors
    result = compare(game, guess)
    assert result == pytest.approx(expected)

@pytest.mark.parametrize("game, guess", [
    ([1, 2], [1, 2, 3]),
    ([1, 2, 3], [1, 2]),
])
def test_compare_mismatched_lengths(game, guess):
    """
    Defensive test: The prompt states arrays are of equal length.
    If they are not, the function should ideally raise an error 
    or we should document the behavior. 
    Assuming standard robust implementation should raise an error.
    """
    with pytest.raises((ValueError, IndexError)):
        compare(game, guess)