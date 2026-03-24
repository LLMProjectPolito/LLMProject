import pytest
from your_module import generate_integers  # Replace your_module

def test_ascending_even_numbers():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(6, 8) == [6, 8]

def test_descending_even_numbers():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_empty_range():
    assert generate_integers(1, 3) == []
    assert generate_integers(10, 14) == []

def test_single_even_number():
    assert generate_integers(2, 3) == [2]
    assert generate_integers(4, 5) == [4]

def test_multiple_even_numbers():
    assert generate_integers(4, 10) == [4, 6, 8, 10]

def test_inclusive_range():
    assert generate_integers(2, 4) == [2, 4]
    assert generate_integers(6, 8) == [6, 8]

def test_negative_numbers():
    assert generate_integers(-2, 8) == []
    assert generate_integers(2, -8) == []
    assert generate_integers(-2, -8) == []

def test_zero_input():
    assert generate_integers(0, 8) == [0, 2, 4, 6, 8]
    assert generate_integers(2, 0) == []
    assert generate_integers(0, 0) == [0]

def test_mixed_even_odd():
    assert generate_integers(3, 9) == [4, 6, 8]

def test_no_even_numbers():
    assert generate_integers(1, 3) == []

def test_same_number_even():
    assert generate_integers(4, 4) == [4]

def test_same_number_odd():
    assert generate_integers(3, 3) == []

def test_edge_case_zero():
    assert generate_integers(0, 4) == [0, 2, 4]

def test_large_numbers():
    assert generate_integers(100, 110) == [100, 102, 104, 106, 108, 110]

def test_negative_input_error():
    with pytest.raises(TypeError):
        generate_integers(-2, 4)
    with pytest.raises(TypeError):
        generate_integers(2, -4)