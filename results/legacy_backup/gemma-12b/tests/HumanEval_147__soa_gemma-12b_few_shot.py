import pytest

def test_get_max_triples_example():
    assert get_max_triples(5) == 1

def test_get_max_triples_small():
    assert get_max_triples(3) == 0

def test_get_max_triples_n_equals_1():
    assert get_max_triples(1) == 0

def test_get_max_triples_n_equals_2():
    assert get_max_triples(2) == 0

def test_get_max_triples_n_equals_4():
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