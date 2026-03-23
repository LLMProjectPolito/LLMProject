import pytest
from your_module import order_by_points  # Replace your_module

def sum_digits(n):
    s = 0
    for digit in str(abs(n)):
        s += int(digit)
    return s

@pytest.fixture
def sample_data():
    return [1, 11, -1, -11, -12]

@pytest.fixture
def empty_data():
    return []

@pytest.fixture
def single_element_data():
    return [5]

@pytest.fixture
def multiple_elements_same_digit_sum():
    return [10, 1, 100]

def test_order_by_points_sample_data(sample_data):
    expected = [-1, -11, 1, -12, 11]
    assert order_by_points(sample_data) == expected

def test_order_by_points_empty_data(empty_data):
    assert order_by_points(empty_data) == []

def test_order_by_points_single_element_data(single_element_data):
    assert order_by_points(single_element_data) == single_element_data

def test_order_by_points_multiple_elements_same_digit_sum(multiple_elements_same_digit_sum):
    expected = [1, 10, 100]
    assert order_by_points(multiple_elements_same_digit_sum) == expected

def test_order_by_points_negative_numbers(sample_data):
    assert order_by_points(sample_data) == [-1, -11, 1, -12, 11]

def test_order_by_points_zero(sample_data):
    data = [0, 1, -1]
    assert order_by_points(data) == [0, -1, 1]

def test_order_by_points_large_numbers(sample_data):
    data = [123, 45, 6, -789]
    expected = [-789, 6, 45, 123]
    assert order_by_points(data) == expected

def test_order_by_points_mixed_positive_negative_zero():
    data = [1, -1, 0, 10, -10]
    expected = [0, -1, 1, -10, 10]
    assert order_by_points(data) == expected

def test_order_by_points_all_negative():
    data = [-1, -2, -3, -4, -5]
    expected = [-1, -2, -3, -4, -5]
    assert order_by_points(data) == expected