
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """

```python
import pytest

def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.
    """
    try:
        num1, den1 = map(int, x.split('/'))
        num2, den2 = map(int, n.split('/'))
        result = num1 * num2 / den1 / den2
        return result == int(result)
    except ValueError:
        return False

# Suite 1: Original Suite
@pytest.mark.parametrize("x, n, expected", [
    ("1/5", "5/1", True),
    ("1/6", "2/1", False),
    ("7/10", "10/2", False),
    ("1/2", "2/1", True),
    ("2/3", "3/1", True),
    ("4/5", "5/4", True),
    ("1/1", "1/1", True),
    ("1/1", "2/1", False),
    ("2/1", "1/1", True),
    ("5/7", "7/5", True),
    ("1/3", "3/1", True),
    ("2/5", "5/2", True),
    ("1/4", "4/1", True),
    ("1/2", "1/2", True),
    ("3/4", "4/3", True),
    ("1/2", "2/2", False),
    ("1/3", "3/3", False),
    ("1/5", "5/5", False),
    ("2/3", "3/3", False),
    ("1/1", "1/1", True),
    ("1/1", "2/1", False),
    ("2/1", "1/1", True),
    ("1/2", "2/1", True),
    ("2/5", "5/1", True),
    ("3/7", "7/3", True),
    ("5/12", "12/5", True),
    ("1/10", "10/1", True),
    ("1/10", "1/10", True),
    ("1/2", "1/2", True),
    ("1/3", "1/3", True),
    ("1/4", "1/4", True),
    ("1/5", "1/5", True),
    ("1/6", "1/6", True),
    ("1/7", "1/7", True),
    ("1/8", "1/8", True),
    ("1/9", "1/9", True),
    ("1/10", "1/10", True),
    ("1/11", "1/11", True),
    ("1/12", "1/12", True),
    ("1/13", "1/13", True),
    ("1/14", "1/14", True),
    ("1/15", "1/15", True),
    ("1/16", "1/16", True),
    ("1/17", "1/17", True),
    ("1/18", "1/18", True),
    ("1/19", "1/19", True),
    ("1/20", "1/20", True),
    ("1/21", "1/21", True),
    ("1/22", "1/22", True),
    ("1/23", "1/23", True),
    ("1/24", "1/24", True),
    ("1/25", "1/25", True),
    ("1/26", "1/26", True),
    ("1/27", "1/27", True),
    ("1/28", "1/28", True),
    ("1/29", "1/29", True),
    ("1/30", "1/30", True),
    ("1/31", "1/31", True),
    ("1/32", "1/32", True),
    ("1/33", "1/33", True),
    ("1/34", "1/34", True),
    ("1/35", "1/35", True),
    ("1/36", "1/36", True),
    ("1/37", "1/37", True),
    ("1/38", "1/38", True),
    ("1/39", "1/39", True),
    ("1/40", "1/40", True),
    ("1/41", "1/41", True),
    ("1/42", "1/42", True),
    ("1/43", "1/43", True),
    ("1/44", "1/44", True),
    ("1/45", "1/45", True),
    ("1/46", "1/46", True),
    ("1/47", "1/47", True),
    ("1/48", "1/48", True),
    ("1/49", "1/49", True),
    ("1/50", "1/50", True),
    ("1/51", "1/51", True),
    ("1/52", "1/52", True),
    ("1/53", "1/53", True),
    ("1/54", "1/54", True),
    ("1/55", "1/55", True),
    ("1/56", "1/56", True),
    ("1/57", "1/57", True),
    ("1/58", "1/58", True),
    ("1/59", "1/59", True),
    ("1/60", "1/60", True),
    ("1/61", "1/61", True),
    ("1/62", "1/62", True),
    ("1/63", "1/63", True),
    ("1/64", "1/64", True),
    ("1/65", "1/65", True),
    ("1/66", "1/66", True),
    ("1/67", "1/67", True),
    ("1/68", "1/68", True),
    ("1/69", "1/69", True),
    ("1/70", "1/70", True),
    ("1/71", "1/71", True),
    ("1/72", "1/72", True),
    ("1/73", "1/73", True),
    ("1/74", "1/74", True),
    ("1/75", "1/75", True),
    ("1/76", "1/76", True),
    ("1/77", "1/77", True),
    ("1/78", "1/78", True),
    ("1/79", "1/79", True),
    ("1/80", "1/80", True),
    ("1/81", "1/81", True),
    ("1/82", "1/82", True),
    ("1/83", "1/83", True),
    ("1/84", "1/84", True),
    ("1/85", "1/85", True),
    ("1/86", "1/86", True),
    ("1/87", "1/87", True),
    ("1/88", "1/88", True),
    ("1/89", "1/89", True),
    ("1/90", "1/90", True),
])
def test_positive_fractions():
    assert simplify("1/5", "5/1") == True
    assert simplify("