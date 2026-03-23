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
    return sides[0]**2 + sides[1]**2 == sides[2]**2

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True
    assert right_angle_triangle(6, 8, 10) == True

def test_right_angle_triangle_invalid():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(6, 7, 8) == False

def test_right_angle_triangle_zero_sides():
    assert right_angle_triangle(0, 0, 0) == True  # Technically a degenerate case, but satisfies the equation
    assert right_angle_triangle(0, 3, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 5, 0) == False

def test_right_angle_triangle_negative_sides():
    assert right_angle_triangle(-3, 4, 5) == False # Sides cannot be negative
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False
    assert right_angle_triangle(-3, -4, -5) == False

def test_right_angle_triangle_equal_sides():
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(1, 1, 1.41421356) == True #approx sqrt(2)
    assert right_angle_triangle(1, 1, 1.41421356237) == True #approx sqrt(2)
    assert right_angle_triangle(2, 2, 2.82842712475) == True #approx 2*sqrt(2)

def test_right_angle_triangle_large_numbers():
    assert right_angle_triangle(1000, 1000, 1414.21356) == True #approx sqrt(2) * 1000
    assert right_angle_triangle(1000, 1000, 1414.21356237) == True #approx 1000*sqrt(2)
    assert right_angle_triangle(100, 100, 141.421356237) == True #approx 100*sqrt(2)
    assert right_angle_triangle(1000, 1000, 1001) == False

def test_right_angle_triangle_float_sides():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(3.5, 4.5, 5.700877) == True #approx sqrt(3.5^2 + 4.5^2)
    assert right_angle_triangle(3.5, 4.5, 5.7) == False
    assert right_angle_triangle(1.5, 2.0, 2.5) == True

def test_right_angle_triangle_order_agnostic():
    assert right_angle_triangle(4, 3, 5) == True
    assert right_angle_triangle(5, 3, 4) == True
    assert right_angle_triangle(3, 5, 4) == True

# Palindrome tests
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True

def test_palindrome_mixed_case():
    assert is_palindrome('Racecar') == False # Case sensitive

# Max tests
def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4