import pytest

def test_get_max_triples_empty():
    assert get_max_triples(0) == 0

def test_get_max_triples_one():
    assert get_max_triples(1) == 0

def test_get_max_triples_two():
    assert get_max_triples(2) == 0

def test_get_max_triples_three():
    assert get_max_triples(3) == 1

def test_get_max_triples_four():
    assert get_max_triples(4) == 1

def test_get_max_triples_five():
    assert get_max_triples(5) == 1

def test_get_max_triples_six():
    assert get_max_triples(6) == 3

def test_get_max_triples_seven():
    assert get_max_triples(7) == 6

def test_get_max_triples_eight():
    assert get_max_triples(8) == 10

def test_get_max_triples_nine():
    assert get_max_triples(9) == 16

def test_get_max_triples_ten():
    assert get_max_triples(10) == 22

def test_get_max_triples_large():
    assert get_max_triples(100) == 161700

def test_get_max_triples_mod_0():
    n = 30
    assert get_max_triples(n) == 4350

def test_get_max_triples_mod_1():
    n = 31
    assert get_max_triples(n) == 4684

def test_get_max_triples_mod_2():
    n = 32
    assert get_max_triples(n) == 5053