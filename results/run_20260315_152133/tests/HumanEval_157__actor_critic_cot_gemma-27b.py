import pytest
import math

def test_valid_right_triangle_3_4_5():
    """Tests a standard 3-4-5 right triangle."""
    assert right_angle_triangle(3, 4, 5) == True

def test_valid_right_triangle_5_12_13():
    """Tests a 5-12-13 right triangle."""
    assert right_angle_triangle(5, 12, 13) == True

def test_valid_right_triangle_8_15_17():
    """Tests an 8-15-17 right triangle."""
    assert right_angle_triangle(8, 15, 17) == True

def test_invalid_triangle_1_2_3():
    """Tests a degenerate triangle where the sum of two sides equals the third."""
    assert right_angle_triangle(1, 2, 3) == False

def test_invalid_triangle_scalene():
    """Tests a scalene triangle that is not a right triangle."""
    assert right_angle_triangle(2, 3, 4) == False

def test_invalid_triangle_isosceles():
    """Tests an isosceles triangle that is not a right triangle."""
    assert right_angle_triangle(5, 5, 6) == False

def test_invalid_triangle_equilateral():
    """Tests an equilateral triangle that is not a right triangle."""
    assert right_angle_triangle(5, 5, 5) == False

@pytest.mark.parametrize("a, b, c", [(0, 0, 0), (0, 4, 5), (3, 0, 5), (3, 4, 0)])
def test_zero_length_sides(a, b, c):
    """Tests triangles with zero-length sides."""
    assert right_angle_triangle(a, b, c) == False

@pytest.mark.parametrize("a, b, c", [(5, 3, 4), (4, 5, 3), (3, 5, 4)])
def test_side_order(a, b, c):
    """Tests that the order of sides doesn't matter."""
    assert right_angle_triangle(a, b, c) == True

def test_large_numbers():
    """Tests a right triangle with large numbers."""
    expected = pytest.approx(math.sqrt(1000**2 + 1000**2))
    assert right_angle_triangle(1000, 1000, expected) == True

def test_floating_point_numbers():
    """Tests a right triangle with floating-point numbers."""
    assert right_angle_triangle(3.0, 4.0, 5.0) == True

def test_almost_right_triangle_1():
    """Tests a triangle that is close to being a right triangle but isn't."""
    assert right_angle_triangle(3.0, 4.0, 5.001) == False

def test_almost_right_triangle_2():
    """Tests a triangle that is close to being a right triangle but isn't."""
    assert right_angle_triangle(3.0, 4.0, 4.999) == False

def test_invalid_input_string():
    """Tests that a TypeError is raised when a string is passed as input."""
    with pytest.raises(TypeError):
        right_angle_triangle("3", 4, 5)

def test_invalid_input_list():
    """Tests that a TypeError is raised when a list is passed as input."""
    with pytest.raises(TypeError):
        right_angle_triangle([3], 4, 5)

def test_invalid_input_none():
    """Tests that a TypeError is raised when None is passed as input."""
    with pytest.raises(TypeError):
        right_angle_triangle(None, 4, 5)

@pytest.mark.parametrize("a, b, c", [(-3, 4, 5), (3, -4, 5), (3, 4, -5), (3, -4, -5), (-3, 4, -5), (-3, -4, 5)])
def test_negative_and_positive_sides(a, b, c):
    """Tests triangles with a mix of negative and positive sides."""
    assert right_angle_triangle(a, b, c) == False