import pytest
import math


# Focus: Boundary Values
def test_get_max_triples_boundary_small():
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 1

def test_get_max_triples_boundary_large():
    assert get_max_triples(100) == 161700
    assert get_max_triples(1000) == 166167000

# Focus: Equivalence Partitioning
def test_get_max_triples_n_mod_3_is_0():
    assert get_max_triples(3) == 1

def test_get_max_triples_n_mod_3_is_1():
    assert get_max_triples(4) == 1

def test_get_max_triples_n_mod_3_is_2():
    assert get_max_triples(5) == 1

# Focus: Large Input/Performance
import pytest
import time

def test_get_max_triples_large_n(benchmark):
    n = 1000
    result = benchmark(get_max_triples, n)
    assert isinstance(result, int)

def test_get_max_triples_very_large_n(benchmark):
    n = 5000
    result = benchmark(get_max_triples, n)
    assert isinstance(result, int)