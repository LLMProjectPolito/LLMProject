
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

@pytest.mark.parametrize("game, guess, expected", [
    # Examples from docstring
    ([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2], [0, 0, 0, 0, 3, 3]),
    ([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2], [4, 4, 1, 0, 0, 6]),
    # Edge cases: Empty and Single element
    ([], [], []),
    ([10], [10], [0]),
    ([10], [20], [10]),
    ([10], [0], [10]),
    # Logic cases: All correct, all incorrect, and zeros
    ([1, 2, 3], [1, 2, 3], [0, 0, 0]),
    ([-1, -5, 0], [-1, -5, 0], [0, 0, 0]),
    ([1, 2, 3], [4, 5, 6], [3, 3, 3]),
    ([0, 0, 0], [1, 2, 3], [1, 2, 3]),
    ([0, 0, 0], [0, 0, 0], [0, 0, 0]),
    ([0, 0, 0], [1, -1, 0], [1, 1, 0]),
    # Negative numbers and mixed signs
    ([-1, -2], [-1, -2], [0, 0]),
    ([-1, -10], [-5, -2], [4, 8]),
    ([5, -5], [-5, 5], [10, 10]),
    ([1, -1], [0, 0], [1, 1]),
    # Large values
    ([1000000, 0], [0, 1000000], [1000000, 1000000]),
])
def test_compare_scenarios(game, guess, expected):
    """Consolidated tests for standard scenarios and basic edge cases."""
    assert compare(game, guess) == expected

def test_compare_floats():
    """Test handling of floating-point numbers and precision."""
    # Testing precision: 0.3 - 0.1 is often 0.19999999999999998 in binary floating point
    assert compare([0.1, 0.2], [0.3, 0.4]) == pytest.approx([0.2, 0.2])
    assert compare([1.5, -1.5], [2.5, -2.5]) == [1.0, 1.0]

def test_compare_mismatched_lengths():
    """Test that mismatched list lengths raise a ValueError."""
    with pytest.raises(ValueError):
        compare([1, 2, 3], [1, 2])
    with pytest.raises(ValueError):
        compare([1, 2], [1, 2, 3])

def test_compare_invalid_types():
    """Test that non-numeric types or None values raise a TypeError."""
    # Test None values
    with pytest.raises(TypeError):
        compare(None, [1, 2, 3])
    with pytest.raises(TypeError):
        compare([1, 2, 3], None)
    
    # Test non-numeric types within lists
    with pytest.raises(TypeError):
        compare([1, 2, "3"], [1, 2, 3])
    with pytest.raises(TypeError):
        compare([1, 2, 3], [1, 2, "3"])
    with pytest.raises(TypeError):
        compare([1, 2, 3], [1, 2, None])