
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

```python
import pytest

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        a, b = b, a

    even_numbers = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

class TestGenerateIntegers:

    def test_empty_range(self):
        assert generate_integers(10, 14) == []

    def test_single_number(self):
        assert generate_integers(2, 2) == [2]
        assert generate_integers(8, 8) == [8]
        assert generate_integers(1, 1) == [1]

    def test_basic_range(self):
        assert generate_integers(2, 8) == [2, 4, 6, 8]
        assert generate_integers(8, 2) == [2, 4, 6, 8]
        assert generate_integers(1, 5) == [2, 4]
        assert generate_integers(5, 1) == [2, 4]

    def test_large_range(self):
        assert generate_integers(1, 100) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
        assert generate_integers(100, 1) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]

    def test_range_with_no_even_numbers(self):
        assert generate_integers(1, 3) == []
        assert generate_integers(1, 3) == []
        assert generate_integers(1, 3) == []
        assert generate_integers(1, 3) == []
        assert generate_integers(1, 3) == []
        assert generate_integers(1, 3) == []



    def test_edge_cases(self):
      assert generate_integers(2, 4) == [2, 4]
      assert generate_integers(4, 2) == [2, 4]
      assert generate_integers(1, 3) == []
      assert generate_integers(3, 1) == []
      assert generate_integers(2, 2) == [2]
      assert generate_integers(2, 1) == []
      assert generate_integers(8, 2) == [2, 4, 6, 8]
      assert generate_integers(10, 14) == []
      assert generate_integers(14, 10) == []
      assert generate_integers(1, 2) == [2]
      assert generate_integers(2, 1) == []

    def test_zero_values(self):
        assert generate_integers(0, 2) == [0, 2]
        assert generate_integers(2, 0) == [2]
        assert generate_integers(0, 0) == [0]

def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        a, b = b, a

    even_numbers = []
    for i in range(a, b + 1):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

@pytest.mark.parametrize("a, b, expected", [
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (10, 14, []),
    (1, 1, []),
    (2, 2, []),
    (1, 2, [2]),
    (2, 1, [2]),
    (100, 102, [100, 102]),
    (102, 100, [100, 102]),
    (1000, 1002, [1000, 1002]),
    (1002, 1000, [1000, 1002]),
    (20, 25, [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198]),
    (1000000, 1000001, [1000000, 1000002]),
    (1000001, 100