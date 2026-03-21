import pytest

@pytest.mark.parametrize("n, expected_output", [
    (3, [3, 5, 7]),
    (5, [5, 7, 9, 11, 13]),
    (2, [2, 4]),
    (10, [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]),
    (1, [1, 3]),
])
def test_make_a_pile(n, expected_output):
    assert make_a_pile(n) == expected_output

def test_make_a_pile_invalid_input():
    with pytest.raises(TypeError):
        make_a_pile("a")

def test_make_a_pile_negative_input():
    with pytest.raises(ValueError):
        make_a_pile(-1)

def test_make_a_pile_zero_input():
    with pytest.raises(ValueError):
        make_a_pile(0)

def test_make_a_pile_non_integer_input():
    with pytest.raises(TypeError):
        make_a_pile(1.5)