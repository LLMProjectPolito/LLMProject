
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
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]

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


# --- Tests for is_palindrome ---
def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_single_char():
    assert is_palindrome('a') == True

def test_palindrome_special_chars():
    assert is_palindrome('.,;?!') == True

def test_palindrome_mixed_case():
    assert is_palindrome('Madam') == True

def test_palindrome_with_spaces():
    assert is_palindrome('  race car  ') == True

# --- Tests for get_max ---
def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_max_single_element():
    assert get_max([5]) == 5

def test_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_max_duplicate():
    assert get_max([1, 1, 1]) == 1

# --- Tests for right_angle_triangle ---
def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True

def test_right_angle_triangle_invalid():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(4, 5, 6) == False
    assert right_angle_triangle(1, 1, 1) == False

def test_right_angle_triangle_different_order():
    assert right_angle_triangle(5, 3, 4) == True
    assert right_angle_triangle(4, 3, 5) == True

def test_right_angle_triangle_zero():
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(0, 1, 1) == False
    assert right_angle_triangle(1, 0, 1) == False
    assert right_angle_triangle(1, 1, 0) == False