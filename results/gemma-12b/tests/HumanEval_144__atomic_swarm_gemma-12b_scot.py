import pytest
import math

def test_simplify_positive():
    assert simplify("1/5", "5/1") == True

def test_simplify_edge_case_zero_numerator():
    """Test case with zero numerator in both fractions."""
    assert simplify("0/1", "0/1") == True

import pytest

def test_simplify_invalid_fraction_format():
    """Test that the function handles invalid fraction formats gracefully."""
    with pytest.raises(ValueError):
        simplify("1/5", "5")
    with pytest.raises(ValueError):
        simplify("1", "5/1")
    with pytest.raises(ValueError):
        simplify("1/5", "5/0")