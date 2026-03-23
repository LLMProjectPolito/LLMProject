import pytest

# Adjust the import below to match the location of your implementation.
# If the function is defined in the same file that pytest discovers,
# you can simply use: `from solution import simplify`
from solution import simplify


@pytest.mark.parametrize(
    "x, n, expected",
    [
        # --------------------------------------------------------------------
        # Simple true cases – product is a whole number
        # --------------------------------------------------------------------
        ("1/5", "5/1", True),          # 1/5 * 5 = 1
        ("2/3", "3/2", True),          # 2/3 * 3/2 = 1
        ("4/6", "3/2", True),          # (2/3) * (3/2) = 1
        ("6/8", "4/3", True),          # 6/8 * 4/3 = 24/24 = 1
        ("9/4", "4/9", True),          # 9/4 * 4/9 = 1
        ("2/7", "7/2", True),          # 2/7 * 7/2 = 1
        ("5/1", "3/1", True),          # 5 * 3 = 15
        ("1/2", "2/1", True),          # 1/2 * 2 = 1
        ("13/17", "17/13", True),      # product = 1
        ("123456789/1", "1/123456789", True),   # product = 1
        ("123456789/100000000", "100000000/123456789", True),  # product = 1
        ("1000000/3", "3/1000000", True),        # product = 1
        # --------------------------------------------------------------------
        # Simple false cases – product is NOT a whole number
        # --------------------------------------------------------------------
        ("1/6", "2/1", False),         # 1/6 * 2 = 1/3
        ("7/10", "10/2", False),       # 7/10 * 5 = 35/10 = 3.5
        ("2/5", "3/4", False),         # 6/20 = 3/10
        ("5/8", "3/2", False),         # 15/16
        ("3/7", "2/5", False),         # 6/35
        ("11/13", "5/7", False),       # 55/91
        ("123/456", "789/1011", False),# non‑integer product
    ],
)
def test_simplify_correctness(x, n, expected):
    """Check that `simplify` returns the expected boolean for a variety of inputs."""
    result = simplify(x, n)
    assert isinstance(result, bool), "Result should be a bool"
    assert result is expected, f"simplify({x!r}, {n!r}) should be {expected}"


def test_commutativity():
    """Multiplication of fractions is commutative – the function should reflect that."""
    pairs = [
        ("3/4", "8/9"),
        ("5/2", "7/3"),
        ("13/5", "25/13"),
        ("123456/789", "789/123456"),
    ]
    for a, b in pairs:
        assert simplify(a, b) == simplify(b, a), f"commutativity failed for {a}, {b}"


def test_idempotent_integer_inputs():
    """When both arguments are already whole numbers (denominator == 1) the result must be True."""
    for a in ["1/1", "2/1", "15/1", "100/1"]:
        for b in ["3/1", "7/1", "20/1"]:
            assert simplify(a, b) is True, f"Expected True for {a} * {b}"


def test_large_numbers_no_overflow():
    """Very large numerators/denominators should not cause errors and must give the correct boolean."""
    x = "987654321987654321/123456789123456789"
    n = "123456789123456789/987654321987654321"
    # The product simplifies to 1, therefore True
    assert simplify(x, n) is True