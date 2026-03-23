import pytest
import math

def find_max(words):
    """
    Finds the longest word in a list of words.
    """
    if not words:
        return None
    return max(words, key=len)

def test_find_max_single_word():
    assert find_max(["hello"]) == "hello"