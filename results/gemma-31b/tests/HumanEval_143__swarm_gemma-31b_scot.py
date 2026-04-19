
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

def test_words_in_sentence_no_primes_including_unit_length():
    """
    Test that words of length 1 (not prime) and composite lengths (e.g., 4)
    are correctly excluded, resulting in an empty string.
    """
    assert words_in_sentence("I have a goal") == ""

def test_words_in_sentence_prime_lengths_edge_cases():
    # 'a' (1): Not prime
    # 'bb' (2): Prime
    # 'ccc' (3): Prime
    # 'dddd' (4): Not prime
    # 'eeeee' (5): Prime
    sentence = "a bb ccc dddd eeeee"
    expected = "bb ccc eeeee"
    assert words_in_sentence(sentence) == expected

def test_words_in_sentence_boundary_primes():
    # Lengths: I(1), do(2), a(1), lot(3), of(2), work(4)
    # Primes: 2, 3, 2
    # Non-Primes: 1, 1, 4
    sentence = "I do a lot of work"
    expected = "do lot of"
    assert words_in_sentence(sentence) == expected