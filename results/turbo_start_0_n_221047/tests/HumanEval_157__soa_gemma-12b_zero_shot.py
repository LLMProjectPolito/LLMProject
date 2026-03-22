import pytest
from your_module import right_angle_triangle  # Replace your_module

def test_valid_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True
    assert right_angle_triangle(20, 21, 29) == True
    assert right_angle_triangle(6, 8, 10) == True
    assert right_angle_triangle(9, 12, 15) == True

def test_invalid_right_triangle():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(4, 5, 6) == False
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(1, 2, 2) == False
    assert right_angle_triangle(5, 5, 5) == False
    assert right_angle_triangle(10, 11, 12) == False

def test_edge_cases():
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(1, 0, 1) == False
    assert right_angle_triangle(0, 1, 1) == False
    assert right_angle_triangle(1, 1, 0) == False
    assert right_angle_triangle(3, 4, 4) == False
    assert right_angle_triangle(4, 3, 4) == False
    assert right_angle_triangle(4, 4, 3) == False

def test_float_inputs():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(1.0, 2.0, 3.0) == False
    assert right_angle_triangle(0.5, 1.2, 1.3) == True
    assert right_angle_triangle(0.5, 1.0, 1.0) == False

def test_large_numbers():
    assert right_angle_triangle(1000, 1000, 1414.21356) == True
    assert right_angle_triangle(1000, 1001, 1002) == False

def test_input_types():
    with pytest.raises(TypeError):
        right_angle_triangle("3", 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle(3, "4", 5)
    with pytest.raises(TypeError):
        right_angle_triangle(3, 4, "5")
    with pytest.raises(TypeError):
        right_angle_triangle(3, 4, None)
    with pytest.raises(TypeError):
        right_angle_triangle(None, 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle(3, None, 5)
    with pytest.raises(TypeError):
        right_angle_triangle(3, 4, [5])
    with pytest.raises(TypeError):
        right_angle_triangle([3], 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle(3, [4], 5)

def test_negative_inputs():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False
    assert right_angle_triangle(-3, -4, -5) == False