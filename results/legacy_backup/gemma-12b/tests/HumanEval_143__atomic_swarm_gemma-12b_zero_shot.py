import pytest
import math

def test_words_in_sentence_positive():
    from main import words_in_sentence
    sentence = "This is a test"
    expected = "is"
    assert words_in_sentence(sentence) == expected

def test_empty_sentence():
    from solution import words_in_sentence
    assert words_in_sentence("") == ""

def test_words_in_sentence_empty_sentence():
    """Test with an empty sentence."""
    from main import words_in_sentence
    assert words_in_sentence("") == ""