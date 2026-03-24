import pytest

def compare(game,guess):
    """
    Calculates the absolute difference between elements of two lists.

    Args:
        game (list): List of integer scores.
        guess (list): List of integer guesses.

    Returns:
        list: List of absolute differences between game and guess elements.
              The comparison stops at the length of the shorter list.
    """
    result = []
    min_len = min(len(game), len(guess))
    for i in range(min_len):
        result.append(abs(game[i] - guess[i]))
    return result

def test_empty_lists():
    assert compare([], []) == []

def test_single_element_correct():
    assert compare([5], [5]) == [0]

def test_single_element_incorrect():
    assert compare([5], [3]) == [2]

def test_all_elements_equal():
    assert compare([1, 1, 1], [1, 1, 1]) == [0, 0, 0]

def test_mixed_correct_incorrect():
    assert compare([1, 2, 3, 4], [1, 3, 3, 5]) == [0, 1, 0, 1]

def test_negative_numbers():
    assert compare([-1, -2, -3], [-1, -1, -4]) == [0, 1, 1]

def test_zero_values():
    assert compare([0, 0, 0], [1, 2, 3]) == [1, 2, 3]

def test_example_1():
    assert compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) == [0,0,0,0,3,3]

def test_example_2():
    assert compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) == [4,4,1,0,0,6]

def test_unequal_length_lists():
    assert compare([1, 2, 3, 4], [1, 2, 3]) == [0, 0, 0]

def test_unequal_length_lists_guess_longer():
    assert compare([1, 2, 3], [1, 2, 3, 4]) == [0, 0, 0]

def test_large_numbers():
    assert compare([10**9, 10**9 + 1], [10**9, 10**9]) == [0, 1]

def test_mixed_positive_negative_zero():
    assert compare([-1, 0, 1, -2], [1, -1, 0, 2]) == [2, 1, 1, 4]

def test_string_input():
    with pytest.raises(TypeError):
        compare(["1", "2"], [1, 2])