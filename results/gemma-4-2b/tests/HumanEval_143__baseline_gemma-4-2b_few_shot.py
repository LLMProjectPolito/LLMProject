
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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
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


import pytest

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_words_in_sentence_basic():
    assert words_in_sentence("This is a test") == "is"

def test_words_in_sentence_complex():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_empty():
    assert words_in_sentence("") == ""

def test_words_in_sentence_single_word():
    assert words_in_sentence("word") == "word"

def test_words_in_sentence_multiple_prime_length_words():
    assert words_in_sentence("apple banana orange") == "banana orange"

def test_words_in_sentence_no_prime_length_words():
    assert words_in_sentence("cat dog bird") == ""

def test_words_in_sentence_mixed_words():
    assert words_in_sentence("This is a test string") == "is a test"

def test_words_in_sentence_long_sentence():
    assert words_in_sentence("This is a very long sentence with some words") == "is a very long sentence"