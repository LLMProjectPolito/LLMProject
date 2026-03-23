import pytest
import math

def test_find_max_typical():
    words = ["name", "of", "string"]
    assert find_max(words) == "string"

def test_empty_input():
    """Test with an empty list as input."""
    from solution import find_max
    assert find_max([]) == ""

import pytest

def test_empty_list():
    """Test with an empty list as input."""
    assert find_max([]) == ""