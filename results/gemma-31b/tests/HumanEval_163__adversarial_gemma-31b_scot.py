
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

import pytest

# The function is provided in the environment; we are testing it.
# from solution import generate_integers 

class TestGenerateIntegers:
    """
    Blue Team QA suite to detect bugs in generate_integers.
    Focuses on range boundaries, digit constraints, and input ordering.
    """

    @pytest.mark.parametrize("a, b, expected", [
        (2, 8, [2, 4, 6, 8]),    # Standard case
        (8, 2, [2, 4, 6, 8]),    # Reversed arguments
        (1, 9, [2, 4, 6, 8]),    # Full range of positive digits
        (10, 14, []),            # Entirely outside digit range
        (2, 12, [2, 4, 6, 8]),   # Partial overlap (starts in digits, ends above)
        (7, 15, [8]),            # Partial overlap (starts in digits, ends above)
        (1, 3, [2]),             # Small range with one even digit
        (1, 1, []),              # Single odd value
        (4, 4, [4]),             # Single even digit value
        (12, 12, []),            # Single value above digit range
        (3, 5, [4]),             # Middle of digit range
        (5, 7, [6]),             # Middle of digit range
        (9, 11, []),             # Range crossing the 9-10 boundary
    ])
    def test_functional_scenarios(self, a, b, expected):
        """Test various ranges to ensure correct digit filtering and ordering."""
        assert generate_integers(a, b) == expected

    def test_large_inputs(self):
        """Test with very large integers to ensure no performance hang or overflow."""
        # Range is far beyond single digits
        assert generate_integers(1000, 2000) == []
        # Range is huge but includes digits
        assert generate_integers(1, 10**6) == [2, 4, 6, 8]

    def test_ascending_order(self):
        """Explicitly verify that the output is always sorted ascending."""
        result = generate_integers(8, 2)
        assert result == sorted(result), "The output list must be in ascending order."

    def test_positive_integers_constraint(self):
        """
        Verify behavior with the smallest positive integers.
        If the function handles 0 as a digit, this test helps define that behavior.
        """
        # Since prompt says 'positive integers', we assume a, b >= 1.
        # If the range is (1, 2), only 2 is an even digit.
        assert generate_integers(1, 2) == [2]