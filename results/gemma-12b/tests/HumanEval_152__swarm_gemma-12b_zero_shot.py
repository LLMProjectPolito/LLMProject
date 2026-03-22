import pytest
import math

def test_compare_empty_lists():
    """Test with empty lists to ensure no errors and correct behavior."""
    assert compare([], []) == []