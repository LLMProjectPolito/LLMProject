def test_get_max_triples_n1():
    assert get_max_triples(1) == 0

def test_get_max_triples_n2():
    assert get_max_triples(2) == 0

def test_get_max_triples_n3():
    assert get_max_triples(3) == 0

def test_get_max_triples_n4():
    assert get_max_triples(4) == 0

def test_get_max_triples_n5():
    assert get_max_triples(5) == 1

def test_get_max_triples_n6():
    assert get_max_triples(6) == 2

def test_get_max_triples_n7():
    assert get_max_triples(7) == 4

def test_get_max_triples_n8():
    assert get_max_triples(8) == 7

def test_get_max_triples_n9():
    assert get_max_triples(9) == 12