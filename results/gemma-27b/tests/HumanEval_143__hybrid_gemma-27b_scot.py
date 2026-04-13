
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
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_length_words():
    assert words_in_sentence("this is a test") == ""

def test_only_prime_length_words():
    assert words_in_sentence("is a") == "is a"

def test_mixed_prime_and_non_prime_length_words():
    assert words_in_sentence("This is a test") == "is"

def test_single_prime_length_word():
    assert words_in_sentence("go") == "go"

def test_single_non_prime_length_word():
    assert words_in_sentence("test") == ""

def test_leading_and_trailing_spaces():
    assert words_in_sentence("  This is a test  ") == "is"

def test_multiple_spaces_between_words():
    assert words_in_sentence("This  is   a    test") == "is"

def test_example_1():
    assert words_in_sentence("This is a test") == "is"

def test_example_2():
    assert words_in_sentence("lets go for swimming") == "go for"