import pytest

def test_sum_squares_empty():
    assert sum_squares([]) == 0

def test_sum_squares_basic1():
    assert sum_squares([1, 2, 3]) == 6

def test_sum_squares_basic2():
    assert sum_squares([1, 2, 3, 4]) == 1 + 2 + 9 + 64 == 76

def test_sum_squares_basic3():
    assert sum_squares([1, 2, 3, 4, 5, 6]) == 1 + 2 + 9 + 64 + 5 + 36 == 117

def test_sum_squares_negative():
    assert sum_squares([-1, -5, 2, -1, -5]) == -1 + -5 + 4 + -1 + -125 == -138

def test_sum_squares_mixed():
    assert sum_squares([1, -2, 3, -4, 5, -6]) == 1 + -2 + 9 + -64 + 5 + -216 == -297

def test_sum_squares_zeros():
    assert sum_squares([0, 0, 0, 0]) == 0

def test_sum_squares_large_numbers():
    assert sum_squares([100, 200, 300, 400]) == 100 + 200 + 90000 + 64000000 == 64090300

def test_sum_squares_multiple_of_3_and_4():
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 1 + 2 + 9 + 64 + 5 + 216 + 7 + 512 + 81 + 100 + 121 + 144 == 1062