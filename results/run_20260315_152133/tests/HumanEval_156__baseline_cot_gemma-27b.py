import pytest

def test_basic_cases():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'

def test_boundary_cases():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(1000) == 'm'

def test_edge_cases_subtractive_notation():
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(900) == 'cm'

def test_repeating_symbols():
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(8) == 'viii'
    assert int_to_mini_roman(30) == 'xxx'
    assert int_to_mini_roman(80) == 'lxxx'
    assert int_to_mini_roman(300) == 'ccc'
    assert int_to_mini_roman(800) == 'dccc'

def test_combination_cases():
    assert int_to_mini_roman(16) == 'xvi'
    assert int_to_mini_roman(23) == 'xxiii'
    assert int_to_mini_roman(58) == 'lviii'
    assert int_to_mini_roman(149) == 'cxlix'
    assert int_to_mini_roman(399) == 'cccxcix'
    assert int_to_mini_roman(789) == ' DCCLXXXIX'

def test_invalid_input():
    assert int_to_mini_roman(0) == ''
    assert int_to_mini_roman(-1) == ''
    assert int_to_mini_roman(1001) == 'm'