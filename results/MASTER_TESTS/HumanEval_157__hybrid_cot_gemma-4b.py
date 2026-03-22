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
    a, b, c = sides[0], sides[1], sides[2]
    return abs(a**2 + b**2 - c**2) < 1e-6  # Using a small tolerance for floating-point comparisons


def test_basic_right_triangle():
    assert right_angle_triangle(3, 4, 5) == True

def test_basic_non_right_triangle():
    assert right_angle_triangle(1, 2, 3) == False

def test_zero_side():
    assert right_angle_triangle(0, 4, 5) == False

def test_negative_side():
    assert right_angle_triangle(-3, 4, 5) == False

def test_small_sides():
    assert right_angle_triangle(1, 1, 1) == False

def test_equilateral_triangle():
    assert right_angle_triangle(5, 5, 5) == False

def test_isosceles_right_triangle():
    assert right_angle_triangle(1, 1, 1.41421356237) == True

def test_large_sides():
    assert right_angle_triangle(100, 100, 141.421356237) == True

def test_sides_in_different_order():
    assert right_angle_triangle(4, 3, 5) == True

def test_sides_close_to_right_triangle():
    assert right_angle_triangle(5, 12, 13) == True

def test_sides_almost_right_triangle():
    assert right_angle_triangle(6, 8, 10) == True

def test_invalid_triangle():
    assert right_angle_triangle(1, 2, 5) == False

def test_edge_case_small_numbers():
    assert right_angle_triangle(0.1, 0.2, 0.3) == False

def test_edge_case_large_numbers():
    assert right_angle_triangle(1000, 2000, 3000) == True

def test_zero_length_sides():
    assert right_angle_triangle(0, 0, 0) == False

def test_reverse_order():
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(13, 5, 12) == True

def test_small_values():
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(1, 1, 1.41421356237) == True

def test_large_values():
    assert right_angle_triangle(1000, 1000, 141421356.237) == True

def test_equilateral_triangle():
    assert right_angle_triangle(5, 5, 5) == False

def test_isosceles_triangle():
    assert right_angle_triangle(5, 5, 6) == False

def test_right_triangle_pythagorean():
    assert right_angle_triangle(3, 4, 5) == True

def test_non_right_triangle():
    assert right_angle_triangle(1, 2, 3) == False

def test_identical_sides():
    assert right_angle_triangle(5, 5, 5) == False