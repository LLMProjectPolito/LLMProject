import pytest
import math


# Focus: Prime Number Word Lengths
def test_prime_word_lengths_basic():
    assert words_in_sentence("This is a test") == "is"

def test_prime_word_lengths_multiple():
    assert words_in_sentence("lets go for swimming") == "go for"

def test_prime_word_lengths_no_primes():
    assert words_in_sentence("hello world") == ""

# Focus: Empty/Null Input
def test_words_in_sentence_empty():
    assert words_in_sentence("") == ""

def test_words_in_sentence_null():
    assert words_in_sentence(None) == ""

# Focus: Sentence with Non-Space Characters Only
def test_words_in_sentence_non_space_only():
    assert words_in_sentence("abcde") == ""

def test_words_in_sentence_non_space_only_long():
    assert words_in_sentence("abcdefghijk") == ""

def test_words_in_sentence_non_space_only_mixed():
    assert words_in_sentence("aabccddeeffgghhiijjkk") == ""