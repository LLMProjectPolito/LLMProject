import pytest

def test_generate_integers_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reversed():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_even():
    assert generate_integers(2, 3) == [2]

def test_generate_integers_single_odd():
    assert generate_integers(1, 2) == [2]

def test_generate_integers_same_number_even():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_same_number_odd():
    assert generate_integers(3, 3) == []

def test_generate_integers_large_range():
    assert generate_integers(1, 100) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

def test_generate_integers_negative_numbers():
    assert generate_integers(-2, 2) == [2]

def test_generate_integers_mixed_numbers():
    assert generate_integers(-1, 5) == [2, 4]