import pytest
import math

def test_words_in_sentence_leading_and_trailing_spaces():
    assert words_in_sentence("  hello world  ") == ""