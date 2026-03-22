import pytest

# The function under test is assumed to be importable from the module where it is defined.
# Replace `my_module` with the actual module name if different.
from my_module import even_odd_count


@pytest.mark.parametrize(
    "num, expected",
    [
        # Basic positive numbers
        (0, (1, 0)),          # 0 is even
        (1, (0, 1)),          # single odd digit
        (2, (1, 0)),          # single even digit
        (5, (0, 1)),
        (8, (1, 0)),
        (12, (1, 1)),         # 1 odd, 2 even
        (123, (1, 2)),        # example from docstring
        (2468, (4, 0)),       # all even
        (13579, (0, 5)),      # all odd
        (1010, (2, 2)),       # mix with zeros
        (1001, (2, 2)),       # zeros counted as even
        (999999, (0, 6)),     # many odds
        (888888, (6, 0)),     # many evens
        (1234567890, (5, 5)), # balanced large number
        # Negative numbers – sign should be ignored
        (-1, (0, 1)),
        (-12, (1, 1)),        # example from docstring
        (-246, (3, 0)),
        (-135, (0, 3)),
        (-1010, (2, 2)),
        # Very large integer (more than typical 32‑bit range)
        (10**20 + 12345, (6, 5)),  # 100000000000000000000 + 12345 = 100000000000000012345
    ],
)
def test_even_odd_count_correctness(num, expected):
    """Check that even_odd_count returns the correct (even, odd) tuple."""
    result = even_odd_count(num)
    assert isinstance(result, tuple), "Result must be a tuple"
    assert len(result) == 2, "Result tuple must have exactly two elements"
    assert result == expected, f"For {num!r} expected {expected} but got {result}"


def test_return_type_elements_are_int():
    """All elements of the returned tuple should be integers."""
    for n in [0, 7, -42, 123456]:
        ev, od = even_odd_count(n)
        assert isinstance(ev, int) and isinstance(od, int)


@pytest.mark.parametrize("bad_input", [
    None,
    3.14,
    "123",
    [1, 2, 3],
    (4, 5),
    {6: "six"},
])
def test_invalid_input_type_raises(bad_input):
    """
    The function is documented only for integers.
    Supplying any other type should raise a TypeError.
    """
    with pytest.raises(TypeError):
        even_odd_count(bad_input)


def test_zero_is_counted_as_even():
    """Zero is an even digit and should be counted accordingly."""
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(1000) == (4, 0)  # three zeros + one '1' (odd)


def test_no_mutation_of_input():
    """
    Ensure that the function does not modify the input value.
    (Integers are immutable, but this guards against accidental conversion to mutable types.)
    """
    original = -987654321
    copy = original
    even_odd_count(original)
    assert original == copy, "The input integer should remain unchanged after the call"


def test_consistency_multiple_calls():
    """Calling the function repeatedly with the same argument should always give the same result."""
    num = 123456789
    first = even_odd_count(num)
    for _ in range(5):
        assert even_odd_count(num) == first