import pytest

# The function `double_the_difference` is assumed to be imported from the target module.
# from your_module import double_the_difference


@pytest.mark.parametrize(
    "input_list, expected",
    [
        # Basic examples from the docstring
        ([1, 3, 2, 0], 10),          # 1^2 + 3^2 + 0^2 = 10 (2 is even, ignored)
        ([-1, -2, 0], 0),            # all negatives ignored, 0 contributes 0
        ([9, -2], 81),               # 9 is odd, -2 ignored
        ([0], 0),                    # only zero
        # Edge cases
        ([], 0),                     # empty list
        ([2, 4, 6, 8], 0),           # only even positives → 0
        ([1, 5, 7, 9], 1+25+49+81),  # all odd positives
        ([1.0, 3, 5.5, -3, 7], 9+49),# floats ignored, -3 ignored, 3 and 7 counted
        (["1", 3, None, 5], 9+25),   # non‑int types ignored
        ([True, False, 2, 3], 1+9),  # bool is subclass of int: True→1 (odd), False→0 (even)
        ([-10, -9, -8, -7], 0),      # all negatives ignored
        ([10**6, 10**6+1], (10**6+1)**2),  # large odd number
    ],
)
def test_double_the_difference_various_inputs(input_list, expected):
    """Validate correct sum of squares for a variety of inputs."""
    assert double_the_difference(input_list) == expected


def test_ignores_non_integer_types():
    """Ensure that floats, strings, None, and other non‑int types are ignored."""
    mixed = [1, 2.5, "3", None, 5, -7, 8.0, [9], {10: "ten"}]
    # Only 1 and 5 are non‑negative odd integers
    assert double_the_difference(mixed) == 1**2 + 5**2


def test_boolean_handling():
    """Check that booleans are treated as integers (True → 1, False → 0)."""
    # True is odd (1), False is even (0)
    assert double_the_difference([True, False]) == 1**2  # only True contributes


def test_large_input_performance():
    """A large list should still produce the correct result without overflow."""
    large_list = list(range(0, 1000))  # 0‑999
    # Sum of squares of odd numbers from 1 to 999
    expected = sum(i * i for i in large_list if i % 2 == 1)
    assert double_the_difference(large_list) == expected