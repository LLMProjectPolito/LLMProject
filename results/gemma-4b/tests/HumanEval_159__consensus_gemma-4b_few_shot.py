def test_eat_basic():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]
    assert eat(2, 11, 5) == [7, 0]

def test_eat_no_remaining():
    assert eat(0, 5, 0) == [5, 0]
    assert eat(1, 1, 0) == [1, 0]

def test_eat_enough_remaining():
    assert eat(2, 3, 5) == [5, 2]
    assert eat(1, 2, 3) == [3, 1]

def test_eat_not_enough_remaining():
    assert eat(3, 2, 5) == [5, 0]
    assert eat(1, 1, 1) == [1, 0]

def test_eat_zero_need():
    assert eat(5, 0, 10) == [5, 5]
    assert eat(0, 0, 10) == [0, 10]