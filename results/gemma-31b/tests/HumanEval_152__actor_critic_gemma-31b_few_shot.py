
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

# --- Existing Tests ---

def test_compare_examples():
    """Tests the examples provided in the docstring."""
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_empty():
    """Tests that empty lists return an empty list."""
    assert compare([], []) == []

def test_compare_single_element():
    """Tests lists with a single element."""
    assert compare([10], [10]) == [0]
    assert compare([10], [5]) == [5]
    assert compare([5], [10]) == [5]

def test_compare_all_correct():
    """Tests cases where every guess is exactly correct."""
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]
    assert compare([-1, -5, 0], [-1, -5, 0]) == [0, 0, 0]

def test_compare_all_incorrect():
    """Tests cases where no guesses are correct."""
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_compare_negative_numbers():
    """Tests absolute difference logic with negative integers."""
    assert compare([-1, -2, 5], [-5, 2, -5]) == [4, 4, 10]

def test_compare_large_numbers():
    """Tests the function with large integer values."""
    assert compare([1000000], [2000000]) == [1000000]

def test_compare_zeros():
    """Tests cases involving zeros."""
    assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]
    assert compare([0, 0, 0], [1, -1, 0]) == [1, 1, 0]

# --- Refined/New Tests based on Review ---

def test_compare_unequal_lengths():
    """Verifies that lists of different lengths raise a ValueError."""
    with pytest.raises(ValueError):
        compare([1, 2], [1, 2, 3])
    with pytest.raises(ValueError):
        compare([1, 2, 3], [1, 2])

def test_compare_floats():
    """Tests floating-point numbers for precision and type handling."""
    # Basic float difference
    assert compare([1.5, 2.0], [1.0, 3.5]) == [0.5, 1.5]
    
    # Testing floating point precision (e.g., 0.1 + 0.2 != 0.3 exactly)
    # We use pytest.approx to handle floating point inaccuracies
    result = compare([0.1 + 0.2], [0.3])
    assert result[0] == pytest.approx(0.0)

def test_compare_invalid_input_types():
    """Verifies that invalid input types raise a TypeError."""
    # Test None inputs
    with pytest.raises(TypeError):
        compare(None, [1, 2])
    with pytest.raises(TypeError):
        compare([1, 2], None)
    
    # Test non-list inputs
    with pytest.raises(TypeError):
        compare("123", [1, 2])
    with pytest.raises(TypeError):
        compare([1, 2], "123")
        
    # Test lists containing invalid types (e.g., strings instead of numbers)
    with pytest.raises(TypeError):
        compare([1, 2], [1, "2"])