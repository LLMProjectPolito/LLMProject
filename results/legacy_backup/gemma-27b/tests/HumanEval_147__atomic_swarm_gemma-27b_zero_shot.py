import pytest
import math

def test_basic():
    assert get_max_triples(5) == 1

def test_edge():
    assert get_max_triples(0) == 0

def test_get_max_triples_negative_input():
    import pytest
    from your_module import get_max_triples  # Replace your_module

    with pytest.raises(ValueError):
        get_max_triples(-1)