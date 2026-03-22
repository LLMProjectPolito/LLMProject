import pytest

def test_basic_right_triangles():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True

def test_non_right_triangles():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(2, 2, 3) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(6, 7, 8) == False

def test_zero_length_sides():
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False
    assert right_angle_triangle(0, 0, 5) == False
    assert right_angle_triangle(0, 0, 0) == False

def test_negative_length_sides():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False
    assert right_angle_triangle(-3, -4, 5) == False
    assert right_angle_triangle(-3, -4, -5) == False

def test_floating_point_numbers():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(6.0, 8.0, 10.0) == True
    assert right_angle_triangle(1.5, 2.0, 2.5) == True
    assert right_angle_triangle(0.3, 0.4, 0.5) == True
    assert right_angle_triangle(3.1, 4.1, 5.1) == False

def test_almost_right_triangle():
    assert right_angle_triangle(3.0001, 4, 5) == False
    assert right_angle_triangle(3, 4.0001, 5) == False

def test_order_of_sides():
    assert right_angle_triangle(4, 3, 5) == True
    assert right_angle_triangle(5, 3, 4) == True
    assert right_angle_triangle(4, 5, 3) == True
    assert right_angle_triangle(5, 4, 3) == True

def test_large_numbers():
    assert right_angle_triangle(1000, 1000, 1414.21356) == True
    assert right_angle_triangle(1000, 1000, 1414.21356237) == True
    assert right_angle_triangle(1000, 1000, 1001) == False

def test_invalid_triangle_inequality():
    assert right_angle_triangle(1, 2, 5) == False
    assert right_angle_triangle(10, 2, 5) == False
    assert right_angle_triangle(1, 5, 2) == False
    assert right_angle_triangle(5, 1, 2) == False

def test_edge_cases_small_numbers():
    assert right_angle_triangle(0.1, 0.2, 0.22360679775) == True
    assert right_angle_triangle(0.1, 0.2, 0.3) == False

def test_duplicate_sides():
    assert right_angle_triangle(3, 3, 3 * 2**0.5) == True
    assert right_angle_triangle(5, 5, 5) == False
    assert right_angle_triangle(4, 4, 5) == False