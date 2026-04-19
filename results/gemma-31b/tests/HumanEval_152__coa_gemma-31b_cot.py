
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

def test_compare_single_element_zero():
    assert compare([0], [0]) == [0]

def test_compare_extreme_boundaries():
    assert compare([1000000], [-1000000]) == [2000000]

# Focus: Type Scenarios
import pytest

def test_compare_floats():
    """Test the function with floating point numbers to ensure type compatibility."""
    assert compare([1.5, 2.0, 3.5], [1.0, 2.0, 4.0]) == [0.5, 0.0, 0.5]

def test_compare_empty_lists():
    """Test the function with empty lists to ensure it handles the base case of the list type."""
    assert compare([], []) == []

def test_compare_mixed_numeric_types():
    """Test the function with a mix of integers and floats."""
    assert compare([1, 2.5], [1.5, 2]) == [0.5, 0.5]

# Focus: Logic Branches
import pytest

def test_compare_exact_matches():
    # Branch: game[i] == guess[i]
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_compare_mixed_branches():
    # Branch: game[i] > guess[i] and game[i] < guess[i]
    assert compare([10, 5], [2, 8]) == [8, 3]

def test_compare_negative_logic():
    # Branch: Absolute difference with negative numbers
    assert compare([-1, -5, 0], [1, -10, -2]) == [2, 5, 2]