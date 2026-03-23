import pytest

# ----------------------------------------------------------------------
# Adjust the import below to match the location of `generate_integers`.
# For example, if the function lives in a file called `solution.py`,
# use:  from solution import generate_integers
# ----------------------------------------------------------------------
from your_module_name import generate_integers   # <-- replace `your_module_name`


@pytest.mark.parametrize(
    "a, b, expected",
    [
        # basic ascending range – contains several even digits
        (2, 8, [2, 4, 6, 8]),
        # same range but reversed – order must still be ascending
        (8, 2, [2, 4, 6, 8]),
        # range that does not contain any even digit (all numbers >= 10)
        (10, 14, []),
        # single‑element range that is an even digit
        (4, 4, [4]),
        # single‑element range that is an odd digit
        (5, 5, []),
        # range that starts below 0 (function spec says positive, but we test robustness)
        (-3, 3, [0, 2]),
        # range that spans the whole single‑digit space
        (0, 9, [0, 2, 4, 6, 8]),
        # large range – only the even digits should be returned once
        (1, 1000, [0, 2, 4, 6, 8]),
        # range where both bounds are even digits but out of order
        (8, 0, [0, 2, 4, 6, 8]),
        # range where bounds are the same odd digit > 9 (should be empty)
        (13, 13, []),
    ],
)
def test_generate_integers_various_cases(a, b, expected):
    """
    Verify that `generate_integers` returns the correct list of even digits
    for a variety of input configurations.
    """
    result = generate_integers(a, b)
    assert result == expected, f"Failed for a={a}, b={b}"


def test_return_type_and_mutability():
    """
    The function must return a list (not a generator or tuple) and must
    produce a new list on each call (i.e., callers can modify the result
    without affecting subsequent calls).
    """
    first = generate_integers(2, 8)
    second = generate_integers(2, 8)

    # Both calls should give equal content
    assert first == second == [2, 4, 6, 8]

    # They must be distinct objects
    assert first is not second

    # Mutating one result must not affect the other
    first.append(10)
    assert first != second
    assert second == [2, 4, 6, 8]


def test_invalid_input_types():
    """
    The specification mentions *positive integers*, but the implementation
    should raise a clear exception for non‑integer inputs.
    """
    with pytest.raises(TypeError):
        generate_integers("a", 5)

    with pytest.raises(TypeError):
        generate_integers(5, None)

    with pytest.raises(TypeError):
        generate_integers(3.14, 10)


def test_negative_and_zero_bounds():
    """
    Even though the contract says “positive integers”, many implementations
    gracefully handle zero and negative numbers. This test documents the
    expected behaviour for such inputs.
    """
    # Zero is an even digit, so it should appear when the interval includes it
    assert generate_integers(0, 0) == [0]
    assert generate_integers(-5, 1) == [0, 2]  # 2 is included because the interval is inclusive
    # When the interval is entirely negative, no even digit can appear
    assert generate_integers(-9, -1) == []


def test_large_random_ranges(monkeypatch):
    """
    Stress test with a large random range to ensure the function does not
    perform unnecessary work (e.g., iterating over every integer).  The
    expected result is always the static list of even digits.
    """
    import random

    # Pick two random numbers far apart
    a = random.randint(1, 10_000)
    b = random.randint(1, 10_000)

    # The correct answer is simply the even digits that lie between the
    # numeric bounds, regardless of how large the interval is.
    low, high = sorted((a, b))
    expected = [d for d in (0, 2, 4, 6, 8) if low <= d <= high]

    assert generate_integers(a, b) == expected