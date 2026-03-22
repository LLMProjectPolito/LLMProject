import pytest

# Assume the function `eat` is imported from the module under test
# from mymodule import eat


@pytest.mark.parametrize(
    "number, need, remaining, expected",
    [
        # Provided examples
        (5, 6, 10, [11, 4]),
        (4, 8, 9, [12, 1]),
        (1, 10, 10, [11, 0]),
        (2, 11, 5, [7, 0]),
        # Edge / boundary cases
        (5, 0, 10, [5, 10]),          # need = 0, nothing to eat
        (3, 5, 0, [3, 0]),            # no carrots left to eat
        (0, 5, 5, [5, 0]),            # start from zero, exact stock
        (0, 0, 0, [0, 0]),            # all zeros
        (1000, 0, 0, [1000, 0]),      # max number, no need, no stock
        (0, 1000, 1000, [1000, 0]),   # need equals stock, start from zero
        (500, 500, 500, [1000, 0]),   # need exactly matches remaining
        (10, 5, 100, [15, 95]),       # remaining > need
        (10, 200, 150, [160, 0]),     # need > remaining
        # Additional random boundary checks
        (0, 1, 0, [0, 0]),            # cannot eat any, still hungry
        (999, 1, 0, [999, 0]),        # no remaining carrots
        (0, 1000, 0, [0, 0]),         # huge need, no stock
    ],
)
def test_eat(number, need, remaining, expected):
    """
    Verify that `eat` returns the correct total eaten carrots and remaining stock
    for a variety of normal, edge, and boundary conditions.
    """
    result = eat(number, need, remaining)

    # The function should return a list (or sequence) of length 2
    assert isinstance(result, (list, tuple)), "Result should be a list or tuple"
    assert len(result) == 2, "Result must contain exactly two elements"

    # Compare the actual result with the expected list
    assert list(result) == expected, f"Failed for inputs ({number}, {need}, {remaining})"