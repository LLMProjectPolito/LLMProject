import pytest

# ----------------------------------------------------------------------
# NOTE:
# Adjust the import below to match the location of the `do_algebra` function.
# For example, if the function lives in a file called `algebra.py` in the
# same directory, use:
#     from algebra import do_algebra
# ----------------------------------------------------------------------
from solution import do_algebra  # <-- replace `solution` with the actual module name


# ----------------------------------------------------------------------
# Helper – a tiny wrapper that mimics the doc‑string examples.
# ----------------------------------------------------------------------
def evaluate_expression(operators, operands):
    """Convenient wrapper used only inside the test suite."""
    return do_algebra(operators, operands)


# ----------------------------------------------------------------------
# 1.  Basic functionality – one operator
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "operators, operands, expected",
    [
        (["+"], [1, 2], 3),
        (["-"], [10, 4], 6),
        (["*"], [7, 8], 56),
        (["//"], [9, 2], 4),          # floor division
        (["**"], [2, 5], 32),         # exponentiation
    ],
)
def test_single_operator(operators, operands, expected):
    assert evaluate_expression(operators, operands) == expected


# ----------------------------------------------------------------------
# 2.  Operator precedence – the core requirement
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "operators, operands, expected",
    [
        # addition vs multiplication
        (["+", "*"], [2, 3, 4], 2 + 3 * 4),          # 2 + (3*4) = 14
        # subtraction vs multiplication
        (["-", "*"], [10, 2, 3], 10 - 2 * 3),        # 10 - (2*3) = 4
        # multiplication vs floor division (same precedence, left‑to‑right)
        (["*", "//"], [7, 3, 2], (7 * 3) // 2),     # (7*3)//2 = 10
        # floor division vs multiplication (same precedence, left‑to‑right)
        (["//", "*"], [7, 3, 2], (7 // 3) * 2),     # (7//3)*2 = 4
        # exponentiation vs multiplication (exponentiation higher)
        (["**", "*"], [2, 3, 4], (2 ** 3) * 4),     # (2**3)*4 = 32
        # multiplication vs exponentiation (exponentiation higher)
        (["*", "**"], [2, 3, 2], 2 * (3 ** 2)),     # 2*(3**2) = 18
        # mixed chain – mirrors the example in the doc‑string
        (["+", "*", "-"], [2, 3, 4, 5], 2 + 3 * 4 - 5),  # 9
    ],
)
def test_operator_precedence(operators, operands, expected):
    assert evaluate_expression(operators, operands) == expected


# ----------------------------------------------------------------------
# 3.  Exponentiation associativity (right‑to‑left)
# ----------------------------------------------------------------------
def test_exponentiation_associativity():
    # 2 ** 3 ** 2  == 2 ** (3 ** 2) == 2 ** 9 == 512
    operators = ["**", "**"]
    operands = [2, 3, 2]
    assert evaluate_expression(operators, operands) == 512


# ----------------------------------------------------------------------
# 4.  Large numbers and zero handling
# ----------------------------------------------------------------------
def test_large_numbers_and_zero():
    operators = ["+", "*", "//", "**"]
    operands = [0, 123456789, 987654321, 2, 3]  # 0 + 123456789 * 987654321 // 2 ** 3
    # Compute expected using Python's own precedence rules
    expected = 0 + 123456789 * 987654321 // (2 ** 3)
    assert evaluate_expression(operators, operands) == expected


# ----------------------------------------------------------------------
# 5.  Division by zero should raise the same error as Python's // operator
# ----------------------------------------------------------------------
def test_floor_division_by_zero():
    operators = ["//"]
    operands = [5, 0]
    with pytest.raises(ZeroDivisionError):
        evaluate_expression(operators, operands)


# ----------------------------------------------------------------------
# 6.  Mismatched lengths – the function is expected to validate input
# ----------------------------------------------------------------------
@pytest.mark.parametrize(
    "operators, operands",
    [
        (["+", "-"], [1, 2]),          # 2 operators, 2 operands → invalid
        (["*"], [1]),                  # 1 operator, 1 operand → invalid
        ([], [1, 2]),                  # no operator (spec says at least one)
    ],
)
def test_invalid_lengths_raise_value_error(operators, operands):
    with pytest.raises(ValueError):
        evaluate_expression(operators, operands)


# ----------------------------------------------------------------------
# 7.  Unsupported operator – should raise a clear exception
# ----------------------------------------------------------------------
def test_unsupported_operator():
    operators = ["%"]          # modulo is not listed in the spec
    operands = [10, 3]
    with pytest.raises(RuntimeError):
        evaluate_expression(operators, operands)


# ----------------------------------------------------------------------
# 8.  Type safety – non‑integer operands should raise TypeError
# ----------------------------------------------------------------------
def test_non_integer_operand():
    operators = ["+"]
    operands = [1, "two"]
    with pytest.raises(TypeError):
        evaluate_expression(operators, operands)


# ----------------------------------------------------------------------
# 9.  Ensure the return type is always an int (even for floor division)
# ----------------------------------------------------------------------
def test_return_type_is_int():
    operators = ["//"]
    operands = [7, 2]
    result = evaluate_expression(operators, operands)
    assert isinstance(result, int)
    assert result == 3