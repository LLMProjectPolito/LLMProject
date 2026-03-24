import pytest
from your_module import get_max_triples  # Replace your_module

def test_get_max_triples_example():
    assert get_max_triples(5) == 1

def test_get_max_triples_small_n():
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0
    assert get_max_triples(4) == 0

def test_get_max_triples_n_equals_6():
    assert get_max_triples(6) == 2

def test_get_max_triples_n_equals_7():
    assert get_max_triples(7) == 3

def test_get_max_triples_n_equals_8():
    assert get_max_triples(8) == 4

def test_get_max_triples_n_equals_9():
    assert get_max_triples(9) == 6

def test_get_max_triples_n_equals_10():
    assert get_max_triples(10) == 8

def test_get_max_triples_large_n():
    assert get_max_triples(100) == 1617

def test_get_max_triples_n_equals_15():
    assert get_max_triples(15) == 225

def test_get_max_triples_n_equals_20():
    assert get_max_triples(20) == 410