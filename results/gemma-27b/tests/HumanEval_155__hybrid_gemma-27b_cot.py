import pytest

def test_positive_number():
    assert even_odd_count(123456) == (3, 3)

def test_negative_number():
    assert even_odd_count(-123456) == (3, 3)

def test_zero():
    assert even_odd_count(0) == (1, 0)

def test_single_even_digit():
    assert even_odd_count(2) == (1, 0)

def test_single_odd_digit():
    assert even_odd_count(1) == (0, 1)

def test_mixed_digits():
    assert even_odd_count(12) == (1, 1)
    assert even_odd_count(21) == (1, 1)

def test_large_number():
    assert even_odd_count(1234567890) == (5, 5)

def test_negative_large_number():
    assert even_odd_count(-1234567890) == (5, 5)

def test_number_with_leading_zeros_as_string():
    assert even_odd_count("0012") == (1, 1)

def test_number_with_only_even_digits():
    assert even_odd_count(2468) == (4, 0)

def test_number_with_only_odd_digits():
    assert even_odd_count(13579) == (0, 5)

def test_number_with_repeated_digits():
    assert even_odd_count(2222) == (4, 0)
    assert even_odd_count(1111) == (0, 4)
    assert even_odd_count(1212) == (2, 2)

def test_edge_case_max_int():
    assert even_odd_count(2147483647) == (4, 6)

def test_edge_case_min_int():
    assert even_odd_count(-2147483648) == (1, 7)

def test_number_with_negative_and_positive():
    assert even_odd_count(-123) == (1, 2)
    assert even_odd_count(123) == (1, 2)

def test_max_int():
    assert even_odd_count(2147483647) == (4, 5)

def test_min_int():
    assert even_odd_count(-2147483648) == (4, 5)

def test_edge_case_negative_zero():
    assert even_odd_count(-0) == (1, 0)

def test_string_input_positive():
    assert even_odd_count("123") == (1, 2)

def test_string_input_negative():
    assert even_odd_count("-123") == (1, 2)

def test_string_input_mixed():
    assert even_odd_count("21") == (1, 1)

def test_string_input_zero():
    assert even_odd_count("0") == (1, 0)

def test_string_input_negative_zero():
    assert even_odd_count("-0") == (1, 0)