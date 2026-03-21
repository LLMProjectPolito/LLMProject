import pytest
import math

def test_words_string_single_comma():
    """Test if a single word with comma delimiter is correctly split."""
    assert words_string("Hello,") == ["Hello"]

def test_words_string_empty_input():
    """Test the function with an empty input string."""
    assert words_string("") == []