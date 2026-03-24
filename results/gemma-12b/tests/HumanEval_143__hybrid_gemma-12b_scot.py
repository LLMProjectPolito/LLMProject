
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
    words = sentence.split()
    prime_words = [word for word in words if is_prime(len(word))]
    return " ".join(prime_words)

def test_empty_sentence():
    assert words_in_sentence("") == ""

def test_no_prime_words():
    assert words_in_sentence("this is not a prime sentence") == ""

def test_all_prime_words():
    assert words_in_sentence("a is i") == "a is i"
    assert words_in_sentence("go for a swim") == "go for a"
    assert words_in_sentence("to be or not") == "to be or"

def test_mixed_words():
    assert words_in_sentence("This is a test sentence") == "is a"
    assert words_in_sentence("This is a test") == "is"

def test_leading_trailing_spaces():
    assert words_in_sentence("  This is a test  ") == "is"

def test_multiple_spaces():
    assert words_in_sentence("This  is   a    test") == "is"

def test_single_prime_word():
    assert words_in_sentence("go") == "go"

def test_single_letter_prime():
    assert words_in_sentence("a b c d e") == "a b c d e"

def test_longer_prime_word():
    assert words_in_sentence("This is a very long prime word") == "This is a very long"