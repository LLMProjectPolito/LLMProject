import pytest

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
    result = []
    for i in range(len(game)):
        result.append(abs(guess[i] - game[i]))
    return result

def test_compare_correct_guesses():
    """Test case: All guesses are correct."""
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 2, -2]
    assert compare(game, guess) == [0, 0, 0, 0, 3, 3]

def test_compare_some_correct_guesses():
    """Test case: Some guesses are correct, some are not."""
    game = [0, 5, 0, 0, 0, 4]
    guess = [4, 1, 1, 0, 0, -2]
    assert compare(game, guess) == [4, 4, 1, 0, 0, 6]

def test_compare_all_incorrect_guesses():
    """Test case: All guesses are incorrect."""
    game = [1, 2, 3, 4, 5, 1]
    guess = [1, 2, 3, 4, 5, 5]
    assert compare(game, guess) == [0, 0, 0, 0, 0, 4]

def test_compare_empty_lists():
    """Test case: Both lists are empty."""
    game = []
    guess = []
    assert compare(game, guess) == []

def test_compare_unequal_length_lists():
    """Test case: Lists have different lengths."""
    game = [1, 2, 3]
    guess = [1, 2, 3, 4]
    with pytest.raises(IndexError):
        compare(game, guess)

def test_compare_negative_numbers():
    """Test case: Lists contain negative numbers."""
    game = [-1, -2, -3]
    guess = [-1, -2, -3]
    assert compare(game, guess) == [0, 0, 0]

def test_compare_mixed_numbers():
    """Test case: Lists contain mixed positive and negative numbers."""
    game = [1, -2, 3]
    guess = [1, 2, 3]
    assert compare(game, guess) == [0, 2, 0]

def test_compare_zero_values():
    """Test case: Lists contain zero values."""
    game = [0, 0, 0]
    guess = [0, 0, 0]
    assert compare(game, guess) == [0, 0, 0]

def test_compare_large_numbers():
    """Test case: Lists contain large numbers."""
    game = [1000, 2000, 3000]
    guess = [1000, 2000, 3000]
    assert compare(game, guess) == [0, 0, 0]