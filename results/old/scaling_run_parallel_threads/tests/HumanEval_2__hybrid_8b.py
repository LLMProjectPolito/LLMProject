import pytest

@pytest.mark.parametrize("number, expected", [
    (3.5, 0.5),
    (10.0, 0.0),
    (0.75, 0.75),
    (123.456, 0.456),
    (987.0, 0.0),
    (3.5, 0.5),
    (10.8, 0.8),
    (7.2, 0.2),
    (1.9, 0.9),
    (0.4, 0.4),
])
def test_truncate_number(number, expected):
    assert truncate_number(number) == expected

def test_truncate_number_zero():
    assert truncate_number(0.0) == 0.0

def test_truncate_number_negative():
    with pytest.raises(ValueError):
        truncate_number(-3.5)

def test_truncate_number_negative_2():
    with pytest.raises(ValueError):
        truncate_number(-1.5)

def test_truncate_number_non_numeric():
    with pytest.raises(TypeError):
        truncate_number("3.5")

def test_truncate_number_non_numeric_2():
    with pytest.raises(TypeError):
        truncate_number("a")