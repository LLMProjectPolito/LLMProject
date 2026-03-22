import pytest

def test_rounded_avg_valid_range():
    assert rounded_avg(1, 5) == "0b11"
    assert rounded_avg(10, 20) == "0b1111"
    assert rounded_avg(20, 33) == "0b11010"

def test_rounded_avg_invalid_range():
    assert rounded_avg(7, 5) == -1
    assert rounded_avg(20, 10) == -1

def test_rounded_avg_equal_numbers():
    assert rounded_avg(10, 10) == "0b1010"

def test_rounded_avg_consecutive_numbers():
    assert rounded_avg(1, 2) == "0b10"

def test_rounded_avg_large_numbers():
    assert rounded_avg(1000, 2000) == "0b10000000000"

def test_rounded_avg_small_numbers():
    assert rounded_avg(1, 1) == "0b1"

def test_rounded_avg_negative_input():
    with pytest.raises(TypeError):
        rounded_avg(-1, 5)
    with pytest.raises(TypeError):
        rounded_avg(5, -1)
    with pytest.raises(TypeError):
        rounded_avg(-1, -5)

def test_rounded_avg_non_integer_input():
    with pytest.raises(TypeError):
        rounded_avg(1.5, 5)
    with pytest.raises(TypeError):
        rounded_avg(5, 1.5)
    with pytest.raises(TypeError):
        rounded_avg(1.5, 5.5)

def test_rounded_avg_non_numeric_input():
    with pytest.raises(TypeError):
        rounded_avg("a", 5)
    with pytest.raises(TypeError):
        rounded_avg(5, "a")
    with pytest.raises(TypeError):
        rounded_avg("a", "b")