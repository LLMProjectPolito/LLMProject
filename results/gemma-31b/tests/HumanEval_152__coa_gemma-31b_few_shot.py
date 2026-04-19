
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

def test_compare_single_element():
    assert compare([10], [20]) == [10]
    assert compare([5], [5]) == [0]

def test_compare_extreme_values():
    assert compare([10**9], [-10**9]) == [2 * 10**9]
    assert compare([0], [0]) == [0]

# Focus: Type Scenarios
import pytest

def test_compare_floats():
    assert compare([1.5, 2.0, 3.5], [1.0, 2.0, 4.0]) == [0.5, 0.0, 0.5]

def test_compare_empty_lists():
    assert compare([], []) == []

# Focus: Logic Branches
import pytest

def test_compare_logic_branches():
    # Branch 1: Exact matches (result 0)
    # Branch 2: Guess is lower than score (positive difference)
    # Branch 3: Guess is higher than score (positive difference)
    # Branch 4: Handling negative values
    assert compare([10, 20, 30, 5], [10, 15, 35, -5]) == [0, 5, 5, 10]

def test_compare_all_incorrect():
    # Testing branch where no guesses are correct
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_compare_all_correct():
    # Testing branch where all guesses are correct
    assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]