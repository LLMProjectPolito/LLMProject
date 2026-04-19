
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

def test_words_in_sentence_examples():
    """Test the examples provided in the problem description."""
    assert words_in_sentence("This is a test") == "is"
    assert words_in_sentence("lets go for swimming") == "go for"

def test_words_in_sentence_no_primes():
    """Test sentences where no words have prime lengths."""
    # lengths: 1, 4, 6 (none are prime)
    assert words_in_sentence("a test street") == ""
    # length: 4
    assert words_in_sentence("word") == ""

def test_words_in_sentence_all_primes():
    """Test sentences where all words have prime lengths."""
    # lengths: 2, 3, 5 (all prime)
    assert words_in_sentence("go for apple") == "go for apple"

def test_words_in_sentence_length_one():
    """Test that words of length 1 are not treated as prime."""
    # lengths: 1, 1, 1
    assert words_in_sentence("I a o") == ""

def test_words_in_sentence_single_word_boundaries():
    """Test single word inputs and boundary constraints (merged)."""
    # length 1 (not prime)
    assert words_in_sentence("a") == ""
    # length 2 (prime)
    assert words_in_sentence("is") == "is"
    # length 4 (not prime)
    assert words_in_sentence("test") == ""

def test_words_in_sentence_various_primes():
    """Test a variety of prime lengths (2, 3, 5, 7, 11)."""
    # lengths: 2 (is), 3 (the), 5 (great), 7 (amazing), 11 (extraordinary)
    sentence = "is the great amazing extraordinary"
    assert words_in_sentence(sentence) == "is the great amazing extraordinary"

def test_words_in_sentence_mixed_lengths():
    """Test a mix of prime and non-prime lengths."""
    # lengths: 3 (The - P), 5 (quick - P), 5 (brown - P), 3 (fox - P), 
    # 5 (jumps - P), 4 (over - NP), 3 (the - P), 4 (lazy - NP), 3 (dog - P)
    sentence = "The quick brown fox jumps over the lazy dog"
    expected = "The quick brown fox jumps the dog"
    assert words_in_sentence(sentence) == expected

def test_words_in_sentence_max_length():
    """Test a sentence approaching the maximum length of 100 characters."""
    # Create a string of 10 words of length 9 (non-prime) and 1 word of length 2 (prime)
    sentence = "ninechars " * 10 + "is"
    assert words_in_sentence(sentence) == "is"

def test_words_in_sentence_empty():
    """Test that an empty string returns an empty string."""
    assert words_in_sentence("") == ""

def test_words_in_sentence_whitespace():
    """Test handling of leading, trailing, and multiple consecutive spaces."""
    # Should ignore extra whitespace and not return double spaces in output
    assert words_in_sentence("  go   for  ") == "go for"
    assert words_in_sentence("   ") == ""

def test_words_in_sentence_punctuation():
    """
    Test how punctuation is handled. 
    Assuming punctuation is counted as part of the word length.
    """
    # "Hello!" length is 6 (not prime)
    assert words_in_sentence("Hello!") == ""
    # "Hi!" length is 3 (prime)
    assert words_in_sentence("Hi!") == "Hi!"
    # "Wait..." length is 7 (prime)
    assert words_in_sentence("Wait...") == "Wait..."