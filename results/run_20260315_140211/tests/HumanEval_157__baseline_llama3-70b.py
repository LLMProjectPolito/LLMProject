import pytest

def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False

def test_right_angle_triangle_zero_length():
    with pytest.raises(ValueError):
        right_angle_triangle(0, 3, 4)

def test_right_angle_triangle_negative_length():
    with pytest.raises(ValueError):
        right_angle_triangle(-1, 3, 4)

def test_right_angle_triangle_non_numeric_input():
    with pytest.raises(TypeError):
        right_angle_triangle('a', 3, 4)

def test_right_angle_triangle_float_input():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True

def test_right_angle_triangle_large_input():
    assert right_angle_triangle(3000, 4000, 5000) == True

def test_right_angle_triangle_edge_cases():
    assert right_angle_triangle(1, 1, 1.4142135623730951) == True
    assert right_angle_triangle(1, 1, 2) == False

def test_right_angle_triangle_permutations():
    assert right_angle_triangle(3, 4, 5) == right_angle_triangle(4, 3, 5)
    assert right_angle_triangle(3, 4, 5) == right_angle_triangle(5, 3, 4)
    assert right_angle_triangle(3, 4, 5) == right_angle_triangle(5, 4, 3)