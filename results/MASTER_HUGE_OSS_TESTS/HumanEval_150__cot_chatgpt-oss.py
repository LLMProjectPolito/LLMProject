import pytest

# Assume x_or_y is imported from the module under test
# from mymodule import x_or_y


@pytest.mark.parametrize(
    "n, x, y, expected",
    [
        (2, "prime", "not prime", "prime"),          # smallest prime
        (3, 10, 20, 10),
        (5, [1, 2], {"a": 1}, [1, 2]),               # mutable x
        (7, None, "fallback", None),
        (13, 0, 1, 0),
        (104729, "big prime", "big composite", "big prime"),  # large prime
    ],
)
def test_returns_x_when_n_is_prime(n, x, y, expected):
    """x_or_y should return x for prime n."""
    assert x_or_y(n, x, y) == expected
    # For mutable objects, also check identity
    if isinstance(x, (list, dict, set)):
        assert x_or_y(n, x, y) is x


@pytest.mark.parametrize(
    "n, x, y, expected",
    [
        (1, "prime", "not prime", "not prime"),      # 1 is not prime
        (0, "prime", "not prime", "not prime"),
        (-3, "prime", "not prime", "not prime"),     # negative numbers not prime
        (4, 10, 20, 20),                              # small composite
        (6, "x", "y", "y"),
        (9, [1], {"b": 2}, {"b": 2}),                # mutable y
        (15, 0, 1, 1),
        (104730, "big prime", "big composite", "big composite"),  # large composite
    ],
)
def test_returns_y_when_n_is_not_prime(n, x, y, expected):
    """x_or_y should return y for non‑prime n."""
    assert x_or_y(n, x, y) == expected
    # For mutable objects, also check identity
    if isinstance(y, (list, dict, set)):
        assert x_or_y(n, x, y) is y


def test_x_and_y_are_unchanged():
    """Ensure that x_or_y does not modify the provided arguments."""
    mutable_x = [1, 2, 3]
    mutable_y = {"key": "value"}
    # Prime n -> should return x unchanged
    result = x_or_y(11, mutable_x, mutable_y)
    assert result is mutable_x
    assert mutable_x == [1, 2, 3]
    assert mutable_y == {"key": "value"}

    # Non‑prime n -> should return y unchanged
    result = x_or_y(12, mutable_x, mutable_y)
    assert result is mutable_y
    assert mutable_x == [1, 2, 3]
    assert mutable_y == {"key": "value"}


def test_invalid_n_type():
    """If n is not an integer, the function should raise a TypeError."""
    with pytest.raises(TypeError):
        x_or_y(3.14, "x", "y")
    with pytest.raises(TypeError):
        x_or_y("7", "x", "y")