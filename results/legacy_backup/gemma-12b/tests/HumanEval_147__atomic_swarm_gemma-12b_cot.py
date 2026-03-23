import pytest
import math

def test_get_max_triples():
    assert get_max_triples(5) == 1

def test_get_max_triples_empty():
    """Test with n = 0, which should return 0."""
    assert get_max_triples(0) == 0

import pytest
from your_module import get_max_triples  # Replace your_module

def test_negative_input():
    with pytest.raises(ValueError):
        get_max_triples(-1)

def test_zero_input():
    with pytest.raises(ValueError):
        get_max_triples(0)

def test_large_input():
    assert get_max_triples(1000) == 166666

def test_small_input():
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0
    assert get_max_triples(4) == 1
    assert get_max_triples(5) == 1
    assert get_max_triples(6) == 3