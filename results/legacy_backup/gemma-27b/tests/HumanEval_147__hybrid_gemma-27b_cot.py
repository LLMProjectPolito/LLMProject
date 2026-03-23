import pytest

def test_get_max_triples_empty():
    assert get_max_triples(0) == 0

def test_get_max_triples_small():
    assert get_max_triples(1) == 0
    assert get_max_triples(2) == 0
    assert get_max_triples(3) == 1

def test_get_max_triples_example():
    assert get_max_triples(5) == 1

def test_get_max_triples_n_6():
    assert get_max_triples(6) == 5

def test_get_max_triples_n_7():
    assert get_max_triples(7) == 15

def test_get_max_triples_n_8():
    assert get_max_triples(8) == 28

def test_get_max_triples_n_9():
    assert get_max_triples(9) == 45

def test_get_max_triples_n_10():
    assert get_max_triples(10) == 78

def test_get_max_triples_n_11():
    assert get_max_triples(11) == 117

def test_get_max_triples_n_12():
    assert get_max_triples(12) == 176

def test_get_max_triples_n_13():
    assert get_max_triples(13) == 253

def test_get_max_triples_n_14():
    assert get_max_triples(14) == 345

def test_get_max_triples_n_15():
    assert get_max_triples(15) == 455

def test_get_max_triples_four():
    assert get_max_triples(4) == 1

def test_get_max_triples_large():
    assert get_max_triples(100) == 161700

def test_get_max_triples_mod_0():
    n = 30
    assert get_max_triples(n) == 4495

def test_get_max_triples_mod_1():
    n = 31
    assert get_max_triples(n) == 4960

def test_get_max_triples_mod_2():
    n = 32
    assert get_max_triples(n) == 5426