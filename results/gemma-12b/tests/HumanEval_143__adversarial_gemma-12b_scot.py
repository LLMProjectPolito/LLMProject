
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
    if not sentence:
        return ""

    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)


def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_words():
    assert words_in_sentence("This is a long sentence") == ""

def test_all_prime_words():
    assert words_in_sentence("This is a test") == "is a"

def test_mixed_prime_words():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_leading_trailing_spaces():
    assert words_in_sentence("  This is a test  ") == "is a"

def test_multiple_spaces():
    assert words_in_sentence("This  is   a    test") == "is a"

def test_single_word_prime():
    assert words_in_sentence("This") == "This"

def test_single_word_non_prime():
    assert words_in_sentence("Testing") == ""

def test_sentence_length_constraint():
    long_sentence = "a" * 101
    assert words_in_sentence(long_sentence) == "" # or handle the exception if needed

def test_invalid_characters():
    sentence_with_numbers = "This is a test1"
    assert words_in_sentence(sentence_with_numbers) == ""