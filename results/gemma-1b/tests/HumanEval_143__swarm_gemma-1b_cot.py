
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
from math import sqrt

def words_in_sentence(text):
    """
    Checks if a sentence contains only valid words.
    """
    words = text.split()
    for word in words:
        if not word.isalpha():
            return False
    return True

def test_words_in_sentence():
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"
    assert words_in_sentence("a b c d e") == "a b c d e"
    assert words_in_sentence("abc") == "abc"
    assert words_in_sentence("12345") == "12345"
    assert words_in_sentence("1234567890") == "1234567890"
    assert words_in_sentence("abcde") == "abcde"
    assert words_in_sentence("a") == "a"
    assert words_in_sentence("") == ""

Final Suite:
    pass