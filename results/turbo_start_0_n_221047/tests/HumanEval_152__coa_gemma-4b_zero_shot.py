import pytest
import math


# Focus: Boundary Values
import pytest

def test_compare_perfect_guess():
    assert compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) == [0,0,0,0,3,3]

def test_compare_some_off():
    assert compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) == [4,4,1,0,0,6]

def test_compare_all_off():
    assert compare([1,2,3,4,5,1],[5,6,7,8,9,10]) == [4,4,4,4,4,9]

# Focus: Type Scenarios
import pytest

def test_type_scenario_correct_guess():
    assert compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) == [0,0,0,0,3,3]

def test_type_scenario_incorrect_guess_small_diff():
    assert compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) == [4,4,1,0,0,6]

def test_type_scenario_incorrect_guess_large_diff():
    assert compare([1,2,3,4,5,1],[5,6,7,8,9,10]) == [4,4,4,4,4,9]

# Focus: Logic Branches
import pytest

def test_compare_correct_guesses():
    assert compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) == [0,0,0,0,3,3]

def test_compare_incorrect_guesses():
    assert compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) == [4,4,1,0,0,6]

def test_compare_single_element():
    assert compare([5],[5]) == [0]
    assert compare([5],[6]) == [1]