import pytest
from your_module import get_max_triples  # Replace your_module

def test_get_max_triples_small():
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0
    assert get_max_triples(4) == 1
    assert get_max_triples(5) == 1

def test_get_max_triples_medium():
    assert get_max_triples(6) == 2
    assert get_max_triples(7) == 3
    assert get_max_triples(8) == 4
    assert get_max_triples(9) == 6
    assert get_max_triples(10) == 8
    assert get_max_triples(11) == 10
    assert get_max_triples(12) == 13

def test_get_max_triples_patterns():
    # Test cases designed to check for patterns related to modulo 3
    assert get_max_triples(15) == 24
    assert get_max_triples(18) == 32

def test_get_max_triples_large():
    assert get_max_triples(100) == 1667
    assert get_max_triples(200) == 3334
    assert get_max_triples(500) == 8334

def test_get_max_triples_edge_cases():
    with pytest.raises(ValueError):
        get_max_triples(0)
    with pytest.raises(ValueError):
        get_max_triples(-1)