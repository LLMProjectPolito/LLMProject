import pytest
import math

def test_empty_list():
    """Test with an empty list to ensure no errors and a sensible default."""
    assert find_max([]) == ""