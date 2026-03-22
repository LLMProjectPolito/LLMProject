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
def multiple_elements_data():
    return [10, 1, 11, 2, 21]

@pytest.fixture
def negative_and_positive_data():
    return [-5, 5, -10, 10, -15, 15]

def test_order_by_points_sample_data(sample_data):
    expected = [-1, -11, 1, -12, 11]
    assert order_by_points(sample_data) == expected

def test_order_by_points_empty_data(empty_data):
    assert order_by_points(empty_data) == []

def test_order_by_points_single_element_data(single_element_data):
    assert order_by_points(single_element_data) == single_element_data

def test_order_by_points_multiple_elements_data(multiple_elements_data):
    expected = [1, 10, 11, 2, 21]
    assert order_by_points(multiple_elements_data) == expected

def test_order_by_points_negative_and_positive_data(negative_and_positive_data):
    expected = [-5, 5, -10, 10, -15, 15]
    assert order_by_points(negative_and_positive_data) == expected

def test_order_by_points_with_zeros(data_with_zeros):
    data_with_zeros = [10, 0, 1, -10, -1]
    expected = [-10, -1, 0, 1, 10]
    assert order_by_points(data_with_zeros) == expected

def test_order_by_points_all_negative(all_negative):
    all_negative = [-1, -2, -3, -4, -5]
    expected = [-1, -2, -3, -4, -5]
    assert order_by_points(all_negative) == expected

def test_order_by_points_all_positive(all_positive):
    all_positive = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert order_by_points(all_positive) == expected

def test_order_by_points_duplicate_sums(duplicate_sums):
    duplicate_sums = [12, 21, 30, 1, 2]
    expected = [1, 2, 12, 21, 30]
    assert order_by_points(duplicate_sums) == expected

def test_order_by_points_large_numbers(large_numbers):
    large_numbers = [1234, 4321, 1000, 2000]
    expected = [1000, 1234, 2000, 4321]
    assert order_by_points(large_numbers) == expected