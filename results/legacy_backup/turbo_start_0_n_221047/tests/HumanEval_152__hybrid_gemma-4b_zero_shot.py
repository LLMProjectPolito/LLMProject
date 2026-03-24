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

def test_compare_empty():
    assert compare([], []) == []

def test_compare_equal():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_compare_one_off():
    assert compare([1, 2, 3], [1, 2, 4]) == [0, 0, 1]

def test_compare_multiple_off():
    assert compare([1, 2, 3], [1, 2, 5]) == [0, 0, 2]

def test_compare_negative_numbers():
    assert compare([-1, 2, -3], [-1, 2, -3]) == [0, 0, 0]

def test_compare_mixed_numbers():
    assert compare([1, -2, 3], [1, -2, 3]) == [0, 0, 0]

def test_compare_different_lengths():
    with pytest.raises(IndexError):
        compare([1, 2, 3], [1, 2])

def test_compare_large_numbers():
    assert compare([1000, 2000, 3000], [1000, 2000, 3000]) == [0, 0, 0]

def test_compare_zero_values():
    assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]

def test_compare_zero_and_positive():
    assert compare([0, 1, 2], [0, 1, 2]) == [0, 0, 0]

def test_compare_complex_case1():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

def test_compare_complex_case2():
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_all_negative():
    assert compare([-1, -2, -3], [-1, -2, -3]) == [0, 0, 0]

def test_compare_mixed_positive_negative():
    assert compare([1, -2, 3], [1, -2, 3]) == [0, 0, 0]

def test_compare_correct_guesses():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 5, 1]) == [0, 0, 0, 0, 0, 0]
    assert compare([10, 20, 30, 40, 50, 60], [10, 20, 30, 40, 50, 60]) == [0, 0, 0, 0, 0, 0]

def test_compare_incorrect_guesses():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 6, -2]) == [0, 0, 0, 0, 2, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 5, 2]) == [0, 0, 0, 0, 1, 1]
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 5, 3]) == [0, 0, 0, 0, 0, 2]

def test_compare_empty_arrays():
    assert compare([], []) == []

def test_compare_unequal_length_arrays():
    with pytest.raises(IndexError):
        compare([1, 2, 3], [1, 2])

def test_compare_negative_numbers():
    assert compare([-1, -2, -3, -4, -5, -1], [-1, -2, -3, -4, -2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([-1, -2, -3, -4, -5, -1], [-1, -2, -3, -4, -6, -2]) == [0, 0, 0, 0, 1, 3]

def test_compare_mixed_positive_negative():
    assert compare([1, -2, 3, -4, 5, -1], [1, -2, 3, -4, 5, -2]) == [0, 0, 0, 0, 0, 1]
    assert compare([1, -2, 3, -4, 5, -1], [1, -2, 3, -4, 6, -2]) == [0, 0, 0, 0, 1, 1]