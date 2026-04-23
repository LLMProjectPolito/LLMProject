
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

def test_provided_examples():
    """Tests the examples provided in the problem description."""
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"

def test_prime_logic():
    """Tests various combinations of prime and non-prime word lengths."""
    # All prime: lengths 2, 3, 2
    assert words_in_sentence("is the at") == "is the at"
    # All prime: lengths 5, 7
    assert words_in_sentence("apple amazing") == "apple amazing"
    # No primes: lengths 4, 4, 4
    assert words_in_sentence("abcd efgh ijkl") == ""
    # Mixed: lengths 1, 2, 1, 3, 4, 5 -> primes: 2, 3, 5
    # This also verifies that length 1 is not treated as prime.
    assert words_in_sentence("a is a cat test apple") == "is cat apple"

def test_empty_string():
    """Tests that an empty string returns an empty string."""
    assert words_in_sentence("") == ""

def test_whitespace_handling():
    """
    Tests how the function handles irregular spacing.
    Ensures leading, trailing, and multiple consecutive spaces do not 
    result in empty strings or extra spaces in the output.
    """
    assert words_in_sentence("  is  cat  ") == "is cat"
    assert words_in_sentence("is    cat") == "is cat"
    assert words_in_sentence("is cat ") == "is cat"

def test_punctuation_handling():
    """
    Tests if punctuation is treated as part of the word's length.
    """
    # "is," (len 3, prime), "cat!" (len 4, not prime)
    assert words_in_sentence("is, cat!") == "is,"
    # "hi," (len 3, prime), "there!" (len 6, not prime)
    assert words_in_sentence("hi, there!") == "hi,"

def test_numeric_strings():
    """
    Tests if the function correctly treats digits as characters when calculating length.
    """
    # "123" (len 3, prime), "4567" (len 4, not prime)
    assert words_in_sentence("123 4567") == "123"
    # "12" (len 2, prime), "345" (len 3, prime)
    assert words_in_sentence("12 345") == "12 345"

def test_large_prime_length():
    """Tests words with larger prime lengths within the constraint."""
    # length 11 is prime
    assert words_in_sentence("elevenwords") == "elevenwords"
    # length 13 is prime
    assert words_in_sentence("thirteentexts") == "thirteentexts"

def test_boundary_constraints():
    """Tests the smallest possible word lengths."""
    # Smallest prime lengths
    assert words_in_sentence("ab") == "ab"   # length 2 is prime
    assert words_in_sentence("abc") == "abc" # length 3 is prime
    # Smallest non-prime length (greater than 1)
    assert words_in_sentence("abcd") == ""   # length 4 is not prime