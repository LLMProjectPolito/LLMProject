import pytest

# Assume the function is imported from the module where it is defined.
# from mymodule import even_odd_count


@pytest.mark.parametrize(
    "num, expected",
    [
        # Basic examples from the docstring
        (-12, (1, 1)),
        (123, (1, 2)),
        # Single‑digit numbers
        (0, (1, 0)),   # 0 is even
        (1, (0, 1)),
        (2, (1, 0)),
        (9, (0, 1)),
        # All even digits
        (24680, (5, 0)),
        (-86420, (5, 0)),
        # All odd digits
        (13579, (0, 5)),
        (-97531, (0, 5)),
        # Mixed digits, including repeated ones
        (112233, (3, 3)),
        (-112233, (3, 3)),
        # Large integer (Python supports arbitrary precision)
        (12345678901234567890, (10, 10)),
        (-12345678901234567890, (10, 10)),
        # Number with trailing zeros (e.g., 1000 -> three zeros)
        (1000, (4, 0)),
        (-1000, (4, 0)),
        # Negative zero (should behave like zero)
        (-0, (1, 0)),
    ],
)
def test_even_odd_count(num, expected):
    """Validate that even_odd_count returns correct (even, odd) counts."""
    result = even_odd_count(num)
    assert isinstance(result, tuple), "Result should be a tuple"
    assert len(result) == 2, "Tuple should contain exactly two elements"
    assert result == expected, f"Expected {expected} for input {num}, got {result}"


def test_even_odd_count_type_error():
    """If the implementation validates input types, it should raise TypeError for non‑int."""
    for bad_input in ["123", 12.34, None, [1, 2, 3], (4, 5)]:
        with pytest.raises(TypeError):
            even_odd_count(bad_input)