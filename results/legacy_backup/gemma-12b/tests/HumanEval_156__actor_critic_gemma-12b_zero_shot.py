import pytest
from your_module import int_to_mini_roman  # Replace your_module

def test_positive_integers():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(2) == "ii"
    assert int_to_mini_roman(3) == "iii"
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(5) == "v"
    assert int_to_mini_roman(10) == "x"
    assert int_to_mini_roman(20) == "xx"
    assert int_to_mini_roman(39) == "xxxix"
    assert int_to_mini_roman(40) == "xl"
    assert int_to_mini_roman(50) == "l"
    assert int_to_mini_roman(90) == "xc"
    assert int_to_mini_roman(100) == "c"
    assert int_to_mini_roman(200) == "cc"
    assert int_to_mini_roman(399) == "cccxciix"
    assert int_to_mini_roman(400) == "cd"
    assert int_to_mini_roman(500) == "d"
    assert int_to_mini_roman(900) == "cm"
    assert int_to_mini_roman(1000) == "m"

def test_edge_cases():
    assert int_to_mini_roman(3999) == "m" # Boundary test
    assert int_to_mini_roman(1000) == "m" # Upper bound test

def test_zero_input():
    assert int_to_mini_roman(0) == ""

def test_invalid_input_positive():
    with pytest.raises(ValueError) as excinfo:
        int_to_mini_roman(-1)
    assert "Input must be a positive integer." in str(excinfo.value)

def test_invalid_input_range():
    @pytest.mark.parametrize("input_value", [1001, 2000, -1, -100])
    def test_range(input_value):
        with pytest.raises(ValueError) as excinfo:
            int_to_mini_roman(input_value)
        assert "Input must be between 1 and 1000." in str(excinfo.value)