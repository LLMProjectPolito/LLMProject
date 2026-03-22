import pytest
import math

@pytest.mark.parametrize(
    "num,expected",
    [
        (-102, (2, 1)),
        (-120, (2, 1)),
    ],
)
def test_even_odd_count(num, expected):
    """Test even_odd_count with negative numbers containing zero."""
    assert even_odd_count(num) == expected