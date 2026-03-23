def test_eat_positive():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_empty():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_one():
    assert eat(1, 10, 10) == [11, 0]