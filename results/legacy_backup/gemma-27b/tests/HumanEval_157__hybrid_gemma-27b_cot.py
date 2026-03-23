import pytest

def test_valid_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True

def test_invalid_right_triangle():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(6, 8, 10) == True
    assert right_angle_triangle(6, 8, 11) == False

def test_zero_length_sides():
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False

def test_negative_length_sides():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False
    assert right_angle_triangle(-3, -4, -5) == False

def test_equal_sides():
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(1, 1, 1.41421356237) == True  # Approximately sqrt(2)
    assert right_angle_triangle(5, 5, 5*2**0.5) == True

def test_float_sides():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(1.5, 2.0, 2.5) == True
    assert right_angle_triangle(3.1, 4.1, 5.1) == False

def test_large_numbers():
    assert right_angle_triangle(1000, 1000, 1414.21356237) == True
    assert right_angle_triangle(1000, 1000, 1415) == False

def test_side_order():
    assert right_angle_triangle(4, 3, 5) == True
    assert right_angle_triangle(5, 3, 4) == True
    assert right_angle_triangle(3, 5, 4) == True

def test_float_length_sides():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(5.0, 12.0, 13.0) == True
    assert right_angle_triangle(3.1, 4.1, 5.1) == False
    assert right_angle_triangle(0.3, 0.4, 0.5) == True

def test_large_numbers_2():
    assert right_angle_triangle(1000, 1000, 1414) == False
    assert right_angle_triangle(1000, 1000, 1414.2135623730951) == True

def test_same_sides():
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(2, 2, 2) == False

def test_sides_out_of_order():
    assert right_angle_triangle(4, 3, 5) == True
    assert right_angle_triangle(5, 3, 4) == True
    assert right_angle_triangle(12, 5, 13) == True

def test_edge_case_close_to_right():
    assert right_angle_triangle(3, 4, 5.00000000001) == False
    assert right_angle_triangle(3, 4, 4.99999999999) == False