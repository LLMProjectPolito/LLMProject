import pytest
from your_module import compare  # Replace your_module

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

def test_compare_empty_lists():
    game = []
    guess = []
    expected = []
    assert compare(game, guess) == expected

def test_compare_single_element_lists():
    game = [5]
    guess = [6]
    expected = [1]
    assert compare(game, guess) == expected

def test_compare_single_element_correct():
    game = [5]
    guess = [5]
    expected = [0]
    assert compare(game, guess) == expected

def test_compare_negative_scores():
    game = [-1, -2, -3]
    guess = [-1, -2, 0]
    expected = [0, 0, 3]
    assert compare(game, guess) == expected

def test_compare_large_numbers():
    game = [1000, 2000, 3000]
    guess = [1000, 2500, 3000]
    expected = [0, 500, 0]
    assert compare(game, guess) == expected

def test_compare_zero_scores():
    game = [0, 0, 0]
    guess = [1, 2, 3]
    expected = [1, 2, 3]
    assert compare(game, guess) == expected

def test_compare_different_lengths_raises_error():
    game = [1, 2, 3]
    guess = [1, 2]
    with pytest.raises(ValueError):
        compare(game, guess)

def test_compare_different_lengths_raises_error2():
    game = [1, 2]
    guess = [1, 2, 3]
    with pytest.raises(ValueError):
        compare(game, guess)