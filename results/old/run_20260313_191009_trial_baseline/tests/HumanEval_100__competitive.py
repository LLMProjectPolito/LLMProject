def test_make_a_pile_example():
    assert make_a_pile(3) == [3, 5, 7]

def test_make_a_pile_single_level():
    assert make_a_pile(1) == [1]

def test_make_a_pile_two_levels_even_start():
    assert make_a_pile(2) == [2, 4]

def test_make_a_pile_five_levels_odd_start():
    assert make_a_pile(5) == [5, 7, 9, 11, 13]

def test_make_a_pile_four_levels_even_start():
    assert make_a_pile(4) == [4, 6, 8, 10]

def test_make_a_pile_six_levels_even_start():
    assert make_a_pile(6) == [6, 8, 10, 12, 14, 16]

def test_make_a_pile_seven_levels_odd_start():
    assert make_a_pile(7) == [7, 9, 11, 13, 15, 17, 19]

def test_make_a_pile_zero_levels():
    assert make_a_pile(0) == []