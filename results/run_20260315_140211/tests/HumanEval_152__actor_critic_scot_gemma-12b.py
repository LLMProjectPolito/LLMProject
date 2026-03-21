import pytest
from your_module import compare  # Replace your_module

def test_mixed_guesses_with_negative_value():
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 2, -2]
    expected = [0, 0, 0, 0, 1, 3]
    assert compare(game, guess) == expected

def test_negative_values():
    game = [-1, -2, -3, -4, -5]
    guess = [-2, -3, -4, -5, -6]
    expected = [1, 1, 1, 1, 1]
    assert compare(game, guess) == expected

def test_large_values():
    game = [1000000, 2000000, 3000000]
    guess = [1000000, 2000000, 3000001]
    expected = [0, 0, 1]
    assert compare(game, guess) == expected

    game = [2**30, 2**30 + 1, 2**30 + 2]
    guess = [2**30, 2**30 + 1, 2**30 + 3]
    expected = [0, 0, 1]
    assert compare(game, guess) == expected

def test_duplicate_values():
    game = [1, 2, 2, 3, 4]
    guess = [1, 2, 3, 4, 5]
    expected = [0, 0, 1, 0, 0]
    assert compare(game, guess) == expected

def test_all_values_present():
    game = [1, 2, 3, 4, 5]
    guess = [2, 1, 4, 5, 3]
    expected = [1, 0, 1, 0, 0]
    assert compare(game, guess) == expected

def test_unequal_lengths():
    game = [1, 2, 3]
    guess = [1, 2]
    with pytest.raises(ValueError):
        compare(game, guess)

def test_non_numeric_input():
    game = [1, 2, "a", 3.14, True]
    guess = [1, 2, 3, 4, 5]
    with pytest.raises(TypeError):
        compare(game, guess)

def test_single_element():
    game = [5]
    guess = [5]
    expected = [0]
    assert compare(game, guess) == expected

    game = [5]
    guess = [6]
    expected = [1]
    assert compare(game, guess) == expected

def test_identical_elements():
    game = [2, 2, 2, 2]
    guess = [2, 2, 2, 2]
    expected = [0, 0, 0, 0]
    assert compare(game, guess) == expected

    game = [2, 2, 2, 2]
    guess = [2, 2, 2, 3]
    expected = [0, 0, 0, 1]
    assert compare(game, guess) == expected

def test_subset_lists():
    game = [1, 2, 3, 4, 5]
    guess = [1, 2, 3]
    expected = [0, 0, 0, 1, 1]
    assert compare(game, guess) == expected