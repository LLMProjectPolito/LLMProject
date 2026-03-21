import pytest

def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True

def test_right_angle_triangle_negative_numbers():
    with pytest.raises(ValueError):
        right_angle_triangle(-3, 4, 5)
    with pytest.raises(ValueError):
        right_angle_triangle(3, -4, 5)
    with pytest.raises(ValueError):
        right_angle_triangle(3, 4, -5)

def test_right_angle_triangle_zero():
    with pytest.raises(ValueError):
        right_angle_triangle(0, 4, 5)
    with pytest.raises(ValueError):
        right_angle_triangle(3, 0, 5)
    with pytest.raises(ValueError):
        right_angle_triangle(3, 4, 0)

def test_right_angle_triangle_non_numeric_input():
    with pytest.raises(TypeError):
        right_angle_triangle('a', 4, 5)
    with pytest.raises(TypeError):
        right_angle_triangle(3, 'b', 5)
    with pytest.raises(TypeError):
        right_angle_triangle(3, 4, 'c')

def test_right_angle_triangle_float_input():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(1.0, 2.0, 3.0) == False