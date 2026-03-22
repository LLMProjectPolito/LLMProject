import pytest

def test_int_to_mini_roman_valid_range():
    """Test cases within the valid range (1-1000)."""
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
    assert int_to_mini_roman(39) == "xxxix"
    assert int_to_mini_roman(40) == "xl"
    assert int_to_mini_roman(41) == "xli"
    assert int_to_mini_roman(49) == "xlix"
    assert int_to_mini_roman(50) == "l"
    assert int_to_mini_roman(51) == "li"
    assert int_to_mini_roman(90) == "xc"
    assert int_to_mini_roman(91) == "xci"
    assert int_to_mini_roman(100) == "c"
    assert int_to_mini_roman(101) == "ci"
    assert int_to_mini_roman(149) == "cxlix"
    assert int_to_mini_roman(150) == "cl"
    assert int_to_mini_roman(152) == "clii"
    assert int_to_mini_roman(199) == "xciix"
    assert int_to_mini_roman(200) == "cc"
    assert int_to_mini_roman(399) == "cccxciix"
    assert int_to_mini_roman(400) == "cd"
    assert int_to_mini_roman(426) == "cdxxvi"
    assert int_to_mini_roman(444) == "cdxliv"
    assert int_to_mini_roman(499) == "cdxciix"
    assert int_to_mini_roman(500) == "d"
    assert int_to_mini_roman(501) == "di"
    assert int_to_mini_roman(900) == "cm"
    assert int_to_mini_roman(901) == "cmi"
    assert int_to_mini_roman(999) == "cmxciix"
    assert int_to_mini_roman(1000) == "m"

def test_int_to_mini_roman_edge_cases():
    """Test edge cases: 1 and 1000."""
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(1000) == "m"

def test_int_to_mini_roman_invalid_input_lower_bound():
    """Test input less than 1."""
    with pytest.raises(ValueError):
        int_to_mini_roman(0)
    with pytest.raises(ValueError):
        int_to_mini_roman(-1)

def test_int_to_mini_roman_invalid_input_upper_bound():
    """Test input greater than 1000."""
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)
    with pytest.raises(ValueError):
        int_to_mini_roman(2000)