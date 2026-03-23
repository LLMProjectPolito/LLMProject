import pytest
import math


# Focus: Order of Inputs
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
        if i % 2 == 0:
            result.append(i)
    return result

def test_order_inputs_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_order_inputs_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_order_inputs_no_evens():
    assert generate_integers(10, 14) == []

# Focus: Even Number Generation
import pytest

def test_generate_integers_ascending():
    assert generate_integers(2, 8) == [2, 4, 6, 8]

def test_generate_integers_descending():
    assert generate_integers(8, 2) == [2, 4, 6, 8]

def test_generate_integers_no_even():
    assert generate_integers(10, 14) == []

# Focus: Empty List Condition
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
        if i % 2 == 0:
            result.append(i)
    return result

def test_empty_list_condition_1():
    assert generate_integers(10, 11) == []

def test_empty_list_condition_2():
    assert generate_integers(11, 13) == []

def test_empty_list_condition_3():
    assert generate_integers(15, 17) == []