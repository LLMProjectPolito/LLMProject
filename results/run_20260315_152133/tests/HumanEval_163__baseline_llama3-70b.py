import pytest

def test_generate_integers_even_range():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_reversed_range():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even_digits():
    assert generate_integers(10, 14) == []

def test_generate_integers_single_even_digit():
    assert generate_integers(4, 4) == [4]

def test_generate_integers_no_even_digits_in_range():
    assert generate_integers(1, 3) == []

def test_generate_integers_negative_numbers():
    with pytest.raises(ValueError):
        generate_integers(-2, 8)

def test_generate_integers_non_integer_input():
    with pytest.raises(TypeError):
        generate_integers(2.5, 8)

def test_generate_integers_non_numeric_input():
    with pytest.raises(TypeError):
        generate_integers('a', 8)

def test_generate_integers_equal_numbers():
    assert generate_integers(2, 2) == [2]

def test_generate_integers_large_range():
    assert generate_integers(2, 100) == [i for i in range(2, 101) if i % 2 == 0]