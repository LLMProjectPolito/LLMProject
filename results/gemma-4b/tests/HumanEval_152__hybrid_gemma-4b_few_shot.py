import pytest

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

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
        result.append(abs(game[i] - guess[i]))
    return result

# Pytest suite for is_palindrome
def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Race car') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True
    assert is_palindrome('Madam, I\'m Adam') == True
    assert is_palindrome('No lemon, no melon') == True
    assert is_palindrome('12321') == True
    assert is_palindrome('12345') == False

def test_is_palindrome_empty():
    assert is_palindrome('') == True
    assert is_palindrome(' ') == True
    assert is_palindrome('a') == True

def test_is_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True

def test_is_palindrome_with_punctuation():
    assert is_palindrome('A man, a plan, a canal: Panama!') == True

# Pytest suite for get_max
def test_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([3, 2, 1]) == 3
    assert get_max([-1, 0, 1]) == 1
    assert get_max([5, 5, 5]) == 5

def test_max_empty():
    assert get_max([]) == None

def test_max_single_element():
    assert get_max([7]) == 7

def test_max_negative_numbers():
    assert get_max([-1, -5, -2]) == -1

# Pytest suite for compare
def test_compare_basic():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_perfect_guess():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_compare_single_element():
    assert compare([5], [5]) == [0]

def test_compare_negative_numbers():
    assert compare([-1, -2, -3], [-1, -2, -3]) == [0, 0, 0]

def test_compare_mixed_numbers():
    assert compare([-1, 2, -3], [-1, 2, -3]) == [0, 0, 0]

def test_compare_different_lengths():
    with pytest.raises(IndexError):
        compare([1, 2, 3], [1, 2])

def test_compare_empty_game():
    assert compare([], []) == []

def test_compare_empty_guess():
    assert compare([1, 2, 3], []) == []