import pytest
import math

def test_empty_sentence():
    """Test with an empty sentence."""
    from solution import words_in_sentence
    assert words_in_sentence("") == ""