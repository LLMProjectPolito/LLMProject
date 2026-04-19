
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
def test_words_in_sentence_min_len():
    # Boundary: Minimum sentence length (1)
    # Word length 1 is not prime
    assert words_in_sentence("a") == ""

def test_words_in_sentence_word_len_boundary():
    # Boundary: Primality boundary (1 is not prime, 2 is prime)
    assert words_in_sentence("i am") == "am"

def test_words_in_sentence_max_len():
    # Boundary: Maximum sentence length (100)
    # 100 is not prime
    assert words_in_sentence("a" * 100) == ""

# Focus: Logic Branches
import pytest

def test_words_in_sentence_no_primes():
    # Branch: No words have prime lengths (1 is not prime, 4 is not prime)
    assert words_in_sentence("a test") == ""
    assert words_in_sentence("abcd efgh") == ""

def test_words_in_sentence_all_primes():
    # Branch: All words have prime lengths (2, 3, 5 are prime)
    assert words_in_sentence("is the apple") == "is the apple"
    assert words_in_sentence("go it") == "go it"

def test_words_in_sentence_mixed_primes():
    # Branch: Mixture of prime and non-prime lengths
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"

# Focus: Input Scenarios
import pytest

def test_words_in_sentence_no_primes():
    # Lengths: 'a' (1), 'test' (4) - neither are prime
    assert words_in_sentence("a test") == ""

def test_words_in_sentence_all_primes():
    # Lengths: 'go' (2), 'for' (3), 'it' (2) - all are prime
    assert words_in_sentence("go for it") == "go for it"

def test_words_in_sentence_mixed_with_one():
    # Lengths: 'I' (1), 'am' (2), 'a' (1), 'student' (7) - 2 and 7 are prime
    assert words_in_sentence("I am a student") == "am student"