import pytest

def test_greatest_common_divisor_equal_numbers():
    assert greatest_common_divisor(5, 5) == 5

def test_greatest_common_divisor_coprime_numbers():
    assert greatest_common_divisor(3, 5) == 1

def test_greatest_common_divisor_divisible_numbers():
    assert greatest_common_divisor(25, 15) == 5

def test_greatest_common_divisor_negative_numbers():
    assert greatest_common_divisor(-3, 5) == 1

def test_greatest_common_divisor_zero():
    with pytest.raises(ZeroDivisionError):
        greatest_common_divisor(0, 5)

def test_greatest_common_divisor_negative_and_zero():
    with pytest.raises(ZeroDivisionError):
        greatest_common_divisor(-3, 0)

def test_greatest_common_divisor_non_integer_input():
    with pytest.raises(TypeError):
        greatest_common_divisor(3.5, 5)

def test_greatest_common_divisor_non_integer_and_zero():
    with pytest.raises(TypeError):
        greatest_common_divisor(3.5, 0)

def test_greatest_common_divisor_large_numbers():
    assert greatest_common_divisor(12345, 6789) == 3

def test_greatest_common_divisor_negative_and_large_numbers():
    assert greatest_common_divisor(-12345, 6789) == 3