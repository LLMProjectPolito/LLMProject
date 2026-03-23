import pytest
from your_module import order_by_points  # Replace your_module

def sum_digits(n):
    """Helper function to calculate the sum of digits of an integer."""
    s = 0
    for digit in str(abs(n)):
        s += int(digit)
    return s

@pytest.fixture
def sample_data():
    """Fixture providing sample data for testing."""
    return [1, 11, -1, -11, -12]

@pytest.fixture
def empty_data():
    """Fixture providing empty data for testing."""
    return []

@pytest.fixture
def single_element_data():
    """Fixture providing single element data for testing."""
    return [5]

@pytest.fixture
def duplicate_sums_data():
    """Fixture providing data with duplicate sums for testing."""
    return [1, 10, 11, 2, 20]

@pytest.fixture
def negative_numbers_data():
    """Fixture providing data with negative numbers for testing."""
    return [-1, -10, -11, -2, -20]

@pytest.fixture
def mixed_positive_negative_data():
    """Fixture providing data with mixed positive and negative numbers."""
    return [1, -1, 10, -10, 11, -11]

def test_order_by_points_sample_data(sample_data):
    """Test with the sample data provided in the problem description."""
    expected = [-1, -11, 1, -12, 11]
    assert order_by_points(sample_data) == expected

def test_order_by_points_empty_data(empty_data):
    """Test with empty data."""
    assert order_by_points(empty_data) == []

def test_order_by_points_single_element_data(single_element_data):
    """Test with a single element."""
    assert order_by_points(single_element_data) == single_element_data

def test_order_by_points_duplicate_sums_data(duplicate_sums_data):
    """Test with data containing numbers with duplicate digit sums."""
    expected = [1, 2, 10, 11, 20]
    assert order_by_points(duplicate_sums_data) == expected

def test_order_by_points_negative_numbers_data(negative_numbers_data):
    """Test with only negative numbers."""
    expected = [-1, -2, -10, -11, -20]
    assert order_by_points(negative_numbers_data) == expected

def test_order_by_points_mixed_positive_negative_data(mixed_positive_negative_data):
    """Test with a mix of positive and negative numbers."""
    expected = [1, -1, 10, -10, 11, -11]
    assert order_by_points(mixed_positive_negative_data) == expected

def test_order_by_points_large_numbers():
    """Test with larger numbers to ensure digit sum calculation is correct."""
    data = [123, 45, 6, 789, 10]
    expected = [10, 6, 45, 123, 789]
    assert order_by_points(data) == expected

def test_order_by_points_zero():
    """Test with zero in the input list."""
    data = [0, 1, -1]
    expected = [-1, 0, 1]
    assert order_by_points(data) == expected

def test_order_by_points_all_zeros():
    """Test with a list containing only zeros."""
    data = [0, 0, 0]
    expected = [0, 0, 0]
    assert order_by_points(data) == expected

def test_order_by_points_identical_numbers():
    """Test with a list containing identical numbers."""
    data = [5, 5, 5]
    expected = [5, 5, 5]
    assert order_by_points(data) == expected

def test_order_by_points_all_same_digit_sum():
    """Test where all numbers have the same digit sum."""
    data = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert order_by_points(data) == expected

def test_order_by_points_with_duplicates():
    """Test with duplicate numbers in the input list."""
    data = [1, 1, 2, 2]
    expected = [1, 1, 2, 2]
    assert order_by_points(data) == expected