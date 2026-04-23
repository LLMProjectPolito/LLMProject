
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

```python
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


import pytest

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == False # Test with spaces and punctuation
    assert is_palindrome('racecar') == True
    assert is_palindrome('madam') == True
    assert is_palindrome('level') == True
    assert is_palindrome('rotor') == True
    assert is_palindrome('deified') == True
    assert is_palindrome('refer') == True
    assert is_palindrome('stats') == True
    assert is_palindrome('noon') == True
    assert is_palindrome('kayak') == True
    assert is_palindrome('civic') == True
    assert is_palindrome('redder') == True
    assert is_palindrome('reviver') == True
    assert is_palindrome('detartrated') == True
    assert is_palindrome('a') == True
    assert is_palindrome('ab') == False
    assert is_palindrome('abba') == True

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_case_sensitive():
    assert is_palindrome('Racecar') == False
    assert is_palindrome('Madam') == False
    assert is_palindrome('Radar') == False

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([10, 5, 20, 1]) == 20
    assert get_max([1, 1, 1]) == 1
    assert get_max([100, 1, 1000, 10]) == 1000

def test_get_max_empty():
    assert get_max([]) is None

def test_get_max_negative():
    assert get_max([-1, -2, -3]) == -1
    assert get_max([-10, -5, -20]) == -5
    assert get_max([-1, -1, -1]) == -1
    assert get_max([-100, -1, -1000]) == -1

def test_get_max_mixed():
    assert get_max([-1, 0, 1]) == 1
    assert get_max([-5, 0, 5]) == 5
    assert get_max([-10, 0, 10]) == 10

def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(6, 8, 10) == True
    assert right_angle_triangle(9, 12, 15) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(4, 3, 5) == True
    assert right_angle_triangle(10, 24, 26) == True

def test_right_angle_triangle_invalid():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(4, 3, 5) == False
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(1, 2, 4) == False
    assert right_angle_triangle(2, 2, 2) == False
    assert right_angle_triangle(1, 1, 2) == False
    assert right_angle_triangle(1, 2, 5) == False
    assert right_angle_triangle(1, 2, 6) == False
    assert right_angle_triangle(1, 2, 7) == False
    assert right_angle_triangle(1, 2, 8) == False
    assert right_angle_triangle(1, 2, 9) == False
    assert right_angle_triangle(1, 2, 10) == False
    assert right_angle_triangle(1, 2, 11) == False
    assert right_angle_triangle(1, 2, 12) == False
    assert right_angle_triangle(1, 2, 13) == False
    assert right_angle_triangle(1, 2, 14) == False
    assert right_angle_triangle(1, 2, 15) == False
    assert right_angle_triangle(1, 2, 16) == False
    assert right_angle_triangle(1, 2, 17) == False
    assert right_angle_triangle(1, 2, 18) == False
    assert right_angle_triangle(1, 2, 19) == False
    assert right_angle_triangle(1, 2, 20) == False
    assert right_angle_triangle(1, 2, 21) == False
    assert right_angle_triangle(1, 2, 22) == False
    assert right_angle_triangle(1, 2, 23) == False
    assert right_angle_triangle(1, 2, 24) == False
    assert right_angle_triangle(1, 2, 25) == False
    assert right_angle_triangle(1, 2, 26) == False
    assert right_angle_triangle(1, 2, 27) == False
    assert right_angle_triangle(1, 2, 28) == False
    assert right_angle_triangle(1, 2, 29) == False
    assert right_angle_triangle(1, 2, 30) == False
    assert right_angle_triangle(1, 2, 31) == False
    assert right_angle_triangle(1, 2, 32) == False
    assert right_angle_triangle(1, 2, 33) == False
    assert right_angle_triangle(1, 2, 34) == False
    assert right_angle_triangle(1, 2, 35) == False
    assert right_angle_triangle(1, 2, 36) == False
    assert right_angle_triangle(1, 2, 37) == False
    assert right_angle_triangle(1, 2, 38) == False
    assert right_angle_triangle(1, 2, 39) == False
    assert right_angle_triangle(1, 2, 40) == False
    assert right_angle_triangle(1, 2, 41) == False
    assert right_angle_triangle(1, 2, 42) == False
    assert right_angle_triangle(1, 2, 43) == False
    assert right_angle_triangle(1, 2, 44) == False
    assert right_angle_triangle(1, 2, 45) == False
    assert right_angle_triangle(1, 2, 46) == False
    assert right_angle_triangle(1, 2, 47) == False
    assert right_angle_triangle(1, 2, 48) == False
    assert right_angle_triangle(1, 2, 49) == False
    assert right_angle_triangle(1, 2, 50) == False
    assert right_angle_triangle(1, 2, 51)