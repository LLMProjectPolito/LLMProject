import pytest
import math

def test_basic():
    assert simplify("1/5", "5/1") == True

import pytest

def test_edge():
    assert simplify("1/1", "1/1") == True
    assert simplify("0/1", "1/1") == True
    assert simplify("1/1", "0/1") == True
    assert simplify("0/1", "0/1") == True
    assert simplify("1/2", "2/1") == True
    assert simplify("1/3", "3/1") == True
    assert simplify("1/4", "4/1") == True
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
    assert simplify("1/100", "100/1") == True
    assert simplify("1/1000", "1000/1") == True
    assert simplify("1/2", "1/2") == True
    assert simplify("2/4", "1/2") == True
    assert simplify("4/8", "1/2") == True
    assert simplify("1/1", "2/1") == False

import pytest

def test_simplify_invalid_fraction_format():
    """Test with invalid fraction format."""
    with pytest.raises(ValueError):
        simplify("1/a", "1/1")
    with pytest.raises(ValueError):
        simplify("a/1", "1/1")
    with pytest.raises(ValueError):
        simplify("1", "1/1")