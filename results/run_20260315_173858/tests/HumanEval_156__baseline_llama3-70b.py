import pytest

def test_int_to_mini_roman_single_digit():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_additive_notation():
    assert int_to_mini_roman(2) == 'ii'
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(11) == 'xi'
    assert int_to_mini_roman(12) == 'xii'
    assert int_to_mini_roman(101) == 'ci'
    assert int_to_mini_roman(102) == 'cii'

def test_int_to_mini_roman_subtractive_notation():
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(900) == 'cm'

def test_int_to_mini_roman_complex_numbers():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(777) == 'dcclxxvii'
    assert int_to_mini_roman(999) == 'cmxcix'

def test_int_to_mini_roman_edge_cases():
    with pytest.raises(ValueError):
        int_to_mini_roman(0)
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)
    with pytest.raises(TypeError):
        int_to_mini_roman('a')