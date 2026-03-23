```python
import pytest
from typing import List

# The function under test is assumed to be imported from the target module.
# from your_module import order_by_points


def _digit_sum(n: int) -> int:
    """Helper that returns the sum of the absolute decimal digits of ``n``."""
    return sum(int(d) for d in str(abs(n)))


def _expected_order(nums: List[int]) -> List[int]:
    """
    Produce the expected ordering according to the specification:
    1. Ascending order of the sum of decimal digits (absolute value).
    2. For equal sums, preserve the original relative order (stable sort).
    """
    # Pair each number with its original index.
    indexed = list(enumerate(nums))
    # Sort by (digit sum, original index) – the original index ensures stability.
    indexed.sort(key=lambda pair: (_digit_sum(pair[1]), pair[0]))
    # Return the numbers in the new order.
    return [value for _, value in indexed]


@pytest.mark.parametrize(
    "input_list,expected",
    [
        ([], []),  # empty list
        ([0], [0]),  # single zero
        ([5], [5]),  # single positive
        ([-7], [-7]),  # single negative
        ([12, 3, 45, 6], [3, 6, 12, 45]),  # simple positive numbers
        ([-12, -3, -45, -6], [-3, -6, -12, -45]),  # simple negative numbers
        ([1, 11, -1, -11, -12], _expected_order([1, 11, -1, -11, -12])),
        ([101, 20, -20, 2, -101], _expected_order([101, 20, -20, 2, -101])),
        ([99, 9, -9, -99, 0], _expected_order([99, 9, -9, -99, 0])),
        ([123456789, -987654321, 111111111, -222222222],
         _expected_order([123456789, -987654321,