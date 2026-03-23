import pytest

def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_even():
    assert generate_integers(2, 3) == [2]

def test_generate_integers_same_number():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_start_with_odd():
    assert generate_integers(1, 6) == [2, 4, 6]

def test_generate_integers_end_with_odd():
    assert generate_integers(3, 7) == [4, 6]

def test_generate_integers_large_range():
    assert generate_integers(1, 20) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def test_generate_integers_negative_input():
    with pytest.raises(TypeError):
        generate_integers(-2, 8)

def test_generate_integers_float_input():
    with pytest.raises(TypeError):
        generate_integers(2.5, 8)

def test_generate_integers_string_input():
    with pytest.raises(TypeError):
        generate_integers("2", "8")

def test_generate_integers_zero_input():
    with pytest.raises(ValueError):
        generate_integers(0, 8)

def test_generate_integers_zero_and_positive():
    with pytest.raises(ValueError):
        generate_integers(0, 5)

def test_generate_integers_positive_and_zero():
    with pytest.raises(ValueError):
        generate_integers(5, 0)