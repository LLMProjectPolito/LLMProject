import pytest
from your_module import int_to_mini_roman  # Replace your_module

def test_basic_cases():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(2) == "ii"
    assert int_to_mini_roman(3) == "iii"
    assert int_to_mini_roman(5) == "v"
    assert int_to_mini_roman(10) == "x"

def test_teen_cases():
    assert int_to_mini_roman(11) == "xi"
    assert int_to_mini_roman(12) == "xii"
    assert int_to_mini_roman(15) == "xv"
    assert int_to_mini_roman(19) == "xix"

def test_numbers_20_to_99():
    assert int_to_mini_roman(20) == "xx"
    assert int_to_mini_roman(35) == "xxxv"
    assert int_to_mini_roman(42) == "xlii"
    assert int_to_mini_roman(58) == "lviii"
    assert int_to_mini_roman(63) == "lxiii"
    assert int_to_mini_roman(77) == "lxxvii"
    assert int_to_mini_roman(84) == "lxxxiv"
    assert int_to_mini_roman(99) == "xciii"

def test_hundreds_cases():
    assert int_to_mini_roman(100) == "c"
    assert int_to_mini_roman(101) == "ci"
    assert int_to_mini_roman(145) == "clxv"
    assert int_to_mini_roman(200) == "cc"
    assert int_to_mini_roman(250) == "ccl"
    assert int_to_mini_roman(300) == "ccc"
    assert int_to_mini_roman(356) == "cccclvi"
    assert int_to_mini_roman(400) == "cd"
    assert int_to_mini_roman(444) == "cdxliv"
    assert int_to_mini_roman(150) == "cl"
    assert int_to_mini_roman(175) == "clxxv"
    assert int_to_mini_roman(199) == "cxcix"
    assert int_to_mini_roman(222) == "ccxxii"
    assert int_to_mini_roman(249) == "ccxlix"

def test_five_hundreds_cases():
    assert int_to_mini_roman(500) == "d"
    assert int_to_mini_roman(501) == "di"
    assert int_to_mini_roman(543) == "dlxiii"
    assert int_to_mini_roman(600) == "dc"
    assert int_to_mini_roman(650) == "dcl"
    assert int_to_mini_roman(700) == "dcc"
    assert int_to_mini_roman(756) == "dccclvi"
    assert int_to_mini_roman(800) == "dcc"
    assert int_to_mini_roman(899) == "dcccxcix"
    assert int_to_mini_roman(900) == "cm"
    assert int_to_mini_roman(949) == "cmxlix"
    assert int_to_mini_roman(999) == "cmxcix"

def test_edge_cases():
    assert int_to_mini_roman(1000) == "m"

def test_numbers_around_hundreds():
    assert int_to_mini_roman(399) == "cccxcix"
    assert int_to_mini_roman(499) == "cdxcix"
    assert int_to_mini_roman(898) == "dcccxcviii"
    assert int_to_mini_roman(948) == "cmxlviii"

def test_input_validation():
    with pytest.raises(TypeError):
        int_to_mini_roman(1.5)
    with pytest.raises(TypeError):
        int_to_mini_roman("1")
    with pytest.raises(ValueError):
        int_to_mini_roman(0)
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)