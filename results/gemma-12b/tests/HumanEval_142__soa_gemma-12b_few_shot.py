def test_sum_squares_basic():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_negative():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_mixed():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1 + 2 + 3**2 + 4**3 + 5 + 6**2 + 7 + 8**3 + 9 + 10**2

def test_sum_squares_multiple_of_both():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 12]) == 1 + 2 + 3**2 + 4**3 + 5 + 6**2 + 7 + 8**3 + 9 + 12**2

def test_sum_squares_zero():
    assert sum_squares([0, 0, 0, 0, 0]) == 0

def test_sum_squares_large_numbers():
    assert sum_squares([100, 200, 300, 400]) == 100 + 200**2 + 300**3 + 400

def test_sum_squares_single_element():
    assert sum_squares([5]) == 5

def test_sum_squares_longer_list():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 1 + 2 + 3**2 + 4**3 + 5 + 6**2 + 7 + 8**3 + 9 + 10**2 + 11 + 12**2 + 13 + 14**3 + 15 + 16**2