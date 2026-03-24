import pytest

def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    sides = sorted([a, b, c])
    if not all(isinstance(side, (int, float)) for side in sides):
        raise TypeError("Sides must be numeric")
    if any(side <= 0 for side in sides):
        return False
    return sides[0]**2 + sides[1]**2 == sides[2]**2

def test_valid_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True

def test_another_valid_right_triangle():
    assert right_angle_triangle(5, 12, 13) == True

def test_invalid_triangle():
    assert right_angle_triangle(1, 2, 3) == False

def test_equilateral_triangle():
    assert right_angle_triangle(1, 1, 1) == False

def test_isosceles_non_right_triangle():
    assert right_angle_triangle(2, 2, 3) == False

def test_equality_of_sides():
    assert right_angle_triangle(5, 5, 7.071) == False

def test_zero_one_side():
    assert right_angle_triangle(0, 4, 5) == False

def test_zero_two_sides():
    assert right_angle_triangle(0, 0, 5) == False

def test_zero_all_sides():
    assert right_angle_triangle(0, 0, 0) == False

def test_negative_side():
    with pytest.raises(TypeError):
        right_angle_triangle(-3, 4, 5)

def test_non_numeric_side_string():
    with pytest.raises(TypeError):
        right_angle_triangle("a", 4, 5)

def test_non_numeric_side_list():
    with pytest.raises(TypeError):
        right_angle_triangle([1], 4, 5)

def test_float_right_triangle():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True

def test_large_numbers():
    assert right_angle_triangle(600, 800, 1000) == True

def test_decimal_right_triangle():
    assert right_angle_triangle(1.5, 2.0, 2.5) == True

def test_triangle_inequality():
    assert right_angle_triangle(1, 2, 5) == False

def test_none_input():
    with pytest.raises(TypeError):
        right_angle_triangle(None, 4, 5)

def test_float_approx_right_triangle():
    assert right_angle_triangle(1.5, 2.0, 2.5) == pytest.approx(True)