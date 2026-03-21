import pytest

def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False

def test_right_angle_triangle_negative_numbers():
    with pytest.raises(ValueError):
        right_angle_triangle(-3, 4, 5)

def test_right_angle_triangle_zero():
    with pytest.raises(ValueError):
        right_angle_triangle(0, 4, 5)

def test_right_angle_triangle_floats():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True

def test_right_angle_triangle_non_numeric_input():
    with pytest.raises(TypeError):
        right_angle_triangle('a', 4, 5)

def test_right_angle_triangle_unordered_sides():
    assert right_angle_triangle(5, 3, 4) == True
    assert right_angle_triangle(4, 5, 3) == True
    assert right_angle_triangle(3, 5, 4) == True

def test_right_angle_triangle_equal_sides():
    assert right_angle_triangle(3, 3, 3*3**0.5) == True

def test_right_angle_triangle_isosceles_right_triangle():
    assert right_angle_triangle(1, 1, 1*2**0.5) == True