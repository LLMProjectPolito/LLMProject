import pytest
import math

def test_cycpattern_check_empty_pattern():
    """Test case: First word is non-empty, second word is empty."""
    assert cycpattern_check("abc", "") is False