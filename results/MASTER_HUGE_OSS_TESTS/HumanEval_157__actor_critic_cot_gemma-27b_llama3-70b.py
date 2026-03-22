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

@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (3, 4, 5, True),
        (5, 12, 13, True),
        (8, 15, 17, True),
        (4, 3, 5, True),
        (12, 5, 13, True),
        (15, 8, 17, True),
    ],
)
def test_valid_right_triangles(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, 2, 3, False),
        (5, 6, 7, False),
        (2, 2, 3, False),
        (7, 8, 9, False),
    ],
)
def test_invalid_triangles(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (0, 0, 0, False),
        (0, 4, 5, False),
        (3, 0, 5, False),
        (3, 4, 0, False),
    ],
)
def test_zero_length_sides(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (-3, 4, 5, False),
        (3, -4, 5, False),
        (3, 4, -5, False),
        (-3, -4, -5, False),
    ],
)
def test_negative_length_sides(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1000000, 1000000, 1414213, True),
        (1e18, 1e18, 1.4142135623730951e18, True),
    ],
)
def test_large_numbers(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (3.0, 4.0, 5.0, True),
        (3.1, 4.1, 5.1, False),
    ],
)
def test_floating_point_numbers(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, 1, 2, False),  # Triangle inequality violation
        (1, 2, 4, False),  # Triangle inequality violation
        (5, 1, 3, False),  # Triangle inequality violation
    ],
)
def test_triangle_inequality(a, b, c, expected):
    assert right_angle_triangle(a, b, c) == expected

@pytest.mark.parametrize(
    "a, b, c",
    [
        ("3", "4", "5"),
        ([3], 4, 5),
        (3, "4", 5),
        (3, 4, "5"),
        (None, 4, 5),
        (3, None, 5),
        (3, 4, None),
    ],
)
def test_invalid_input_types(a, b, c):
    with pytest.raises(TypeError):
        right_angle_triangle(a, b, c)

@pytest.mark.parametrize(
    "a, b, c",
    [
        (1, 1, 1),  # Isosceles
        (5, 5, 5 * 2**0.5), # Isosceles
    ]
)
def test_isosceles_right_triangles(a, b, c):
    assert right_angle_triangle(a, b, c) == True