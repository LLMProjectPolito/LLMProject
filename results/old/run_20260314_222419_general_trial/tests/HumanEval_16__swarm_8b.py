import pytest
import math

def test_count_distinct_characters_empty_string():
    """Check if the function correctly handles an empty string."""
    assert count_distinct_characters("") == 0