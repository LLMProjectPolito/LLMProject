import pytest
import math

def test_how_many_times_edge_cases():
    """ Test edge cases for the how_many_times function """
    assert how_many_times('a', 'a') == 1  # Single character string
    assert how_many_times('aaaa', 'aaaa') == 1  # Substring equals original string

def test_how_many_times_single_character_subset():
    """ Test case where the substring is a single character and it occurs in the string more than twice. """
    assert how_many_times('abcabcd', 'a') == 2

def test_how_many_times_multiple_occurrences():
    """ Test case where the substring occurs in the string more than twice. """
    assert how_many_times('abcabcd', 'ab') == 2