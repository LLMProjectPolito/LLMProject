import pytest

def test_compare_perfect_guess():
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 5, 1]
    assert compare(game, guess) == [0, 0, 0, 0, 0, 0]

def test_compare_off_by_one():
    game = [1, 2, 3, 4, 5, 1]
    guess = [2, 3, 4, 5, 6, 2]
    assert compare(game, guess) == [1, 1, 1, 1, 1, 1]

def test_compare_off_by_multiple():
    game = [1, 2, 3, 4, 5, 1]
    guess = [10, 20, 30, 40, 50, 10]
    assert compare(game, guess) == [9, 18, 27, 36, 45, 9]

def test_compare_mixed_results():
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 2, -2]
    assert compare(game, guess) == [0, 0, 0, 0, 3, 3]

def test_compare_all_off():
    game = [0, 5, 0, 0, 0, 4]
    guess = [4, 1, 1, 0, 0, -2]
    assert compare(game, guess) == [4, 4, 1, 0, 0, 6]

def test_compare_empty_lists():
    game = []
    guess = []
    assert compare(game, guess) == []

def test_compare_single_element_lists():
    game = [1]
    guess = [1]
    assert compare(game, guess) == [0]

def test_compare_lists_of_different_lengths():
    game = [1, 2, 3]
    guess = [1, 2]
    with pytest.raises(IndexError):
        compare(game, guess)