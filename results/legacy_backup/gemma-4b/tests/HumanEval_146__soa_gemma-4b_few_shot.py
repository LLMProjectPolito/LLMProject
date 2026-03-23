def test_specialFilter_positive():
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_negative():
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_specialFilter_empty():
    assert specialFilter([]) == 0

def test_specialFilter_no_match():
    assert specialFilter([1, 2, 3, 4, 5]) == 0

def test_specialFilter_mixed():
    assert specialFilter([11, 13, 15, 17, 19, 2, 4, 6, 8, 10]) == 3

def test_specialFilter_single_match():
    assert specialFilter([11]) == 0

def test_specialFilter_single_odd_digit():
    assert specialFilter([111]) == 0

def test_specialFilter_single_odd_digit_and_greater_than_10():
    assert specialFilter([11111]) == 0