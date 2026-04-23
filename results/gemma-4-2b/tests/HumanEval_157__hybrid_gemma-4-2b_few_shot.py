
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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
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

def test_palindrome_single_char():
    assert is_palindrome('a') == True

def test_palindrome_mixed_case():
    assert is_palindrome('Racecar') == False

def test_palindrome_with_spaces():
    assert is_palindrome('A man, a plan, a canal: Panama') == False

def test_right_angle_triangle_positive():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(6, 8, 10) == True
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(1, 2, 2) == False
    assert right_angle_triangle(0, 0, 0) == False

def test_right_angle_triangle_negative():
    assert right_angle_triangle(-3, 4, 5) == True
    assert right_angle_triangle(3, -4, 5) == True
    assert right_angle_triangle(3, 4, -5) == True
    assert right_angle_triangle(-3, -4, -5) == False
    assert right_angle_triangle(-1, 2, 2) == False

def test_right_angle_triangle_zero():
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(0, 1, 1) == False
    assert right_angle_triangle(1, 0, 0) == False
    assert right_angle_triangle(0, 0, 1) == False
    assert right_angle_triangle(1, 1, 0) == False

def test_right_angle_triangle_equal_sides():
    assert right_angle_triangle(5, 5, 5) == False
    assert right_angle_triangle(1, 1, 1) == False

def test_right_angle_triangle_large_numbers():
    assert right_angle_triangle(1000, 2000, 2200) == True
    assert right_angle_triangle(1000, 2000, 2199) == False

def test_right_angle_triangle_decimal_sides():
    assert right_angle_triangle(3.5, 4.2, 5.3) == True
    assert right_angle_triangle(1.5, 2.5, 3.7) == False

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_single_element():
    assert get_max([5]) == 5

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_get_max_mixed():
    assert get_max([-1, 0, 1]) == 1

def test_get_max_duplicate():
    assert get_max([1, 1, 1]) == 1