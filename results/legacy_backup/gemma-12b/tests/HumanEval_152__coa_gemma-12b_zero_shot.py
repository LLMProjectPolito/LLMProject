import pytest
import math


# Focus: Boundary Values
def test_boundary_correct_guess():
    assert compare([1], [1]) == [0]

def test_boundary_incorrect_guess_small_difference():
    assert compare([1], [2]) == [1]

def test_boundary_incorrect_guess_large_difference():
    assert compare([1], [10]) == [9]

# Focus: Logic Branches
def test_compare_correct_guesses():
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 5, 1]
    expected = [0, 0, 0, 0, 0, 0]
    assert compare(game, guess) == expected

def test_compare_incorrect_guesses():
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 2, -2]
    expected = [0, 0, 0, 0, 3, 3]
    assert compare(game, guess) == expected

def test_compare_mixed_guesses():
    game = [0, 5, 0, 0, 0, 4]
    guess = [4, 1, 1, 0, 0, -2]
    expected = [4, 4, 1, 0, 0, 6]
    assert compare(game, guess) == expected

# Focus: Type Scenarios
def test_type_scenario_1():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

def test_type_scenario_2():
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_type_scenario_3():
    assert compare([10, 20, 30], [10, 25, 30]) == [0, 5, 0]