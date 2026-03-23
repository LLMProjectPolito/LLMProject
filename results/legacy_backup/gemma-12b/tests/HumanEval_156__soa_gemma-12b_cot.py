import pytest

def test_int_to_mini_roman_positive_numbers():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(2) == "ii"
    assert int_to_mini_roman(3) == "iii"
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(5) == "v"
    assert int_to_mini_roman(6) == "vi"
    assert int_to_mini_roman(7) == "vii"
    assert int_to_mini_roman(8) == "viii"
    assert int_to_mini_roman(9) == "ix"
    assert int_to_mini_roman(10) == "x"
    assert int_to_mini_roman(11) == "xi"
    assert int_to_mini_roman(19) == "xix"
    assert int_to_mini_roman(20) == "xx"
    assert int_to_mini_roman(30) == "xxx"
    assert int_to_mini_roman(39) == "xxxix"
    assert int_to_mini_roman(40) == "xl"
    assert int_to_mini_roman(41) == "xli"
    assert int_to_mini_roman(49) == "xlix"
    assert int_to_mini_roman(50) == "l"
    assert int_to_mini_roman(51) == "li"
    assert int_to_mini_roman(59) == "lix"
    assert int_to_mini_roman(60) == "lx"
    assert int_to_mini_roman(61) == "lxi"
    assert int_to_mini_roman(69) == "lxix"
    assert int_to_mini_roman(70) == "lxx"
    assert int_to_mini_roman(71) == "lxxi"
    assert int_to_mini_roman(79) == "lxxix"
    assert int_to_mini_roman(80) == "lxxx"
    assert int_to_mini_roman(81) == "lxxxi"
    assert int_to_mini_roman(89) == "lxxxix"
    assert int_to_mini_roman(90) == "xc"
    assert int_to_mini_roman(91) == "xci"
    assert int_to_mini_roman(99) == "xciix"
    assert int_to_mini_roman(100) == "c"
    assert int_to_mini_roman(101) == "ci"
    assert int_to_mini_roman(149) == "cxlix"
    assert int_to_mini_roman(150) == "cl"
    assert int_to_mini_roman(152) == "clii"
    assert int_to_mini_roman(199) == "cxcix"
    assert int_to_mini_roman(200) == "cc"
    assert int_to_mini_roman(399) == "cccxcix"
    assert int_to_mini_roman(400) == "cd"
    assert int_to_mini_roman(426) == "cdxxvi"
    assert int_to_mini_roman(444) == "cdxliv"
    assert int_to_mini_roman(499) == "cdxcix"
    assert int_to_mini_roman(500) == "d"
    assert int_to_mini_roman(501) == "di"
    assert int_to_mini_roman(555) == "dlv"
    assert int_to_mini_roman(600) == "dc"
    assert int_to_mini_roman(649) == "dcxlix"
    assert int_to_mini_roman(699) == "dxcix"
    assert int_to_mini_roman(700) == "dd"
    assert int_to_mini_roman(749) == "ddxlix"
    assert int_to_mini_roman(799) == "ddxciii"
    assert int_to_mini_roman(800) == "dcc"
    assert int_to_mini_roman(849) == "dccxlix"
    assert int_to_mini_roman(899) == "dccxcix"
    assert int_to_mini_roman(900) == "cm"
    assert int_to_mini_roman(949) == "cmxlix"
    assert int_to_mini_roman(999) == "cmxcix"
    assert int_to_mini_roman(1000) == "m"

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(1000) == "m"

def test_int_to_mini_roman_invalid_input():
    with pytest.raises(TypeError):
        int_to_mini_roman("abc")
    with pytest.raises(TypeError):
        int_to_mini_roman(1.5)
    with pytest.raises(ValueError):
        int_to_mini_roman(0)
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)