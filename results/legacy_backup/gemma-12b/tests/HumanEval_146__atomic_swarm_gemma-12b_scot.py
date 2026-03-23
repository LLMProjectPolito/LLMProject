import pytest
import math

def test_specialFilter_typical_case():
    nums = [33, -2, -3, 45, 21, 109]
    expected = 2
    result = specialFilter(nums)
    assert result == expected

def test_empty_input():
    """Test with an empty input list."""
    assert specialFilter([]) == 0

import pytest

def test_specialFilter_invalid_input_type():
    """Test with a list containing a string."""
    with pytest.raises(TypeError):
        specialFilter([15, "abc", 14])