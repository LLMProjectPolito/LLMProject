
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
def test_words_in_sentence_min_length():
    # Boundary: Minimum allowed sentence length (1), word length 1 is not prime
    assert words_in_sentence("a") == ""

def test_words_in_sentence_max_length():
    # Boundary: Maximum allowed sentence length (100), word length 100 is not prime
    assert words_in_sentence("a" * 100) == ""

def test_words_in_sentence_smallest_prime_length():
    # Boundary: Smallest possible prime word length (2)
    assert words_in_sentence("ab") == "ab"

# Focus: Logic Branches
def test_words_in_sentence_no_primes():
    # Tests the branch where no words have prime lengths (including length 1)
    assert words_in_sentence("a test four") == ""

def test_words_in_sentence_all_primes():
    # Tests the branch where all words have prime lengths
    assert words_in_sentence("go for") == "go for"

def test_words_in_sentence_mixed_branches():
    # Tests the branch with a mix of prime lengths, non-prime lengths, and length 1
    assert words_in_sentence("a go for swimming") == "go for"

# Focus: Input Scenarios
import pytest

def test_words_in_sentence_no_primes():
    # Scenario: No words have prime lengths (1 is not prime, 4 is not prime)
    assert words_in_sentence("a test") == ""

def test_words_in_sentence_all_primes():
    # Scenario: All words have prime lengths (2 and 3 are prime)
    assert words_in_sentence("go for") == "go for"

def test_words_in_sentence_mixed_lengths():
    # Scenario: Mix of prime (2, 7) and non-prime (1, 1) lengths
    assert words_in_sentence("I am a student") == "am student"