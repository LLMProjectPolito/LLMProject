import pytest

def test_make_a_pile_odd():
    assert make_a_pile(3) == [3, 5, 7]

def test_make_a_pile_even():
    assert make_a_pile(4) == [4, 6, 8]

def test_make_a_pile_single_level():
    assert make_a_pile(1) == [1]

def test_make_a_pile_large_input():
    assert make_a_pile(10) == [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

def test_make_a_pile_zero():
    with pytest.raises(ValueError):
        make_a_pile(0)

def test_make_a_pile_negative():
    with pytest.raises(ValueError):
        make_a_pile(-1)

def test_make_a_pile_non_integer():
    with pytest.raises(TypeError):
        make_a_pile(3.5)

def test_make_a_pile_non_numeric():
    with pytest.raises(TypeError):
        make_a_pile("three")