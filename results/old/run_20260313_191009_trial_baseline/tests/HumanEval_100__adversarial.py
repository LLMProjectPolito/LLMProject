import pytest

def test_make_a_pile_odd():
    assert make_a_pile(3) == [3, 5, 7]
    assert make_a_pile(1) == [1]
    assert make_a_pile(5) == [5, 7, 9, 11, 13]

def test_make_a_pile_even():
    assert make_a_pile(4) == [4, 6, 8, 10]
    assert make_a_pile(2) == [2, 4]
    assert make_a_pile(6) == [6, 8, 10, 12, 14, 16]

def test_make_a_pile_edge_cases():
    with pytest.raises(ValueError):
        make_a_pile(0)
    with pytest.raises(ValueError):
        make_a_pile(-1)
    with pytest.raises(TypeError):
        make_a_pile("a")

def test_make_a_pile_length():
    for i in range(1, 10):
        assert len(make_a_pile(i)) == i

def test_make_a_pile_type():
    for i in range(1, 10):
        assert isinstance(make_a_pile(i), list)
        for j in make_a_pile(i):
            assert isinstance(j, int)