
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

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

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
    words = sentence.split()
    result = ""
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result.strip()


def test_single_prime_word():
    assert words_in_sentence("a") == "a"

def test_single_non_prime_word():
    assert words_in_sentence("b") == ""

def test_multiple_words_mixed():
    assert words_in_sentence("This is a test") == "is"

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_only_non_prime_words():
    assert words_in_sentence("abc def ghi") == ""

def test_only_prime_words():
    assert words_in_sentence("abc def ghi") == "abc def ghi"

def test_mixed_words():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_long_word():
    assert words_in_sentence("verylongword") == "verylongword"

def test_sentence_with_special_characters():
    assert words_in_sentence("hello, world!") == ""