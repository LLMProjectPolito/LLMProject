import pytest

def test_get_max_triples_empty():
    assert get_max_triples(0) == 0

def test_get_max_triples_small():
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 0

def test_get_max_triples_example():
    assert get_max_triples(5) == 1

def test_get_max_triples_n6():
    assert get_max_triples(6) == 20

def test_get_max_triples_n7():
    assert get_max_triples(7) == 35

def test_get_max_triples_n8():
    assert get_max_triples(8) == 56

def test_get_max_triples_n9():
    assert get_max_triples(9) == 84

def test_get_max_triples_n10():
    assert get_max_triples(10) == 120

def test_get_max_triples_n11():
    assert get_max_triples(11) == 165

def test_get_max_triples_n12():
    assert get_max_triples(12) == 220

def test_get_max_triples_n13():
    assert get_max_triples(13) == 286

def test_get_max_triples_n14():
    assert get_max_triples(14) == 364

def test_get_max_triples_n15():
    assert get_max_triples(15) == 455