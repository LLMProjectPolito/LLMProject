
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

def test_compare_empty_lists():
    assert compare([], []) == []

def test_compare_equal_lists():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_compare_different_lists():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_negative_numbers():
    assert compare([-1, -2, -3], [-1, -2, -3]) == [0, 0, 0]
    assert compare([-1, -2, -3], [0, -1, -4]) == [1, 1, 1]

def test_compare_mixed_positive_negative():
    assert compare([1, -2, 3], [1, -2, 3]) == [0, 0, 0]
    assert compare([1, -2, 3], [0, -1, 4]) == [1, 1, 1]
    assert compare([1, -2, 3], [-1, -2, 4]) == [2, 0, 1]

def test_compare_large_numbers():
    assert compare([1000, 2000, 3000], [1000, 2000, 3000]) == [0, 0, 0]
    assert compare([1000, 2000, 3000], [900, 2100, 2900]) == [100, 100, 100]
    assert compare([1000, 2000, 3000], [1000, 2001, 2999]) == [0, 1, 1]

def test_compare_zero_values():
    assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]
    assert compare([0, 0, 0], [1, 2, 3]) == [1, 2, 3]
    assert compare([1, 2, 3], [0, 0, 0]) == [1, 2, 3]

def test_compare_single_element_lists():
    assert compare([5], [5]) == [0]
    assert compare([5], [10]) == [5]

def test_compare_different_lengths_raises_error():
    with pytest.raises(ValueError):
        compare([1, 2], [1])

def test_compare_non_integer_input_raises_error():
    with pytest.raises(TypeError):
        compare([1.5, 2], [1, 2])
    with pytest.raises(TypeError):
        compare([1, 2], [1.5, 2])
    with pytest.raises(TypeError):
        compare(["1", 2], [1, 2])
    with pytest.raises(TypeError):
        compare([1, 2], ["1", 2])