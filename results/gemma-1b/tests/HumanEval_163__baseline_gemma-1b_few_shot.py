
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
    result = []
    for i in range(a, b + 1):
        s = str(i)
        if s[0] % 2 == 0:
            result.append(i)
    return result

def test_generate_integers_positive():
    assert generate_integers(2, 8) == [2, 4, 6, 8]
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(10, 14) == []
    assert generate_integers(1, 5) == [2, 4]
    assert generate_integers(5, 1) == [2, 4]
    assert generate_integers(1, 1) == [2]
    assert generate_integers(1, 2) == [2]
    assert generate_integers(2, 2) == []
    assert generate_integers(2, 3) == [2]
    assert generate_integers(3, 3) == []
    assert generate_integers(3, 4) == [3]
    assert generate_integers(4, 4) == []
    assert generate_integers(4, 5) == [4]
    assert generate_integers(5, 5) == []
    assert generate_integers(5, 6) == [5]
    assert generate_integers(6, 6) == []
    assert generate_integers(6, 7) == [6]
    assert generate_integers(7, 7) == []
    assert generate_integers(7, 8) == [7]
    assert generate_integers(8, 8) == []
    assert generate_integers(8, 9) == [8]
    assert generate_integers(9, 9) == []
    assert generate_integers(9, 10) == [9]
    assert generate_integers(10, 10) == []
    assert generate_integers(10, 11) == [10]
    assert generate_integers(11, 11) == []
    assert generate_integers(11, 12) == [11]
    assert generate_integers(12, 12) == []
    assert generate_integers(12, 13) == [12]
    assert generate_integers(13, 13) == []
    assert generate_integers(13, 14) == [13]
    assert generate_integers(14, 14) == []
    assert generate_integers(14, 15) == [14]
    assert generate_integers(15, 15) == []
    assert generate_integers(15, 16) == [15]
    assert generate_integers(16, 16) == []
    assert generate_integers(16, 17) == [16]
    assert generate_integers(17, 17) == []
    assert generate_integers(17, 18) == [17]
    assert generate_integers(18, 18) == []
    assert generate_integers(18, 19) == [18]
    assert generate_integers(19, 19) == []
    assert generate_integers(19, 20) == [19]
    assert generate_integers(20, 20) == []
    assert generate_integers(20, 21) == [20]
    assert generate_integers(21, 21) == []
    assert generate_integers(21, 22) == [21]
    assert generate_integers(22, 22) == []
    assert generate_integers(22, 23) == [22]
    assert generate_integers(23, 23) == []
    assert generate_integers(23, 24) == [23]
    assert generate_integers(24, 24) == []
    assert generate_integers(24, 25) == [24]
    assert generate_integers(25, 25) == []
    assert generate_integers(25, 26) == [25]
    assert generate_integers(26, 26) == []
    assert generate_integers(26, 27) == [26]
    assert generate_integers(27, 27) == []
    assert generate_integers(27, 28) == [27]
    assert generate_integers(28, 28) == []
    assert generate_integers(28, 29) == [28]
    assert generate_integers(29, 29) == []
    assert generate_integers(29, 30) == [29]
    assert generate_integers(30, 30) == []
    assert generate_integers(30, 31) == [30]
    assert generate_integers(31, 31) == []
    assert generate_integers(31, 32) == [31]
    assert generate_integers(32, 32) == []
    assert generate_integers(32, 33) == [32]
    assert generate_integers(33, 33) == []
    assert generate_integers(33, 34) == [33]
    assert generate_integers(34, 34) == []
    assert generate_integers(34, 35) == [34]
    assert generate_integers(35, 35) == []
    assert generate_integers(35, 36) == [35]
    assert generate_integers(36, 36) == []
    assert generate_integers(36, 37) == [36]
    assert generate_integers(37, 37) == []
    assert generate_integers(37, 38) == [37]
    assert generate_integers(38, 38) == []
    assert generate_integers(38, 39) == [38]
    assert generate_integers(39, 39) == []
    assert generate_integers(39, 40) == [39]
    assert generate_integers(40, 40) == []
    assert generate_integers(40, 41) == [40]
    assert generate_integers(41, 41) == []
    assert generate_integers(41, 42) == [41]
    assert generate_integers(42, 42) == []
    assert generate_integers(42, 43) == [42]
    assert generate_integers(43, 43) == []
    assert generate_integers(43, 44) == [43]
    assert generate_integers(44, 44) == []
    assert generate_integers(44, 45) == [44]
    assert generate_integers(45, 45) == []
    assert generate_integers(45, 46) == [45]
    assert generate_integers(46, 46) == []
    assert generate_integers(46, 47) == [46]
    assert generate_integers(47, 47) == []
    assert generate_integers(47, 48) == [47]
    assert generate_integers(48, 48) == []
    assert generate_integers(48, 49) == [48]
    assert generate_integers(49, 49) == []
    assert generate_inte