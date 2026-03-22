import math
import pytest
from solution import right_angle_triangle  # adjust import path as needed


@pytest.mark.parametrize(
    "sides,expected",
    [
        # Classic integer right triangles (any order)
        ((3, 4, 5), True),
        ((5, 3, 4), True),
        ((4, 5, 3), True),

        # Larger integer right triangles
        ((5, 12, 13), True),
        ((13, 5, 12), True),

        # Float right triangles (scaled 3‑4‑5)
        ((0.3, 0.4, 0.5), True),
        ((0.5, 0.3, 0.4), True),

        # Very large numbers – scaling should preserve right‑angle property
        ((3000000, 4000000, 5000000), True),

        # Non‑right triangles that still satisfy triangle inequality
        ((2, 3, 4), False),
        ((7, 10, 12), False),

        # Degenerate cases (sum of two sides equals the third) – not a triangle
        ((1, 2, 3), False),
        ((5, 5, 10), False),

        # Invalid side lengths (zero or negative) – cannot form a triangle
        ((0, 4, 5), False),
        ((-3, 4, 5), False),

        # Near‑right triangle – testing floating‑point tolerance (should be False)
        ((1, 1, math.sqrt(2) * 0.999999), False),

        # Isosceles right triangle
        ((1, 1, math.sqrt(2)), True),

        # Permutation of isosceles right triangle
        ((math.sqrt(2), 1, 1), True),
    ],
)
def test_right_angle_triangle_various(sides, expected):
    a, b, c = sides
    assert right_angle_triangle(a, b, c) is expected


def test_right_angle_triangle_symmetry():
    """Explicitly verify that the function is order‑independent."""
    base = (6, 8, 10)  # known right triangle
    permutations = [
        base,
        (6, 10, 8),
        (8, 6, 10),
        (8, 10, 6),
        (10, 6, 8),
        (10, 8, 6),
    ]
    for perm in permutations:
        assert right_angle_triangle(*perm) is True


def test_right_angle_triangle_precision():
    """
    Check that the implementation correctly handles floating‑point rounding
    by using values that are mathematically exact but may suffer from binary
    representation errors.
    """
    a, b = 0.1 + 0.2, 0.3  # both evaluate to 0.30000000000000004 in binary
    c = math.sqrt(a ** 2 + b ** 2)
    # The sides are effectively (0.300..., 0.3, ~0.424264...), which is a right triangle.
    assert right_angle_triangle(a, b, c) is True