import pytest
import math

def test_get_max_triples_basic():
    assert get_max_triples(5) == 1

def test_get_max_triples_empty():
    assert get_max_triples(0) == 0

def test_get_max_triples_large():
    assert get_max_triples(300) == 4500