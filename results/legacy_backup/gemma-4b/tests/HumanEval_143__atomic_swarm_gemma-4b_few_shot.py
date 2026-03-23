import pytest
import math

def test_words_in_sentence_basic():
    assert words_in_sentence("This is a test") == "is"

def test_words_in_sentence_empty():
    assert words_in_sentence("") == ""

def test_words_in_sentence_empty():
    assert words_in_sentence("") == ""