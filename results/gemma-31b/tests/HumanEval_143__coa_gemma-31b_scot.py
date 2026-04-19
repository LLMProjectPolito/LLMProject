
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
import pytest

def test_words_in_sentence_min_length():
    # Boundary: Minimum sentence length (1)
    # Length 1 is not a prime number
    assert words_in_sentence("a") == ""

def test_words_in_sentence_max_length():
    # Boundary: Maximum sentence length (100)
    # 97 is prime, 2 is prime. Total length: 97 + 1 (space) + 2 = 100
    sentence = "a" * 97 + " " + "bc"
    assert words_in_sentence(sentence) == sentence

def test_words_in_sentence_primality_boundary():
    # Boundary: Word lengths 1 (not prime) and 2 (smallest prime)
    assert words_in_sentence("i am a") == "am"

# Focus: Logic Branches
def test_words_in_sentence_no_primes():
    # Tests the branch where no words have prime lengths (including length 1)
    assert words_in_sentence("a test") == ""

def test_words_in_sentence_all_primes():
    # Tests the branch where all words have prime lengths
    assert words_in_sentence("is it ok") == "is it ok"

def test_words_in_sentence_mixed_primes():
    # Tests the branch with a mix of prime and non-prime lengths
    assert words_in_sentence("apple banana cherry") == "apple"

# Focus: Edge Cases
import pytest

def test_words_in_sentence_no_primes():
    # Words of length 1 and 4 are not prime
    assert words_in_sentence("a test") == ""
    # All words of length 1
    assert words_in_sentence("a b c d") == ""

def test_words_in_sentence_all_primes():
    # Lengths: 2, 3, 2 (all prime)
    assert words_in_sentence("go for it") == "go for it"
    # Length: 5 (prime)
    assert words_in_sentence("hello") == "hello"

def test_words_in_sentence_single_char():
    # Length 1 is not a prime number
    assert words_in_sentence("a") == ""