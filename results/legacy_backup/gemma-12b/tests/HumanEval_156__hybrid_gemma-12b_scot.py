import pytest
from your_module import int_to_mini_roman  # Replace your_module

def test_valid_input_range():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(20) == 'xx'
    assert int_to_mini_roman(30) == 'xxx'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(60) == 'lx'
    assert int_to_mini_roman(70) == 'lxx'
    assert int_to_mini_roman(80) == 'lxxx'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(999) == 'cmxciii'
    assert int_to_mini_roman(1000) == 'm'

def test_invalid_input_less_than_1():
    with pytest.raises(ValueError):
        int_to_mini_roman(0)

def test_invalid_input_greater_than_1000():
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)

def test_single_digit_numbers():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(2) == 'ii'
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(4) == 'iiii'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(6) == 'vi'
    assert int_to_mini_roman(7) == 'vii'
    assert int_to_mini_roman(8) == 'viii'
    assert int_to_mini_roman(9) == 'ix'

def test_teen_numbers():
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

def test_numbers_in_20s_30s_40s():
    assert int_to_mini_roman(25) == 'xxv'
    assert int_to_mini_roman(31) == 'xxxii'
    assert int_to_mini_roman(48) == 'xlviii'

def test_numbers_in_50s_60s_70s():
    assert int_to_mini_roman(52) == 'lvii'
    assert int_to_mini_roman(67) == 'lxvii'
    assert int_to_mini_roman(79) == 'lxxix'

def test_numbers_in_80s_90s():
    assert int_to_mini_roman(84) == 'lxxxiv'
    assert int_to_mini_roman(91) == 'xci'
    assert int_to_mini_roman(99) == 'xciii'

def test_numbers_with_hundreds():
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(150) == 'cl'
    assert int_to_mini_roman(200) == 'cc'
    assert int_to_mini_roman(250) == 'ccl'
    assert int_to_mini_roman(300) == 'ccc'
    assert int_to_mini_roman(350) == 'ccccl'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(450) == 'cdl'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(550) == 'dl'
    assert int_to_mini_roman(600) == 'dc'
    assert int_to_mini_roman(650) == 'dcl'
    assert int_to_mini_roman(700) == 'dcc'
    assert int_to_mini_roman(750) == 'dcccl'
    assert int_to_mini_roman(800) == 'dccc'
    assert int_to_mini_roman(850) == 'dccccl'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(950) == 'cmx'
    assert int_to_mini_roman(1000) == 'm'

def test_complex_numbers():
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(789) == 'dccclxxxix'
    assert int_to_mini_roman(911) == 'cmi'
    assert int_to_mini_roman(999) == 'cmxciii'

def test_lowercase_output():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(1000) == 'm'