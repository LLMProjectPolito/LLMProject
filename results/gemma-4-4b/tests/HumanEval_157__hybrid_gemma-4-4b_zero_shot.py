
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
    sides = sorted([a, b, c])
    return sides[0]**2 + sides[1]**2 == sides[2]**2

class TestRightAngleTriangle:

    def test_valid_right_triangle(self):
        assert right_angle_triangle(3, 4, 5) == True
        assert right_angle_triangle(5, 12, 13) == True
        assert right_angle_triangle(8, 15, 17) == True
        assert right_angle_triangle(20, 21, 29) == True
        assert right_angle_triangle(7, 24, 25) == True


    def test_invalid_triangle(self):
        assert right_angle_triangle(1, 2, 3) == False
        assert right_angle_triangle(1, 1, 1) == False
        assert right_angle_triangle(1, 1, 2) == False
        assert right_angle_triangle(5, 6, 7) == False
        assert right_angle_triangle(10, 10, 10) == False

    def test_zero_side(self):
        assert right_angle_triangle(0, 4, 5) == False
        assert right_angle_triangle(3, 0, 5) == False
        assert right_angle_triangle(3, 4, 0) == False
        assert right_angle_triangle(0, 0, 0) == False

    def test_negative_side(self):
      with pytest.raises(ValueError):
          right_angle_triangle(-3, 4, 5)
      with pytest.raises(ValueError):
          right_angle_triangle(3, -4, 5)
      with pytest.raises(ValueError):
          right_angle_triangle(3, 4, -5)
      with pytest.raises(ValueError):
          right_angle_triangle(-3, -4, -5)

    def test_equal_sides(self):
        assert right_angle_triangle(5, 5, 5) == False
        assert right_angle_triangle(4, 4, 4) == False

    def test_large_numbers(self):
      assert right_angle_triangle(1000, 1000, 1414) == True
      assert right_angle_triangle(10000, 10000, 14142) == True

    def test_float_sides(self):
      assert right_angle_triangle(3.0, 4.0, 5.0) == True
      assert right_angle_triangle(5.5, 12.0, 13.0) == True
      assert right_angle_triangle(3.14, 4.2, 5.0) == True
      assert right_angle_triangle(1.0, 2.0, 3.0) == False

    def test_edge_cases(self):
        assert right_angle_triangle(1, 1, 1.41421356237) == True #approx sqrt(2)
        assert right_angle_triangle(2, 2, 2.82842712475) == True #approx sqrt(3)
        assert right_angle_triangle(3, 3, 4.24264068712) == True #approx sqrt(5)


    def test_invalid_input_types(self):
      with pytest.raises(TypeError):
        right_angle_triangle("3", 4, 5)
      with pytest.raises(TypeError):
        right_angle_triangle(3, "4", 5)
      with pytest.raises(TypeError):
        right_angle_triangle(3, 4, "5")
      with pytest.raises(TypeError):
        right_angle_triangle([3,4,5], 1, 2) #test if list is passed.

Suite 2:

    def test_valid_right_triangle(self):
        assert right_angle_triangle(3, 4, 5) == True
        assert right_angle_triangle(5, 12, 13) == True
        assert right_angle_triangle(8, 15, 17) == True
        assert right_angle_triangle(20, 21, 29) == True
        assert right_angle_triangle(7, 24, 25) == True
        assert right_angle_triangle(6, 8, 10) == True


    def test_invalid_triangle(self):
        assert right_angle_triangle(1, 2, 3) == False
        assert right_angle_triangle(1, 1, 1) == False
        assert right_angle_triangle(10, 10, 10) == False
        assert right_angle_triangle(2, 3, 4) == False
        assert right_angle_triangle(5, 6, 7) == False
        assert right_angle_triangle(1, 5, 7) == False


    def test_zero_length_sides(self):
        assert right_angle_triangle(0, 0, 0) == False
        assert right_angle_triangle(0, 1, 1) == False
        assert right_angle_triangle(1, 0, 1) == False
        assert right_angle_triangle(1, 1, 0) == False
        assert right_angle_triangle(0, 0, 1) == False

    def test_negative_length_sides(self):
         with pytest.raises(ValueError):
            right_angle_triangle(-3, 4, 5)
         with pytest.raises(ValueError):
            right_angle_triangle(3, -4, 5)
         with pytest.raises(ValueError):
            right_angle_triangle(3, 4, -5)
         with pytest.raises(ValueError):
            right_angle_triangle(-3, -4, -5)
         with pytest.raises(ValueError):
            right_angle_triangle(-1, 2, 3)


    def test_duplicate_sides(self):
      assert right_angle_triangle(5,5,5) == False
      assert right_angle_triangle(5,5,10) == False
      assert right_angle_triangle(10,5,5) == False

    def test_large_numbers(self):
      assert right_angle_triangle(1000, 1000, 1414) == True
      assert right_angle_triangle(1000, 1000, 1001) == False
      assert right_angle_triangle(10000, 10000, 14142) == True

    def test_float_numbers(self):
        assert right_angle_triangle(3.0, 4.0, 5.0) == True
        assert right_angle_triangle(1.5, 2.0, 2.5) == True
        assert right_angle_triangle(1.1, 2.2, 2.5) == False
        assert right_angle_triangle(10.0, 10.0, 14.14) == True