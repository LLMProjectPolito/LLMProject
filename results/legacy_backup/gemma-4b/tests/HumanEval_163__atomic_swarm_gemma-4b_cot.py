import pytest
import math

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
        for digit in s:
            if int(digit) % 2 == 0:
                if int(digit) not in result:
                    result.append(int(digit))
    result.sort()
    return result

def test_basic():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

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
    if a <= b:
        for i in range(a, b + 1):
            s = str(i)
            for digit in s:
                if int(digit) % 2 == 0:
                    if int(digit) not in result:
                        result.append(int(digit))
        result.sort()
    else:
        for i in range(a, b - 1, -1):
            s = str(i)
            for digit in s:
                if int(digit) % 2 == 0:
                    if int(digit) not in result:
                        result.append(int(digit))
        result.sort()
    return result

def test_edge_empty_range():
    assert generate_integers(10, 10) == []

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
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        s = str(i)
        if all(int(digit) % 2 != 0 for digit in s):
            continue
        if all(int(digit) % 2 == 0 for digit in s):
            result.append(i)
    return result
    
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 8, [2, 4, 6, 8]),
        (8, 2, [2, 4, 6, 8]),
        (10, 14, []),
        (2, 2, []),
        (1, 1, []),
        (2, 3, []),
        (10, 12, []),
        (12, 14, []),
    ],
)
def test_generate_integers_edge_cases(a, b, expected):
    assert generate_integers(a, b) == expected