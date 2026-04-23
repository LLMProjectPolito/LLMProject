
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
from typing import List

def is_prime(n: int) -> bool:
    """
    Helper function to check if a number is prime.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

def words_in_sentence(sentence: str) -> str:
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
    result = []
    for word in words:
        if is_prime(len(word)):
            result.append(word)
    return " ".join(result)


def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_single_word():
    assert words_in_sentence("hello") == "hello"

def test_multiple_words_prime():
    assert words_in_sentence("This is a test") == "is"

def test_multiple_words_non_prime():
    assert words_in_sentence("This is a test with some words") == "This is a test"

def test_all_words_prime():
    assert words_in_sentence("abcdefghijk") == "abcdefghijk"

def test_short_sentence_1():
    assert words_in_sentence("a") == "a"

def test_short_sentence_2():
    assert words_in_sentence("ab") == "a"

def test_word_with_number():
    assert words_in_sentence("123 test") == "test"

def test_leading_trailing_space():
    assert words_in_sentence("  hello world  ") == "hello world"

def test_special_characters():
    assert words_in_sentence("Hello! World?") == "Hello! World?" # Should not fail, but should return original sentence.