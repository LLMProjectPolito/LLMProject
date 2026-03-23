import pytest

def test_basic_case1():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_basic_case2():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_no_even_digits():
    assert generate_integers(10, 14) == []

def test_single_digit_range():
    assert generate_integers(1, 1) == []
    assert generate_integers(2, 2) == [2]
    assert generate_integers(3, 3) == []

def test_large_numbers():
    assert generate_integers(1000, 1010) == [1000, 1002, 1004, 1006, 1008, 1010]
    assert generate_integers(100, 110) == [100, 102, 104, 106, 108, 110]

def test_equal_inputs():
    assert generate_integers(5, 5) == []
    assert generate_integers(6, 6) == [6]

def test_boundary_conditions():
    assert generate_integers(1, 2) == [2]
    assert generate_integers(2, 3) == [2]
    assert generate_integers(7, 8) == [8]
    assert generate_integers(8, 9) == [8]

def test_zero_input():
    assert generate_integers(0, 2) == [0, 2]
    assert generate_integers(2, 0) == [0, 2]
    assert generate_integers(0, 0) == [0]

def test_negative_input():
    assert generate_integers(-2, 2) == [-2, 0, 2]
    assert generate_integers(-4, -1) == [-4, -2]
    assert generate_integers(-1, -2) == [-2, -4]

def test_single_number_range_even():
    assert generate_integers(6, 6) == [6]

def test_single_number_range_odd():
    assert generate_integers(5, 5) == []

def test_both_even():
    assert generate_integers(4, 10) == [4, 6, 8, 10]

def test_both_odd():
    assert generate_integers(1, 7) == [2, 4, 6]

def test_a_even_b_odd():
    assert generate_integers(2, 7) == [2, 4, 6]

def test_a_odd_b_even():
    assert generate_integers(1, 8) == [2, 4, 6, 8]

def test_boundary_condition_small():
    assert generate_integers(1, 2) == [2]

def test_empty_list_case():
    assert generate_integers(11, 13) == []

def test_large_range_no_evens():
    assert generate_integers(11, 15) == []

def test_large_range_with_evens():
    assert generate_integers(98, 104) == [98, 100, 102, 104]

def test_negative_input_a():
    with pytest.raises(TypeError):
        generate_integers(-2, 4)

def test_negative_input_b():
    with pytest.raises(TypeError):
        generate_integers(2, -4)

def test_zero_input_a():
    with pytest.raises(TypeError):
        generate_integers(0, 4)

def test_zero_input_b():
    with pytest.raises(TypeError):
        generate_integers(2, 0)