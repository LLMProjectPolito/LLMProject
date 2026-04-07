
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
import math


# Focus: Boundary Values
def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_single_word_prime_length():
    assert words_in_sentence("abc") == "abc"

def test_single_word_non_prime_length():
    assert words_in_sentence("ab") == ""

# Focus: Type Scenarios
def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_length_words():
    assert words_in_sentence("hello world") == ""

def test_mixed_prime_and_non_prime_words():
    assert words_in_sentence("This is a test") == "is"

def test_all_prime_length_words():
    assert words_in_sentence("lets go for swimming") == "go for"

# Focus: Logic Branches
def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_length_words():
    assert words_in_sentence("This is a test") == "is"

def test_all_prime_length_words():
    assert words_in_sentence("lets go for swimming") == "go for"