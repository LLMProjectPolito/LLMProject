
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
    """Test case for an empty sentence."""
    sentence = ""
    assert words_in_sentence(sentence) == ""

def test_sentence_with_no_prime_length_words():
    """Test case where no words have prime length."""
    sentence = "this is a test sentence"
    assert words_in_sentence(sentence) == ""

def test_sentence_with_only_one_prime_length_word():
    """Test case with only one word of prime length."""
    sentence = "a very long sentence"
    assert words_in_sentence(sentence) == "a"

def test_sentence_with_multiple_prime_length_words_at_start():
    """Test case with multiple prime length words at the beginning."""
    sentence = "go for a walk"
    assert words_in_sentence(sentence) == "go for a"

def test_sentence_with_multiple_prime_length_words_at_end():
    """Test case with multiple prime length words at the end."""
    sentence = "this is a fun test"
    assert words_in_sentence(sentence) == "is fun"

def test_sentence_with_leading_and_trailing_spaces():
    """Test case with leading and trailing spaces."""
    sentence = "  this is a test  "
    assert words_in_sentence(sentence) == "is"

def test_sentence_with_multiple_spaces_between_words():
    """Test case with multiple spaces between words."""
    sentence = "this  is   a    test"
    assert words_in_sentence(sentence) == "is"