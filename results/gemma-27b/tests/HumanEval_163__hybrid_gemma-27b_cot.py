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
    assert generate_integers(16, 16) == [16]

def test_generate_integers_a_greater_than_b():
    assert generate_integers(18, 12) == [12, 14, 16, 18]

def test_generate_integers_edge_case_1():
    assert generate_integers(0, 1) == []

def test_generate_integers_edge_case_2():
    assert generate_integers(1, 0) == []

def test_generate_integers_edge_case_3():
    assert generate_integers(2, 1) == []

def test_generate_integers_edge_case_4():
    assert generate_integers(1, 2) == [2]

def test_generate_integers_with_zero():
    assert generate_integers(0, 2) == [2]

def test_generate_integers_with_zero_descending():
    assert generate_integers(2, 0) == [2]

def test_generate_integers_large_numbers():
    assert generate_integers(2000, 2008) == [2000, 2002, 2004, 2006, 2008]

def test_generate_integers_large_numbers_descending():
    assert generate_integers(2008, 2000) == [2000, 2002, 2004, 2006, 2008]

def test_generate_integers_range_with_odd_and_even():
    assert generate_integers(11, 16) == [12, 14, 16]

def test_generate_integers_range_with_odd_and_even_descending():
    assert generate_integers(16, 11) == [12, 14, 16]

def test_generate_integers_a_equals_b_even():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_a_equals_b_odd():
    assert generate_integers(5, 5) == []