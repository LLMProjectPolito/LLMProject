
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

```python
import pytest

def even_odd_count(n):
    assert n % 2 == 0
    assert n % 2 != 0

def test_even_odd_count_negative():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(2468) == (2, 2)
    assert even_odd_count(13579) == (2, 2)
    assert even_odd_count(1) == (1, 0)
    assert even_odd_count(0) == (0, 0)
    assert even_odd_count(10) == (0, 2)
    assert even_odd_count(11) == (0, 2)
    assert even_odd_count(12) == (0, 2)
    assert even_odd_count(1234) == (0, 2)
    assert even_odd_count(12345) == (0, 2)
    assert even_odd_count(123456) == (0, 2)
    assert even_odd_count(1234567) == (0, 2)
    assert even_odd_count(12345678) == (0, 2)
    assert even_odd_count(123456789) == (0, 2)
    assert even_odd_count(1234567890) == (0, 2)
    assert even_odd_count(12345678901) == (0, 2)
    assert even_odd_count(123456789012) == (0, 2)
    assert even_odd_count(1234567890123) == (0, 2)
    assert even_odd_count(12345678901234) == (0, 2)
    assert even_odd_count(123456789012345) == (0, 2)
    assert even_odd_count(1234567890123456) == (0, 2)
    assert even_odd_count(12345678901234567) == (0, 2)
    assert even_odd_count(123456789012345678) == (0, 2)
    assert even_odd_count(1234567890123456789) == (0, 2)
    assert even_odd_count(123456789012345678901) == (0, 2)
    assert even_odd_count(1234567890123456789012) == (0, 2)
    assert even_odd_count(123456789012345678901234) == (0, 2)
    assert even_odd_count(1234567890123456789012345) == (0, 2)
    assert even_odd_count(12345678901234567890123456) == (0, 2)
    assert even_odd_count(12345678901234567890123456789012345678901234567890123456) == (0, 2)
    assert even_odd_count(12345678901234567890123456789012345678901234567890123456) == (0, 2)
    assert even_odd_count(12345678901234567890123456789012345678901234567890123456) == (0, 2)
    assert even_odd_count(12345678901234567890123456789012345678901234567890123456) == (0, 2)
    assert even_odd_count(12345678901234567890123456789012345678901234567890123456) == (0, 2)
    assert even_odd_count(12345678901234567890123456789012345678901234567890123456) == (0, 2)
    assert even_odd_count(12345678901234567890123456789012345678901234567890123456) == (0, 2)
    assert even_odd_count(12345678901234567890123456789012345678901234567890123456) == (0, 2)
    assert even_odd_count(12345678901234567890123456789012345678901234567890123456) == (0, 2)
    assert even_odd_count(12345678901234567890123456789012345678901234567890123456) == (0, 2)
    assert even_odd_count(12345678901234567890123456789012345678901234567890123456) == (0, 2)
    assert even_odd_count(12345678901234567890123456789012345678901234567890123456) == (0, 2)
    assert even_odd_count(12345678901234567890123456789012345678901234567890123456) == (0, 2)
    assert even_odd_count(12345678901234567890123456789012345678901234567890123456) == (0, 2)
    assert even_odd_count(12345678901234567890123456789012345678901234567890123456) == (0, 2)
    assert even_odd_count(12345678901234567890123456789012345678901234567890123456) == (0, 2