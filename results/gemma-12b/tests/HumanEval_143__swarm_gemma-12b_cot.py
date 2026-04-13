
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
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_length_words():
    assert words_in_sentence("this is not a prime") == ""

def test_sentence_with_only_one_word():
    assert words_in_sentence("hello") == ""

def test_sentence_with_leading_and_trailing_spaces():
    assert words_in_sentence("  hello world  ") == "world"

def test_sentence_with_multiple_prime_length_words():
    assert words_in_sentence("a bb ccc dddd eeeee ffffff") == "a"

def test_sentence_with_prime_length_words_at_start_and_end():
    assert words_in_sentence("go for swimming") == "go for"