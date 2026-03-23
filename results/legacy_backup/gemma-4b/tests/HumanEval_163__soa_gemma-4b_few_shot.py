def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []
    assert generate_integers(1, 1) == []
    assert generate_integers(2, 2) == [2]
    assert generate_integers(4, 4) == [4]

def test_generate_integers_range():
    assert generate_integers(1, 5) == [2, 4]
    assert generate_integers(5, 1) == [2, 4]
    assert generate_integers(1, 6) == [2, 4]

def test_generate_integers_no_even():
    assert generate_integers(1, 3) == []
    assert generate_integers(3, 1) == []

def test_generate_integers_with_zero():
    assert generate_integers(0, 4) == [0, 2, 4]
    assert generate_integers(4, 0) == [0, 2, 4]