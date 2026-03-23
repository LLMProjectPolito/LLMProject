def test_eat_basic():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_need_more_than_remaining():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_exactly_enough():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_remaining_less_than_need():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_zero_initial_eaten():
    assert eat(0, 5, 10) == [5, 5]

def test_eat_zero_need():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_zero_remaining():
    assert eat(5, 6, 0) == [5, 0]

def test_eat_all_zeros():
    assert eat(0, 0, 0) == [0, 0]

def test_eat_large_numbers():
    assert eat(999, 999, 1000) == [1998, 1]

def test_eat_large_numbers2():
    assert eat(100, 1000, 500) == [600, 0]

def test_eat_edge_case_need_equals_remaining():
    assert eat(2, 5, 5) == [7, 0]

def test_eat_edge_case_need_equals_remaining_plus_eaten():
    assert eat(3, 5, 4) == [8, 1]