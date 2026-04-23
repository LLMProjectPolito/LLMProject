
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """

import pytest

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    words = sentence.split()
    result = ""
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result.strip()


def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('Racecar') == True  # Test case-insensitivity
    assert is_palindrome('A man, a plan, a canal: Panama') == False # Test with punctuation and spaces

def test_is_palindrome_empty():
    assert is_palindrome('') == True
    assert is_palindrome(' ') == True # Test with only space

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([5, 2, 8, 1, 9]) == 9
    assert get_max([10]) == 10

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1
    assert get_max([-5, -2, -8, -1, -9]) == -1

def test_get_max_mixed():
    assert get_max([-1, 2, -3, 4, -5]) == 4

def test_words_in_sentence_empty():
    assert words_in_sentence("") == ""

def test_words_in_sentence_no_prime_length():
    assert words_in_sentence("a i") == ""

def test_words_in_sentence_some_prime_length():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("hello world") == "world"
    assert words_in_sentence("the quick brown fox jumps over the lazy dog") == "quick brown jumps"

def test_words_in_sentence_all_prime_length():
    assert words_in_sentence("one three five seven nine") == "one three five seven nine"

def test_words_in_sentence_mixed_prime_non_prime():
    assert words_in_sentence("This is a test sentence") == "is test"

def test_words_in_sentence_long_sentence():
    sentence = "This is a very long sentence with many words to test the function"
    assert words_in_sentence(sentence) == "very long sentence"