def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True

def test_right_angle_triangle_invalid():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(6, 7, 8) == False

def test_right_angle_triangle_zero():
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(0, 4, 5) == False
    assert right_angle_triangle(3, 0, 5) == False
    assert right_angle_triangle(3, 4, 0) == False

def test_right_angle_triangle_negative():
    assert right_angle_triangle(-3, 4, 5) == False
    assert right_angle_triangle(3, -4, 5) == False
    assert right_angle_triangle(3, 4, -5) == False
    assert right_angle_triangle(-3, -4, -5) == False

def test_right_angle_triangle_same_sides():
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(2, 2, 2) == False