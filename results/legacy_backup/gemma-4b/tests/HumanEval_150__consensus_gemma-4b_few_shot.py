def test_x_or_y_prime():
    assert x_or_y(7, 34, 12) == 34

def test_x_or_y_not_prime():
    assert x_or_y(15, 8, 5) == 5

def test_x_or_y_zero():
    assert x_or_y(0, 34, 12) == 12

def test_x_or_y_one():
    assert x_or_y(1, 34, 12) == 12

def test_x_or_y_negative():
    assert x_or_y(-7, 34, 12) == 34