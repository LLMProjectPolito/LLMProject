import pytest

def test_get_max_triples_1():
    assert get_max_triples(1) == 0

def test_get_max_triples_2():
    assert get_max_triples(2) == 0

def test_get_max_triples_3():
    assert get_max_triples(3) == 1

def test_get_max_triples_4():
    assert get_max_triples(4) == 1

def test_get_max_triples_5():
    assert get_max_triples(5) == 1

def test_get_max_triples_6():
    assert get_max_triples(6) == 3

def test_get_max_triples_7():
    assert get_max_triples(7) == 6

def test_get_max_triples_8():
    assert get_max_triples(8) == 10

def test_get_max_triples_9():
    assert get_max_triples(9) == 16

def test_get_max_triples_10():
    assert get_max_triples(10) == 22

def test_get_max_triples_11():
    assert get_max_triples(11) == 29

def test_get_max_triples_12():
    assert get_max_triples(12) == 37

def test_get_max_triples_13():
    assert get_max_triples(13) == 46

def test_get_max_triples_14():
    assert get_max_triples(14) == 56

def test_get_max_triples_15():
    assert get_max_triples(15) == 67

def test_get_max_triples_20():
    assert get_max_triples(20) == 134

def test_get_max_triples_30():
    assert get_max_triples(30) == 335

def test_get_max_triples_50():
    assert get_max_triples(50) == 824