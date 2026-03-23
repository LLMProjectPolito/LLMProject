def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_basic():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_multiple_of_3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 90

def test_sum_squares_multiple_of_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 385

def test_sum_squares_mixed():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_complex():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 270

def test_sum_squares_large_numbers():
    assert sum_squares([100, 200, 300, 400, 500]) == 150000

def test_sum_squares_negative_numbers():
    assert sum_squares([-1, -2, -3, -4, -5]) == -30