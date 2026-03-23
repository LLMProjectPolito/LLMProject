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