def test_right_angle_triangle_valid():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(8, 15, 17) == True
    assert right_angle_triangle(7, 24, 25) == True

def test_right_angle_triangle_invalid():
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(1, 1, 1) == False
    assert right_angle_triangle(2, 3, 4) == False
    assert right_angle_triangle(10, 20, 30) == False

def test_right_angle_triangle_zero():
    assert right_angle_triangle(0, 0, 0) == False
    assert right_angle_triangle(0, 1, 1) == False
    assert right_angle_triangle(1, 0, 1) == False
    assert right_angle_triangle(1, 1, 0) == False

def test_right_angle_triangle_large_numbers():
    assert right_angle_triangle(1000, 1000, 1414) == True
    assert right_angle_triangle(1000, 1001, 1001) == False

def test_right_angle_triangle_float_numbers():
    assert right_angle_triangle(3.0, 4.0, 5.0) == True
    assert right_angle_triangle(1.0, 2.0, 3.0) == False