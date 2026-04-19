
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
import math


# Focus: Boundary Values
import pytest

def test_compare_empty_lists():
    assert compare([], []) == []

def test_compare_single_element_zero_diff():
    assert compare([0], [0]) == [0]

def test_compare_extreme_values():
    assert compare([10**9, -10**9], [-10**9, 10**9]) == [2 * 10**9, 2 * 10**9]

# Focus: Type Scenarios
import pytest

def test_compare_empty_lists():
    """Test with empty lists to ensure the function handles empty input types correctly."""
    assert compare([], []) == []

def test_compare_floats():
    """Test with floating point numbers to ensure type compatibility with non-integers."""
    assert compare([1.5, 2.5, 3.0], [1.0, 3.0, 3.0]) == [0.5, 0.5, 0.0]

def test_compare_mixed_numeric_types():
    """Test with a mix of integers and floats."""
    assert compare([1, 2.5], [1.5, 2]) == [0.5, 0.5]

# Focus: Value Scenarios
import pytest

def test_compare_identical_values():
    assert compare([10, 20, 30], [10, 20, 30]) == [0, 0, 0]

def test_compare_negative_and_positive_values():
    assert compare([-1, -5, 0], [1, -10, 5]) == [2, 5, 5]

def test_compare_large_differences():
    assert compare([1000, -1000], [-1000, 1000]) == [2000, 2000]