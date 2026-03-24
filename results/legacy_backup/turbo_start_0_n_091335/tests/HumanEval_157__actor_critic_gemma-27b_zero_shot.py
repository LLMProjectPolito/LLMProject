import pytest

def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Raises ValueError if any side is negative.
    Returns False if the sides do not form a valid triangle (triangle inequality).
    Returns False if any side is zero.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    if any(side < 0 for side in [a, b, c]):
        raise ValueError("Sides cannot be negative.")
    if any(side == 0 for side in [a, b, c]):
        return False

    sides = sorted([a, b, c])
    if sides[0] + sides[1] <= sides[2]:
        return False

    return pytest.approx(sides[0]**2 + sides[1]**2) == sides[2]**2

def test_valid_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True

def test_invalid_triangle():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(6, 7, 8) == False
    assert right_angle_triangle(1, 1, 1) == False

def test_zero_sides():
    assert right_angle_triangle(0, 3, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 5, 0) == False
    assert right_angle_triangle(0, 0, 0) == False

def test_raises_value_error_for_negative_sides():
    with pytest.raises(ValueError):
        right_angle_triangle(-3, 4, 5)
    with pytest.raises(ValueError):
        right_angle_triangle(3, -4, 5)
    with pytest.raises(ValueError):
        right_angle_triangle(3, 4, -5)
    with pytest.raises(ValueError):
        right_angle_triangle(-3, -4, -5)

def test_floating_point_precision():
    assert right_angle_triangle(1, 1, 1.41421356237) == True
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(0.3, 0.4, 0.5) == True
    assert right_angle_triangle(1, 1, 1.41421356237 + 0.0000000001) == False
    assert right_angle_triangle(1, 1, 1.41421356237 - 0.0000000001) == False

def test_large_numbers():
    assert right_angle_triangle(1000, 1000, 1414.2135623730951) == True
    assert right_angle_triangle(1000, 1001, 1002) == False

def test_almost_right_triangle():
    assert right_angle_triangle(3, 4, 5.000000001) == False
    assert right_angle_triangle(3, 4, 4.999999999) == False