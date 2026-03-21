import pytest
from your_module import generate_integers  # Replace your_module

def test_basic_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_basic_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_no_even_numbers():
    assert generate_integers(10, 14) == []

def test_same_even_number():
    assert generate_integers(4, 4) == [4]

def test_odd_to_even():
    assert generate_integers(1, 6) == [2, 4, 6]

def test_even_to_odd():
    assert generate_integers(6, 1) == [2, 4, 6]

def test_zero_to_even():
    assert generate_integers(0, 6) == [2, 4, 6]

def test_even_to_zero():
    assert generate_integers(6, 0) == [2, 4, 6]

def test_same_odd_number():
    assert generate_integers(3, 3) == []

def test_consecutive_even_numbers():
    assert generate_integers(2, 4) == [2, 4]

def test_consecutive_odd_numbers():
    assert generate_integers(1, 3) == []

def test_invalid_input_type():
    with pytest.raises(TypeError):
        generate_integers(2.5, 5)  # Test with a float
    with pytest.raises(TypeError):
        generate_integers(2, "5")  # Test with a string