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
        if game[i] == guess[i]:
            result.append(0)
        else:
            result.append(abs(game[i] - guess[i]))
    return result

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


# Pytest suite
def test_compare_correct_guesses():
    assert compare([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [0, 0, 0, 0, 0]

def test_compare_incorrect_guesses():
    assert compare([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == [4, 2, 0, 2, 4]

def test_compare_mixed_guesses():
    assert compare([1, 2, 3, 4, 5], [1, 2, 4, 4, 2]) == [0, 0, 1, 0, 3]

def test_compare_negative_numbers():
    assert compare([-1, -2, -3], [-1, -1, -4]) == [0, 1, 1]

def test_compare_zero_scores():
    assert compare([0, 0, 0], [1, 2, 3]) == [1, 2, 3]

def test_compare_empty_lists():
    with pytest.raises(IndexError):
        compare([], [])

def test_compare_different_lengths():
    with pytest.raises(IndexError):
        compare([1, 2], [1])

def test_compare_large_numbers():
    assert compare([1000, 2000, 3000], [1000, 2001, 3000]) == [0, 1, 0]

def test_compare_all_negative_incorrect():
    assert compare([-1, -2, -3], [-4, -5, -6]) == [3, 3, 3]

def test_compare_single_element_correct():
    assert compare([5], [5]) == [0]

def test_compare_single_element_incorrect():
    assert compare([5], [6]) == [1]

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True

def test_palindrome_with_spaces():
    assert is_palindrome('A man, a plan, a canal: Panama') == False # Spaces are not ignored

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4