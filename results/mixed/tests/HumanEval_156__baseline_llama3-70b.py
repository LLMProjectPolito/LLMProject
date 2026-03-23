import pytest

def test_int_to_mini_roman_single_digit():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(2) == 'ii'
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(6) == 'vi'
    assert int_to_mini_roman(7) == 'vii'
    assert int_to_mini_roman(8) == 'viii'
    assert int_to_mini_roman(9) == 'ix'

def test_int_to_mini_roman_tens():
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(11) == 'xi'
    assert int_to_mini_roman(12) == 'xii'
    assert int_to_mini_roman(13) == 'xiii'
    assert int_to_mini_roman(14) == 'xiv'
    assert int_to_mini_roman(15) == 'xv'
    assert int_to_mini_roman(16) == 'xvi'
    assert int_to_mini_roman(17) == 'xvii'
    assert int_to_mini_roman(18) == 'xviii'
    assert int_to_mini_roman(19) == 'xix'

def test_int_to_mini_roman_hundreds():
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(101) == 'ci'
    assert int_to_mini_roman(102) == 'cii'
    assert int_to_mini_roman(103) == 'ciii'
    assert int_to_mini_roman(104) == 'civ'
    assert int_to_mini_roman(105) == 'cv'
    assert int_to_mini_roman(106) == 'cvi'
    assert int_to_mini_roman(107) == 'cvii'
    assert int_to_mini_roman(108) == 'cviii'
    assert int_to_mini_roman(109) == 'cix'

def test_int_to_mini_roman_large_numbers():
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_invalid_input():
    with pytest.raises(ValueError):
        int_to_mini_roman(0)
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)
    with pytest.raises(TypeError):
        int_to_mini_roman('a')