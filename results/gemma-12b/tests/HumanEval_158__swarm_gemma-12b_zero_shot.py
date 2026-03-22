import pytest
import math

def test_empty_list():
    """Test with an empty list - should return None."""
    assert find_max([]) is None