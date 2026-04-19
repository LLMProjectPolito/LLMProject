
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

def test_generate_integers_basic_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_basic_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_out_of_digit_range():
    assert generate_integers(10, 14) == []

def test_generate_integers_mixed_range():
    # Range starts with digits and goes into double digits
    assert generate_integers(4, 12) == [4, 6, 8]
    # Range starts with double digits and ends with digits
    assert generate_integers(12, 4) == [4, 6, 8]

def test_generate_integers_single_value_even():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_single_value_odd():
    assert generate_integers(3, 3) == []

def test_generate_integers_no_evens_in_range():
    assert generate_integers(1, 1) == []
    assert generate_integers(7, 7) == []

def test_generate_integers_small_range():
    assert generate_integers(3, 5) == [4]
    assert generate_integers(5, 3) == [4]

def test_generate_integers_full_digit_set():
    # Testing the full range of even digits
    assert generate_integers(0, 9) == [0, 2, 4, 6, 8]