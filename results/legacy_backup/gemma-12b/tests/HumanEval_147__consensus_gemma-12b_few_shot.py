def test_get_max_triples_example():
    assert get_max_triples(5) == 1

def test_get_max_triples_small():
    assert get_max_triples(3) == 0

def test_get_max_triples_another_small():
    assert get_max_triples(4) == 0

def test_get_max_triples_larger():
    assert get_max_triples(6) == 2

def test_get_max_triples_even_larger():
    assert get_max_triples(10) == 6

def test_get_max_triples_n_equals_1():
    assert get_max_triples(1) == 0

def test_get_max_triples_n_equals_2():
    assert get_max_triples(2) == 0