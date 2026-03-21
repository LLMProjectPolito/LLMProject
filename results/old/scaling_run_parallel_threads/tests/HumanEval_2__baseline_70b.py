import pytest

def test_truncate_number_positive():
    assert truncate_number(3.5) == 0.5

def test_truncate_number_integer():
    assert truncate_number(3.0) == 0.0

def test_truncate_number_zero():
    assert truncate_number(0.0) == 0.0

def test_truncate_number_negative():
    with pytest.raises(ValueError):
        truncate_number(-3.5)

def test_truncate_number_non_numeric():
    with pytest.raises(TypeError):
        truncate_number("3.5")

def test_truncate_number_large_number():
    assert truncate_number(12345.6789) == 0.6789

def test_truncate_number_small_number():
    assert truncate_number(0.000123) == 0.000123

def test_truncate_number_repeating_decimal():
    assert truncate_number(0.333333) == 0.333333