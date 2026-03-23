import pytest
import math

def test_get_max_triples_basic():
    assert get_max_triples(5) == 1

def test_get_max_triples_edge_case():
    assert get_max_triples(1) == 0

def test_get_max_triples_n_1():
    assert get_max_triples(1) == 0