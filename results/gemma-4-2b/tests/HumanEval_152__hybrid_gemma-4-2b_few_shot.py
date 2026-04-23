
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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def compare(game, guess):
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
        if game[i] == guess[i]:
            result.append(0)
        else:
            result.append(abs(guess[i] - game[i]))
    return result

def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_is_palindrome_empty():
    assert is_palindrome('') == True

def test_is_palindrome_single_char():
    assert is_palindrome('a') == True

def test_is_palindrome_multiple_chars():
    assert is_palindrome('racecar') == True
    assert is_palindrome('level') == True
    assert is_palindrome('rotor') == True
    assert is_palindrome('madam') == True
    assert is_palindrome('deified') == True
    assert is_palindrome('noon') == True
    assert is_palindrome('kayak') == True
    assert is_palindrome('stats') == True
    assert is_palindrome('refer') == True
    assert is_palindrome('redder') == True
    assert is_palindrome('civic') == True
    assert is_palindrome('wow') == True
    assert is_palindrome('a') == True
    assert is_palindrome('ab') == False
    assert is_palindrome('abc') == False
    assert is_palindrome('aba') == True
    assert is_palindrome('abcba') == True
    assert is_palindrome('abccba') == True
    assert is_palindrome('abcde') == False

def test_compare_empty_arrays():
    assert compare([], []) == []

def test_compare_all_correct():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_compare_all_incorrect():
    assert compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

def test_compare_mixed_correct_incorrect():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

def test_compare_mixed_correct_incorrect_2():
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_different_length_arrays():
    with pytest.raises(IndexError):
        compare([1, 2], [1, 2, 3])

def test_compare_negative_numbers():
    assert compare([-1, -2, -3], [-1, -2, -3]) == [0, 0, 0]
    assert compare([-1, -2, -3], [4, 5, 6]) == [5, 5, 5]

def test_compare_zero_scores():
    assert compare([0, 0, 0], [1, 2, 3]) == [1, 2, 3]
    assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]

def test_compare_large_numbers():
    assert compare([1000000, 2000000, 3000000], [1000000, 2000000, 3000000]) == [0, 0, 0]
    assert compare([1000000, 2000000, 3000000], [1000000, 2000000, 3000000]) == [0, 0, 0]

def test_compare_mixed_signs_and_zeros():
    assert compare([0, -1, 0, 1], [1, 0, 1, -1]) == [1, 0, 0, 0]

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_single_element():
    assert get_max([5]) == 5
    assert get_max([-5]) == -5

def test_get_max_negative_numbers():
    assert get_max([-1, -2, -3]) == -1
    assert get_max([-1, -2, -3]) == -1

def test_get_max_mixed_numbers():
    assert get_max([1, -2, 3, -4, 5]) == 5
    assert get_max([-1, 2, -3, 4, -5]) == 4
    assert get_max([1, 2, 3, 4, 5]) == 5
    assert get_max([5, 4, 3, 2, 1]) == 5

def test_get_max_same_numbers():
    assert get_max([5, 5, 5, 5]) == 5
    assert get_max([-5, -5, -5, -5]) == -5