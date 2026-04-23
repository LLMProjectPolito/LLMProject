
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
    if not all(isinstance(side, (int, float)) for side in [a, b, c]):
        raise TypeError("Sides must be numbers (int or float)")
    if any(side <= 0 for side in [a, b, c]):
        raise ValueError("Sides must be positive")

    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()  # Ignore case
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


class TestRightAngleTriangle:
    def test_right_angle_triangle_basic(self):
        assert right_angle_triangle(3, 4, 5) == True
        assert right_angle_triangle(5, 12, 13) == True
        assert right_angle_triangle(8, 15, 17) == True
        assert right_angle_triangle(7, 24, 25) == True

    def test_right_angle_triangle_not_right(self):
        assert right_angle_triangle(1, 2, 3) == False
        assert right_angle_triangle(2, 3, 4) == False
        assert right_angle_triangle(1, 1, 1) == False
        assert right_angle_triangle(5, 6, 7) == False
        assert right_angle_triangle(10, 10, 10) == False

    def test_right_angle_triangle_zero_side(self):
        assert right_angle_triangle(0, 4, 5) == False
        assert right_angle_triangle(3, 0, 5) == False
        assert right_angle_triangle(3, 4, 0) == False
        assert right_angle_triangle(0, 0, 0) == False
        assert right_angle_triangle(0, 0, 1) == False

    def test_right_angle_triangle_negative_side(self):
        with pytest.raises(ValueError):
            right_angle_triangle(-3, 4, 5)
        with pytest.raises(ValueError):
            right_angle_triangle(3, -4, 5)
        with pytest.raises(ValueError):
            right_angle_triangle(3, 4, -5)
        with pytest.raises(ValueError):
            right_angle_triangle(-3, -4, 5)
        with pytest.raises(ValueError):
            right_angle_triangle(-3, 4, -5)
        with pytest.raises(ValueError):
            right_angle_triangle(-3, -4, -5)

    def test_right_angle_triangle_floats(self):
        assert right_angle_triangle(3.0, 4.0, 5.0) == True
        assert right_angle_triangle(3.14, 4.2, 5.3) == True
        assert right_angle_triangle(1.0, 1.0, 1.414) == True #approx sqrt 2
        assert right_angle_triangle(1.0, 1.0, 1.0) == False
    
    def test_right_angle_triangle_large_numbers(self):
        assert right_angle_triangle(1000000, 1000000, 1414213.56) == True
        assert right_angle_triangle(1000000, 1000000, 1000001) == False

class TestIsPalindrome:
    def test_palindrome_basic(self):
        assert is_palindrome('radar') == True
        assert is_palindrome('hello') == False

    def test_palindrome_empty(self):
        assert is_palindrome('') == True

    def test_palindrome_case_insensitive(self):
        assert is_palindrome('Racecar') == True
        assert is_palindrome('A man, a plan, a canal: Panama') == False #spaces and punctuation

    def test_palindrome_single_char(self):
        assert is_palindrome('a') == True

class TestGetMax:
    def test_max_positive(self):
        assert get_max([1, 2, 3]) == 3

    def test_max_empty(self):
        assert get_max([]) == None

    def test_max_negative(self):
        assert get_max([-1, -2, -3]) == -1

    def test_max_mixed(self):
        assert get_max([-1, 2, -3, 4]) == 4

    def test_max_single_element(self):
        assert get_max([5]) == 5