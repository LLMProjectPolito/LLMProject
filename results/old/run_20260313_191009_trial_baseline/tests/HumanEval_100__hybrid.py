import pytest

@pytest.mark.parametrize("input_value, expected_output", [
    (3, [3, 5, 7]),
    (4, [4, 6, 8]),
    (1, [1]),
    (2, [2, 4]),
    (5, [5, 7, 9, 11, 13]),
    (6, [6, 8, 10, 12, 14, 16]),
    (10, [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]),
])
def test_make_a_pile(input_value, expected_output):
    assert make_a_pile(input_value) == expected_output

def test_make_a_pile_negative_input():
    with pytest.raises(ValueError):
        make_a_pile(-1)

def test_make_a_pile_zero_input():
    with pytest.raises(ValueError):
        make_a_pile(0)

def test_make_a_pile_non_integer_input():
    with pytest.raises(TypeError):
        make_a_pile(3.5)

def test_make_a_pile_non_numeric_input():
    with pytest.raises(TypeError):
        make_a_pile("3")