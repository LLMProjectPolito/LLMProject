import pytest

# Assume simplify is imported from the module under test
# from mymodule import simplify

@pytest.mark.parametrize(
    "x, n, expected",
    [
        # Basic examples from the description
        ("1/5", "5/1", True),
        ("1/6", "2/1", False),
        ("7/10", "10/2", False),

        # Products that reduce exactly to an integer
        ("2/3", "3/2", True),          # 1
        ("4/1", "5/1", True),          # 20
        ("5/2", "2/5", True),          # 1
        ("3/7", "7/3", True),          # 1
        ("3/2", "4/3", True),          # 2
        ("123456789/1", "1/123456789", True),  # 1
        ("1/1000000", "1000000/1", True),      # 1

        # Products that do NOT reduce to an integer
        ("3/4", "2/3", False),         # 1/2
        ("123456789/1000000000", "2/1", False),  # 247913578/1000000000
        ("7/10", "3/2", False),        # 21/20
        ("9/8", "4/3", False),         # 3/2
    ],
)
def test_simplify_various_cases(x, n, expected):
    """Test simplify() across a range of typical, edge and large‑value cases."""
    assert simplify(x, n) is expected


def test_simplify_commutativity():
    """The product of two fractions should be independent of order."""
    cases = [
        ("2/5", "15/4"),
        ("7/3", "9/14"),
        ("123/456", "789/1011"),
    ]
    for a, b in cases:
        result1 = simplify(a, b)
        result2 = simplify(b, a)
        assert result1 == result2, f"commutativity failed for {a} * {b}"


def test_simplify_identity():
    """Multiplying by 1 (as a fraction) must always return the original truth value."""
    identity = "1/1"
    fractions = ["1/2", "3/4", "5/1", "123456/789012"]
    for frac in fractions:
        # product with 1 should be whole number iff the original fraction is whole
        expected = (int(frac.split('/')[0]) % int(frac.split('/')[1]) == 0)
        assert simplify(frac, identity) is expected
        assert simplify(identity, frac) is expected