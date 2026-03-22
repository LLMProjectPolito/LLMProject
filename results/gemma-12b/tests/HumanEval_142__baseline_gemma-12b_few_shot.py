def test_sum_squares_basic():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_negative():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_mixed():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 130

def test_sum_squares_multiple_of_both():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 12]) == 154

def test_sum_squares_only_multiples_of_3():
    assert sum_squares([3, 6, 9, 12]) == 3*3 + 6*6 + 9*9 + 12*12

def test_sum_squares_only_multiples_of_4():
    assert sum_squares([4, 8, 12, 16]) == 4*4 + 8*8 + 12*12 + 16*16

def test_sum_squares_zero():
    assert sum_squares([0, 0, 0, 0]) == 0

def test_sum_squares_large_numbers():
    assert sum_squares([100, 200, 300, 400]) == 100*100 + 200*200 + 300*300 + 400*400