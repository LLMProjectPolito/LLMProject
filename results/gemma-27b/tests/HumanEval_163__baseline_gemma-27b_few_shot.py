
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reversed():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_even():
    assert generate_integers(2, 3) == [2]

def test_generate_integers_same_number_even():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_same_number_odd():
    assert generate_integers(3, 3) == []

def test_generate_integers_large_range():
    assert generate_integers(1, 10) == [2, 4, 6, 8, 10]

def test_generate_integers_large_range_reversed():
    assert generate_integers(10, 1) == [2, 4, 6, 8, 10]

def test_generate_integers_negative_numbers():
    assert generate_integers(-2, 2) == [2]

def test_generate_integers_mixed_numbers():
    assert generate_integers(-1, 5) == [2, 4]