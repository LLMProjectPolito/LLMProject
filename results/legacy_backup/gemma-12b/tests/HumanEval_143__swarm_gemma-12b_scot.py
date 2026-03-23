import pytest
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def test_empty_sentence():
    """Test case for an empty sentence."""
    sentence = ""
    assert words_in_sentence(sentence) == ""

def test_sentence_with_no_prime_length_words():
    """Test case where no words have prime length."""
    sentence = "this is a test"
    assert words_in_sentence(sentence) == ""

def test_sentence_with_only_one_prime_length_word():
    """Test case with only one prime length word."""
    sentence = "a very long sentence"
    assert words_in_sentence(sentence) == "a"

def test_sentence_with_multiple_prime_length_words_at_start():
    """Test case with multiple prime length words at the beginning."""
    sentence = "go for swimming"
    assert words_in_sentence(sentence) == "go for"

def test_sentence_with_multiple_prime_length_words_mixed():
    """Test case with multiple prime length words mixed."""
    sentence = "This is a test sentence"
    assert words_in_sentence(sentence) == "is a"

def test_sentence_with_long_prime_length_word():
    """Test case with a long prime length word."""
    sentence = "This is a verylongword test"
    assert words_in_sentence(sentence) == "verylongword"

def test_sentence_with_repeated_prime_length_words():
    """Test case with repeated prime length words."""
    sentence = "go go go"
    assert words_in_sentence(sentence) == "go go go"