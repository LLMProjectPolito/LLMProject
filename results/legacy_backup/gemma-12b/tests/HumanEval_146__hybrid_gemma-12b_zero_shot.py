import pytest
from your_module import specialFilter  # Replace your_module

def is_odd_digit(digit):
    return digit in '13579'

def check_first_and_last_digit(num):
    """Checks if the first and last digits of a number are odd."""
    num_str = str(abs(num))  # Handle negative numbers
    if not num_str:
        return False
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])
    return is_odd_digit(first_digit) and is_odd_digit(last_digit)

@pytest.fixture
def sample_data():
    """Provides sample data for testing."""
    return [
        ([15, -73, 14, -15], 1),
        ([33, -2, -3, 45, 21, 109], 2),
        ([11, 33, 55, 77, 99], 5),
        ([12, 23, 34, 45, 56, 67, 78, 89, 90], 0),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0),
        ([111, 222, 333, 444, 555, 666, 777, 888, 999], 9),
        ([101, 202, 303, 404, 505, 606, 707, 808, 909], 9),
        ([11, 13, 15, 17, 19, 21, 23, 25, 27, 29], 5),
        ([31, 33, 35, 37, 39, 41, 43, 45, 47, 49], 5),
        ([51, 53, 55, 57, 59, 61, 63, 65, 67, 69], 5),
        ([71, 73, 75, 77, 79, 81, 83, 85, 87, 89], 5),
        ([91, 93, 95, 97, 99, 101, 103, 105, 107, 109], 5),
        ([], 0),
        ([10, 20, 30, 40, 50], 0),
        ([11, 12, 13, 14, 15], 2),
        ([101, 102, 103, 104, 105], 2),
        ([-11, -13, -15, -17, -19], 0), #Negative numbers should not be counted
        ([15, 15, 15, 15, 15], 5),
        ([15, 15, 15, 15, 16], 4),
        ([15, 16, 17, 18, 19], 2)
    ]

def test_specialFilter_valid_input(sample_data):
    """Tests specialFilter with valid input arrays."""
    input_array, expected_output = sample_data
    assert specialFilter(input_array) == expected_output

def test_specialFilter_empty_array(sample_data):
    """Tests specialFilter with an empty array."""
    input_array, expected_output = sample_data
    assert specialFilter([]) == 0

def test_specialFilter_no_matching_numbers(sample_data):
    """Tests specialFilter when no numbers meet the criteria."""
    input_array, expected_output = sample_data
    assert specialFilter([10, 20, 30]) == 0

def test_specialFilter_all_matching_numbers(sample_data):
    """Tests specialFilter when all numbers meet the criteria."""
    input_array, expected_output = sample_data
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_specialFilter_negative_numbers(sample_data):
    """Tests specialFilter with negative numbers."""
    input_array, expected_output = sample_data
    assert specialFilter([-11, -13, -15, -17, -19]) == 0

def test_specialFilter_mixed_positive_and_negative(sample_data):
    """Tests specialFilter with a mix of positive and negative numbers."""
    input_array, expected_output = sample_data
    assert specialFilter([15, -73, 14, -15]) == 1

def test_specialFilter_large_numbers(sample_data):
    """Tests specialFilter with large numbers."""
    input_array, expected_output = sample_data
    assert specialFilter([12345, 67890, 13579]) == 1

def test_specialFilter_single_digit_numbers(sample_data):
    """Tests specialFilter with single digit numbers."""
    input_array, expected_output = sample_data
    assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5

@pytest.fixture
def sample_data2():
    """Provides sample data for testing."""
    return [
        [15, -73, 14, -15],
        [33, -2, -3, 45, 21, 109],
        [11, 22, 33, 44, 55, 66, 77, 88, 99],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [111, 222, 333, 444, 555, 666, 777, 888, 999],
        [],
        [10, 11, 12, 13, 14, 15],
        [101, 102, 103, 104, 105],
        [11, 12, 13, 14, 15, 16, 17, 18, 19],
        [1111, 1112, 1113, 1114, 1115],
        [15, 25, 35, 45, 55, 65, 75, 85, 95],
        [15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],
        [15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 101, 103, 105, 107, 109],
        [15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119]
    ]

def is_odd_digit2(digit):
    """Helper function to check if a digit is odd."""
    return int(digit) % 2 != 0

def first_and_last_digits_odd2(num):
    """Helper function to check if the first and last digits of a number are odd."""
    num_str = str(abs(num))  # Handle negative numbers
    return is_odd_digit2(num_str[0]) and is_odd_digit2(num_str[-1])

def test_special_filter_empty_list2(sample_data2):
    assert specialFilter([]) == 0

def test_special_filter_no_matches2(sample_data2):
    assert specialFilter([2, 4, 6, 8, 10]) == 0

def test_special_filter_single_match2(sample_data2):
    assert specialFilter([15, -73, 14, -15]) == 1

def test_special_filter_multiple_matches2(sample_data2):
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_special_filter_all_matches2(sample_data2):
    assert specialFilter([11, 33, 55, 77, 99]) == 5

def test_special_filter_mixed_list2(sample_data2):
    assert specialFilter([11, 22, 33, 44, 55, 66, 77, 88, 99, 10]) == 5

def test_special_filter_negative_numbers2(sample_data2):
    assert specialFilter([-15, -73, -11, -33]) == 2

def test_special_filter_large_numbers2(sample_data2):
    assert specialFilter([151, 353, 555, 757, 959]) == 5

def test_special_filter_numbers_close_to_102(sample_data2):
    assert specialFilter([9, 11, 12, 13, 14, 15]) == 2

def test_special_filter_numbers_starting_with_zero2(sample_data2):
    assert specialFilter([015, 033, 055]) == 0  # Leading zeros are not considered

def test_special_filter_numbers_with_leading_zeros2(sample_data2):
    assert specialFilter([15, 015]) == 1

def test_special_filter_complex_scenario2(sample_data2):
    data = [15, -73, 14, -15, 33, -2, -3, 45, 21, 109, 111, 222, 333, 444, 555, 666, 777, 888, 999]
    assert specialFilter(data) == 10

def test_special_filter_with_duplicates2(sample_data2):
    data = [15, 15, 15, -73, -73]
    assert specialFilter(data) == 2

def test_special_filter_with_large_input2(sample_data2):
    data = [i for i in range(1, 1001)]
    count = 0
    for num in data:
        if num > 10 and first_and_last_digits_odd2(num):
            count += 1
    assert specialFilter(data) == count