import pytest

@pytest.mark.parametrize("number, expected", [
    (3.5, 0.5),
    (10.2, 0.2),
    (0.7, 0.7),
    (1.0, 0.0),
    (0.0, 0.0),
    (1.2, 0.2),
    (0.8, 0.8),
    (10.9, 0.9),
    (0.1, 0.1)
])
def test_truncate_number(number, expected):
    assert truncate_number(number) == expected

def test_truncate_number_with_negative_number():
    with pytest.raises(ValueError):
        truncate_number(-3.5)

def test_truncate_number_with_non_float_input():
    with pytest.raises(TypeError):
        truncate_number("3.5")

def test_truncate_number_with_non_numeric_input():
    with pytest.raises(TypeError):
        truncate_number([3.5])

def test_truncate_number_edge_case_zero():
    assert truncate_number(0.0) == 0.0

def test_truncate_number_int_input():
    with pytest.raises(TypeError):
        truncate_number(3)