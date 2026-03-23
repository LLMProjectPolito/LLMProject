def test_eat_basic():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]
    assert eat(2, 11, 5) == [7, 0]

def test_eat_no_remaining():
    assert eat(0, 5, 0) == [5, 0]

def test_eat_enough_remaining():
    assert eat(2, 3, 5) == [5, 2]

def test_eat_exact_match():
    assert eat(3, 3, 6) == [6, 3]

def test_eat_zero_need():
    assert eat(1, 0, 5) == [1, 5]

def test_eat_zero_number():
    assert eat(0, 5, 5) == [5, 0]