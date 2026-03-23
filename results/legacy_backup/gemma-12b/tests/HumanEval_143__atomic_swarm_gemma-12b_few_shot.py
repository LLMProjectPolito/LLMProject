import pytest
import math

def test_words_in_sentence_basic():
    assert words_in_sentence("This is a test") == "is"

def test_words_in_sentence_empty_sentence():
    assert words_in_sentence("") == ""

def test_words_in_sentence_non_string_input():
    assert words_in_sentence(123) == ""