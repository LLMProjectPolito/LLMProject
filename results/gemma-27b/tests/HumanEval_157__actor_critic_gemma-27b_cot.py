
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

import pytest
from decimal import Decimal

def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True

def test_right_angle_triangle_invalid():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(6, 8, 11) == False

def test_right_angle_triangle_zero():
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False
    assert right_angle_triangle(0, 0, 5) == False

def test_right_angle_triangle_negative_sides():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False
    assert right_angle_triangle(-3, -4, -5) == False

def test_right_angle_triangle_float():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(5.0, 12.0, 13.0) == True
    assert right_angle_triangle(1.5, 2.0, 2.5) == True
    assert right_angle_triangle(1.0, 2.0, 3.0) == False

def test_right_angle_triangle_large_numbers():
    assert right_angle_triangle(1000, 1000, 1414) == False
    assert right_angle_triangle(1000, 1000, 1414.2135623730951) == pytest.approx(True)

def test_right_angle_triangle_equilateral():
    assert right_angle_triangle(5, 5, 5) == False
    assert right_angle_triangle(10, 10, 10) == False

def test_right_angle_triangle_different_order():
    assert right_angle_triangle(4, 3, 5) == True
    assert right_angle_triangle(5, 3, 4) == True
    assert right_angle_triangle(3, 5, 4) == True

def test_right_angle_triangle_zero_length_sides():
    assert right_angle_triangle(0, 0, 5) == False
    assert right_angle_triangle(0, 5, 0) == False
    assert right_angle_triangle(5, 0, 0) == False

def test_right_angle_triangle_decimal():
    assert right_angle_triangle(Decimal('3'), Decimal('4'), Decimal('5')) == True
    assert right_angle_triangle(Decimal('1.5'), Decimal('2'), Decimal('2.5')) == True
    assert right_angle_triangle(Decimal('1'), Decimal('2'), Decimal('3')) == False