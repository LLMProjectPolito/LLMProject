import pytest

def test_get_max_triples_small_input():
    assert get_max_triples(5) == 1

def test_get_max_triples_medium_input():
    assert get_max_triples(10) == 4

def test_get_max_triples_large_input():
    assert get_max_triples(20) == 16

def test_get_max_triples_edge_case():
    assert get_max_triples(1) == 0

def test_get_max_triples_invalid_input():
    with pytest.raises(TypeError):
        get_max_triples("10")

def test_get_max_triples_negative_input():
    with pytest.raises(ValueError):
        get_max_triples(-10)

def test_get_max_triples_zero_input():
    with pytest.raises(ValueError):
        get_max_triples(0)