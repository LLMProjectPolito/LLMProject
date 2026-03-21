def test_make_a_pile_odd_start():
    assert make_a_pile(3) == [3, 5, 7]

def test_make_a_pile_even_start():
    assert make_a_pile(4) == [4, 6, 8]

def test_make_a_pile_single_level():
    assert make_a_pile(1) == [1]

def test_make_a_pile_no_levels():
    assert make_a_pile(0) == []

def test_make_a_pile_negative_input():
    with pytest.raises(ValueError):
        make_a_pile(-1)

def test_make_a_pile_non_integer_input():
    with pytest.raises(TypeError):
        make_a_pile(3.5)

def test_make_a_pile_large_input():
    assert len(make_a_pile(100)) == 100

def test_make_a_pile_edge_case():
    assert make_a_pile(2) == [2, 4]

def test_make_a_pile_consecutive_odd_even():
    assert make_a_pile(1) == [1, 2, 3]
    assert make_a_pile(2) == [2, 4, 6]
    assert make_a_pile(3) == [3, 5, 7]
    assert make_a_pile(4) == [4, 6, 8]
    assert make_a_pile(5) == [5, 7, 9]