import pytest

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

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

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_right_angle_triangle_true():
    assert right_angle_triangle(3, 4, 5) == True

def test_right_angle_triangle_false():
    assert right_angle_triangle(1, 2, 3) == False

def test_right_angle_triangle_equal():
    assert right_angle_triangle(5, 12, 13) == True

def test_right_angle_triangle_zero():
    assert right_angle_triangle(0, 0, 0) == False

def test_right_angle_triangle_small():
    assert right_angle_triangle(1, 1, 1) == False

def test_right_angle_triangle_negative():
    assert right_angle_triangle(-3, 4, 5) == False