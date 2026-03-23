import pytest
import math

def test_get_max_triples():
    assert get_max_triples(5) == 1

def test_edge_n_equals_1(n):
    from solution import get_max_triples
    assert get_max_triples(1) == 0

def test_get_max_triples_invalid_input():
    """Test with n = 0, which should return 0."""
    from your_module import get_max_triples  # Replace your_module
    assert get_max_triples(0) == 0