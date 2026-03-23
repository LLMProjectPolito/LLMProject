import pytest
import math


# Focus: Boundary Values
import pytest

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    assert order_by_points([5]) == [5]

def test_order_by_points_negative_numbers():
    assert order_by_points([-1, -11, -12]) == [-1, -11, -12]

# Focus: Type Scenarios
import pytest

def test_empty_list():
    assert order_by_points([]) == []

def test_single_element_positive():
    assert order_by_points([5]) == [5]

def test_single_element_negative():
    assert order_by_points([-5]) == [-5]

# Focus: Logic Branches
import pytest

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_same_sum():
    assert order_by_points([1, 11, 12, 111]) == [1, 11, 111, 12]