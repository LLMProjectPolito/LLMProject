import pytest
import math


# Focus: Boundary Values
def test_boundary_values_empty_lists():
    assert compare([], []) == []

def test_boundary_values_single_element_correct():
    assert compare([5], [5]) == [0]

def test_boundary_values_single_element_incorrect():
    assert compare([5], [6]) == [1]

def test_boundary_values_zero_score_zero_guess():
    assert compare([0], [0]) == [0]

def test_boundary_values_large_numbers():
    assert compare([1000, 2000], [1000, 2001]) == [0, 1]

# Focus: Type Scenarios
def test_compare_correct_guesses():
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 5, 1]
    expected = [0, 0, 0, 0, 0, 0]
    assert compare(game, guess) == expected

def test_compare_mixed_guesses():
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 2, -2]
    expected = [0, 0, 0, 0, 3, 3]
    assert compare(game, guess) == expected

def test_compare_all_incorrect_guesses():
    game = [0, 5, 0, 0, 0, 4]
    guess = [4, 1, 1, 0, 0, -2]
    expected = [4, 4, 1, 0, 0, 6]
    assert compare(game, guess) == expected

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