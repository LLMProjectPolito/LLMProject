
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

def test_words_in_sentence_min_boundary():
    # Minimum length sentence (1), length 1 is not prime
    assert words_in_sentence("a") == ""

def test_words_in_sentence_smallest_prime_boundary():
    # Smallest possible prime length word (2)
    assert words_in_sentence("is") == "is"

def test_words_in_sentence_max_boundary_prime():
    # Maximum length sentence (100), using a prime length word (97)
    sentence = "a" * 97
    assert words_in_sentence(sentence) == sentence

# Focus: Prime Number Scenarios
import pytest

def test_words_with_prime_lengths():
    # Lengths: 1 (no), 2 (yes), 3 (yes), 4 (no), 5 (yes)
    assert words_in_sentence("a bb ccc dddd eeeee") == "bb ccc eeeee"
    # Lengths: 1 (no), 2 (yes), 1 (no), 7 (yes)
    assert words_in_sentence("i am a student") == "am student"

def test_words_with_no_prime_lengths():
    # Lengths: 1 (no), 4 (no), 6 (no), 8 (no), 9 (no)
    assert words_in_sentence("a test street mountain something") == ""

def test_words_with_all_prime_lengths():
    # Lengths: 2 (yes), 3 (yes), 5 (yes), 7 (yes)
    assert words_in_sentence("is the apple quality") == "is the apple quality"

# Focus: Logic Branches
import pytest

def test_words_in_sentence_no_primes():
    # Tests the branch where no words have prime lengths (1 is not prime, 4 is not prime)
    assert words_in_sentence("a b dddd") == ""

def test_words_in_sentence_all_primes():
    # Tests the branch where all words have prime lengths (2, 3, 5)
    assert words_in_sentence("is the apple") == "is the apple"

def test_words_in_sentence_mixed_primes():
    # Tests the branch with a mix of prime (2, 3) and non-prime (1, 4) lengths
    assert words_in_sentence("a is the test") == "is the"