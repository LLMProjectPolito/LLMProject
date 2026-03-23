import pytest
import math


# Focus: Boundary Values
def test_compare_boundary_correct_guess():
    """Test when guess is exactly equal to the score at the boundary."""
    game = [0]
    guess = [0]
    expected = [0]
    assert compare(game, guess) == expected

def test_compare_boundary_negative_score_and_guess():
    """Test with negative scores and guesses at the boundary."""
    game = [-1]
    guess = [-1]
    expected = [0]
    assert compare(game, guess) == expected

def test_compare_boundary_zero_score_non_zero_guess():
    """Test when score is zero and guess is non-zero at the boundary."""
    game = [0]
    guess = [1]
    expected = [1]
    assert compare(game, guess) == expected

# Focus: Logic Branches
def test_compare_correct_guesses():
    """Tests the scenario where all guesses are correct."""
    game = [1, 2, 3, 4, 5, 1]
    guesses = [1, 2, 3, 4, 5, 1]
    expected_result = [0, 0, 0, 0, 0, 0]
    assert compare(game, guesses) == expected_result

def test_compare_incorrect_guesses():
    """Tests the scenario where some guesses are incorrect."""
    game = [1, 2, 3, 4, 5, 1]
    guesses = [1, 2, 3, 4, 2, -2]
    expected_result = [0, 0, 0, 0, 3, 3]
    assert compare(game, guesses) == expected_result

def test_compare_all_guesses_off():
    """Tests the scenario where all guesses are significantly off."""
    game = [0, 5, 0, 0, 0, 4]
    guesses = [4, 1, 1, 0, 0, -2]
    expected_result = [4, 4, 1, 0, 0, 6]
    assert compare(game, guesses) == expected_result

# Focus: Type Scenarios
def test_compare_correct_guesses():
    """Test case where all guesses are correct."""
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 5, 1]
    expected_result = [0, 0, 0, 0, 0, 0]
    assert compare(game, guess) == expected_result

def test_compare_mixed_guesses():
    """Test case with a mix of correct and incorrect guesses."""
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 2, -2]
    expected_result = [0, 0, 0, 0, 3, 3]
    assert compare(game, guess) == expected_result

def test_compare_all_incorrect_guesses():
    """Test case where all guesses are incorrect."""
    game = [0, 5, 0, 0, 0, 4]
    guess = [4, 1, 1, 0, 0, -2]
    expected_result = [4, 4, 1, 0, 0, 6]
    assert compare(game, guess) == expected_result