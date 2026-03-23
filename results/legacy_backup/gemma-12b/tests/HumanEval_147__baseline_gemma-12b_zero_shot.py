import pytest
from your_module import get_max_triples  # Replace your_module

def test_get_max_triples_n_5():
    assert get_max_triples(5) == 1

def test_get_max_triples_n_6():
    assert get_max_triples(6) == 2

def test_get_max_triples_n_7():
    assert get_max_triples(7) == 3

def test_get_max_triples_n_8():
    assert get_max_triples(8) == 4

def test_get_max_triples_n_9():
    assert get_max_triples(9) == 6

def test_get_max_triples_n_10():
    assert get_max_triples(10) == 8

def test_get_max_triples_n_1():
    assert get_max_triples(1) == 0

def test_get_max_triples_n_2():
    assert get_max_triples(2) == 0

def test_get_max_triples_n_3():
    assert get_max_triples(3) == 0

def test_get_max_triples_n_4():
    assert get_max_triples(4) == 0

def test_get_max_triples_n_11():
    assert get_max_triples(11) == 11

def test_get_max_triples_n_12():
    assert get_max_triples(12) == 15

def test_get_max_triples_large_n():
    assert get_max_triples(100) == 3333

def test_get_max_triples_n_15():
    assert get_max_triples(15) == 23

def test_get_max_triples_n_20():
    assert get_max_triples(20) == 46