import pytest
from your_module import special_factorial  # Replace your_module

@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 288),
        (5, 34560),
    ],
)
def test_positive_integers(n, expected):
    assert special_factorial(n) == expected


def test_zero():
    with pytest.raises(ValueError):
        special_factorial(0)


def test_negative_integer():
    with pytest.raises(ValueError):
        special_factorial(-1)


def test_none_input():
    with pytest.raises(TypeError):
        special_factorial(None)


def test_boolean_input():
    with pytest.raises(TypeError):
        special_factorial(True)
    with pytest.raises(TypeError):
        special_factorial(False)


def test_float_input():
    with pytest.raises(TypeError):
        special_factorial(2.5)

# Optional test for large integer overflow.  Remove if not applicable.
# def test_large_integer_overflow():
#     try:
#         result = special_factorial(10)  # Or a larger number
#         # Assert that the result is what you expect in case of overflow
#         # For example, if the function returns a string representation of the result:
#         # assert isinstance(result, str)
#         # assert "overflow" in result
#     except OverflowError:
#         pass  # Expected behavior
#     except Exception as e:
#         pytest.fail(f"Unexpected exception: {e}")