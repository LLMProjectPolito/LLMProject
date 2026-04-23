
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


# Pytest tests for is_palindrome
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('Racecar') == True  # Test case-insensitivity
    assert is_palindrome('A man, a plan, a canal: Panama') == False # Test with spaces and punctuation
    assert is_palindrome('madam') == True

def test_palindrome_empty():
    assert is_palindrome('') == True
    assert is_palindrome(' ') == True # Test with a single space

def test_palindrome_single_char():
    assert is_palindrome('a') == True

# Pytest tests for get_max
def test_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([5, 2, 8, 1, 9]) == 9
    assert get_max([10]) == 10

def test_max_empty():
    assert get_max([]) == None

def test_max_negative():
    assert get_max([-1, -2, -3]) == -1
    assert get_max([-5, -2, -8, -1, -9]) == -1

def test_max_mixed():
    assert get_max([-1, 2, -3, 4, -5]) == 4

# Pytest tests for right_angle_triangle
def test_right_angle_triangle_basic():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True

def test_right_angle_triangle_not_right():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(3, 4, 6) == False
    assert right_angle_triangle(5, 6, 7) == False

def test_right_angle_triangle_zero():
    assert right_angle_triangle(0, 0, 0) == True #Consider zero length sides as a degenerate right triangle
    assert right_angle_triangle(3, 4, 0) == False
    assert right_angle_triangle(0, 4, 5) == False

def test_right_angle_triangle_large_numbers():
    assert right_angle_triangle(1000, 1000, 1414) == True