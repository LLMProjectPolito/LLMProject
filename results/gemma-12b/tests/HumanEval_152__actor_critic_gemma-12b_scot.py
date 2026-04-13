
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
from your_module import compare  # Replace your_module

def test_identical_lists():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_empty_lists():
    assert compare([], []) == []

def test_incorrect_guesses():
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_mixed_guesses():
    assert compare([1, 2, 3, 4, 5], [1, 3, 3, 4, 7]) == [0, 1, 0, 0, 2]

def test_positive_numbers():
    assert compare([10, 20, 30], [15, 20, 25]) == [5, 0, 5]

def test_negative_numbers():
    assert compare([-1, -2, -3], [-4, -2, -5]) == [3, 0, 2]

def test_zero_numbers():
    assert compare([0, 0, 0], [0, 1, 0]) == [0, 1, 0]

def test_mixed_positive_negative_zero():
    assert compare([-1, 0, 1], [2, -1, 0]) == [3, 1, 1]

def test_single_element_lists():
    assert compare([5], [5]) == [0]
    assert compare([5], [10]) == [5]

def test_large_numbers():
    assert compare([100000, 200000, 300000], [100005, 200000, 299995]) == [5, 0, 5]

def test_different_lengths():
    with pytest.raises(ValueError) as excinfo:
        compare([1, 2], [1, 2, 3])
    assert str(excinfo.value) == "Lists must be of the same length."

def test_duplicate_values():
    assert compare([1, 1, 2], [1, 3, 2]) == [0, 2, 0]

def test_same_values_different_order():
    assert compare([1, 2, 3], [3, 2, 1]) == [2, 0, 2]

def test_floating_point_numbers():
    assert compare([1.0, 2.5, 3.0], [1.2, 2.5, 3.1]) == [0.2, 0.0, 0.1]

def test_none_input():
    with pytest.raises(TypeError) as excinfo:
        compare([1, 2, 3], None)
    assert str(excinfo.value) == "Inputs must be lists."

    with pytest.raises(TypeError) as excinfo:
        compare(None, [1, 2, 3])
    assert str(excinfo.value) == "Inputs must be lists."

    with pytest.raises(TypeError) as excinfo:
        compare(None, None)
    assert str(excinfo.value) == "Inputs must be lists."

def test_non_numeric_input():
    with pytest.raises(TypeError) as excinfo:
        compare([1, 2, "a"], [1, 2, 3])
    assert str(excinfo.value) == "List elements must be numeric."

    with pytest.raises(TypeError) as excinfo:
        compare([1, 2, 3], [1, 2, "b"])
    assert str(excinfo.value) == "List elements must be numeric."

def test_mixed_numeric_types():
    assert compare([1, 2.5, 3], [1, 2, 3.5]) == [0, 0.5, 0.5]

def test_ties():
    assert compare([1, 2, 3], [1, 2, 4]) == [0, 0, 1]