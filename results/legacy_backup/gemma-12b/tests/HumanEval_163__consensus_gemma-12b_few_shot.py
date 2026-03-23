def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reversed():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_even():
    assert generate_integers(1, 2) == [2]

def test_generate_integers_start_even():
    assert generate_integers(4, 6) == [4, 6]

def test_generate_integers_end_even():
    assert generate_integers(6, 8) == [6, 8]

def test_generate_integers_same_numbers():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_negative_numbers():
    assert generate_integers(-2, 2) == [-2, 0, 2]

def test_generate_integers_zero():
    assert generate_integers(0, 4) == [0, 2, 4]

def test_generate_integers_large_range():
    assert generate_integers(1, 100) == list(range(2, 101, 2))