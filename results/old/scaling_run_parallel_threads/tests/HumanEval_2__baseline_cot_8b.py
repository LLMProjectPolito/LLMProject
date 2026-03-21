import pytest

def test_truncate_number_integer_part():
    assert truncate_number(3.5) == 0.5

def test_truncate_number_zero():
    assert truncate_number(0.0) == 0.0

def test_truncate_number_decimal_part():
    assert truncate_number(0.5) == 0.5

def test_truncate_number_large_number():
    assert truncate_number(12345.6789) == 0.6789

def test_truncate_number_negative_number():
    with pytest.raises(ValueError):
        truncate_number(-3.5)

def test_truncate_number_non_numeric_input():
    with pytest.raises(TypeError):
        truncate_number("3.5")

def test_truncate_number_empty_input():
    with pytest.raises(TypeError):
        truncate_number()

def test_truncate_number_float_input():
    assert truncate_number(3.5) == 0.5

def test_truncate_number_repeated_decimal():
    assert truncate_number(3.55555) == 0.55555

def test_truncate_number_large_decimal():
    assert truncate_number(3.99999) == 0.99999