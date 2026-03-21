def test_base_cases():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(1000) == 'm'

def test_boundary_cases():
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(99) == 'xix'
    assert int_to_mini_roman(999) == 'cix'

def test_edge_cases():
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(6) == 'vi'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(42) == 'xxii'
    assert int_to_mini_roman(58) == 'lii'
    assert int_to_mini_roman(99) == 'xix'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(199) == 'xcii'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(1000) == 'm'

def test_invalid_input():
    with pytest.raises(Exception):
        int_to_mini_roman(0)
    with pytest.raises(Exception):
        int_to_mini_roman(1001)