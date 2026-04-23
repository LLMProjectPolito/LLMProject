
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

def test_empty_lists():
    assert compare([], []) == []

def test_empty_list_vs_non_empty_list():
    assert compare([], [1, 2, 3]) == [1, 2, 3]

def test_equal_lists_all_correct():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_equal_lists_some_correct():
    assert compare([1, 2, 3, 4, 5], [1, 2, 3, 4, 2]) == [0, 0, 0, 0, 3]

def test_equal_lists_all_incorrect():
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_equal_lists_negative_numbers():
    assert compare([-1, -2, -3], [-1, -2, -4]) == [0, 0, 1]

def test_equal_lists_zero_values():
    assert compare([0, 0, 0], [0, 1, 0]) == [0, 1, 0]

def test_equal_lists_mixed_values():
    assert compare([1, -2, 0, 3], [1, -1, 0, 4]) == [0, 1, 0, 1]

def test_unequal_lists_message():
    with pytest.raises(ValueError) as excinfo:
        compare([1, 2], [1, 2, 3])
    assert str(excinfo.value) == "Lists must be of the same length"

def test_large_numbers():
    assert compare([1000000, 2000000], [1000000, 2000001]) == [0, 1]

def test_non_numeric_comparison():
    assert compare([1, "a", 3], [1, "b", 3]) == [0, 1, 0]  # Expecting always different

def test_floating_point_approx():
    assert compare([1.0, 2.5, 3.0], [1.0, 2.0, 3.0]) == [0.0, pytest.approx(0.5), 0.0]

def test_different_types_same_value():
    assert compare([1, 2], [1.0, 2.0]) == [0.0, 0.0]

def test_nan_values():
    import math
    assert compare([1.0, float('NaN'), 3.0], [1.0, float('NaN'), 3.0]) == [0.0, float('NaN'), 0.0]

def test_inf_values():
    import math
    assert compare([1.0, float('Inf'), 3.0], [1.0, float('Inf'), 3.0]) == [0.0, float('Inf'), 0.0]

def test_mixed_types_error():
    # This test assumes the compare function handles mixed types gracefully
    # and doesn't crash.  The specific expected behavior depends on the
    # implementation of compare.  Here, we expect it to treat the
    # comparison as always different.
    assert compare([1, "a", 3], [1, 2, 3]) == [0, 1, 0]

def test_different_data_types():
    assert compare([1, "a", 3], [1, 2, 3]) == [0, 1, 0]

def test_none_values():
    assert compare([1, None, 3], [1, 2, 3]) == [0, 1, 0]

def test_empty_string_values():
    assert compare([1, "", 3], [1, "a", 3]) == [0, 1, 0]

def test_boolean_values():
    assert compare([True, False, True], [True, True, False]) == [0, 1, 1]

def test_duplicate_values():
    assert compare([1, 2, 2, 3], [1, 2, 3, 3]) == [0, 0, 1, 0]

def test_long_lists():
    list1 = list(range(1000))
    list2 = list(range(1000))
    expected = [0] * 1000
    assert compare(list1, list2) == expected