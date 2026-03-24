
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
    s = ''.join(filter(str.isalnum, s)).lower()
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


def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True
    assert is_palindrome('Madam') == True
    assert is_palindrome('121') == True
    assert is_palindrome('12321') == True
    assert is_palindrome('ab') == False
    assert is_palindrome('a') == True
    assert is_palindrome('') == True


def test_is_palindrome_non_alphanumeric():
    assert is_palindrome('!@#$') == True
    assert is_palindrome('123') == False
    assert is_palindrome('a!b@c') == False

def test_is_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True
    assert is_palindrome('RaceCar') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([3, 2, 1]) == 3
    assert get_max([1, 3, 2]) == 3
    assert get_max([5, 5, 5]) == 5
    assert get_max([-1, 0, 1]) == 1

def test_get_max_empty():
    assert get_max([]) == None

def test_get_max_single_element():
    assert get_max([5]) == 5

def test_get_max_negative_numbers():
    assert get_max([-1, -2, -3]) == -1

def test_right_angle_triangle_true():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True


def test_right_angle_triangle_false():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(3, 4, 6) == False
    assert right_angle_triangle(5, 6, 7) == False
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(1, 2, 2.5) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(3, 4, 5) == False

def test_right_angle_triangle_equal_sides():
    assert right_angle_triangle(5, 5, 5) == False

def test_right_angle_triangle_zero_side():
    assert right_angle_triangle(0, 3, 4) == False
    assert right_angle_triangle(3, 0, 4) == False
    assert right_angle_triangle(3, 4, 0) == False