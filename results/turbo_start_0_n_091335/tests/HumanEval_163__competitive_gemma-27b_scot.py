import pytest

def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_digit_range():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_single_digit_range_odd():
    assert generate_integers(3, 3) == []

def test_generate_integers_larger_range():
    assert generate_integers(12, 20) == [12, 14, 16, 18, 20]

def test_generate_integers_larger_range_descending():
    assert generate_integers(20, 12) == [12, 14, 16, 18, 20]

def test_generate_integers_same_number():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_a_greater_than_b():
    assert generate_integers(16, 10) == [10, 12, 14, 16]

def test_generate_integers_empty_range():
    assert generate_integers(1, 1) == []

def test_generate_integers_start_odd_end_odd():
    assert generate_integers(1, 3) == []

def test_generate_integers_start_even_end_odd():
    assert generate_integers(2, 3) == [2]

def test_generate_integers_start_odd_end_even():
    assert generate_integers(1, 4) == [2, 4]

def test_generate_integers_large_numbers():
    assert generate_integers(2000, 2008) == [2000, 2002, 2004, 2006, 2008]