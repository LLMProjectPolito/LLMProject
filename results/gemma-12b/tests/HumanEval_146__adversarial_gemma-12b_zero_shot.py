import pytest
from your_module import specialFilter  # Replace your_module

def is_odd_digit(digit):
    return int(digit) % 2 != 0

def check_first_and_last_digit_odd(num):
    num_str = str(abs(num))
    if not num_str:
        return False
    first_digit = num_str[0]
    last_digit = num_str[-1]
    return is_odd_digit(first_digit) and is_odd_digit(last_digit)

@pytest.fixture
def sample_data():
    return [
        ([15, -73, 14, -15], 1),
        ([33, -2, -3, 45, 21, 109], 2),
        ([11, 33, 55, 77, 99], 5),
        ([12, 23, 34, 45, 56, 67, 78, 89, 90], 0),
        ([111, 333, 555, 777, 999], 5),
        ([1, 3, 5, 7, 9], 0),
        ([10, 11, 12, 13, 14, 15], 1),
        ([], 0),
        ([20, 21, 22, 23, 24, 25], 1),
        ([101, 103, 105, 107, 109], 0),
        ([1111, 3333, 5555, 7777, 9999], 5),
        ([-11, -33, -55, -77, -99], 5),
        ([15, 15, 15, 15, 15], 5),
        ([15, 15, 15, 15, 16], 4),
        ([15, 16, 17, 18, 19], 1),
        ([100, 101, 102, 103, 104, 105], 1),
        ([1000, 1001, 1002, 1003, 1004, 1005], 1),
        ([10000, 10001, 10002, 10003, 10004, 10005], 1),
        ([100000, 100001, 100002, 100003, 100004, 100005], 1),
        ([1000000, 1000001, 1000002, 1000003, 1000004, 1000005], 1)
    ]

def test_specialFilter_valid_input(sample_data):
    for nums, expected in sample_data:
        assert specialFilter(nums) == expected

def test_specialFilter_empty_list():
    assert specialFilter([]) == 0

def test_specialFilter_no_matching_numbers():
    assert specialFilter([2, 4, 6, 8, 10]) == 0

def test_specialFilter_negative_numbers():
    assert specialFilter([-11, -33, -55, -77, -99]) == 5

def test_specialFilter_mixed_positive_and_negative():
    assert specialFilter([-15, 15, -33, 33]) == 2

def test_specialFilter_large_numbers():
    assert specialFilter([15000, 33000, 55000, 77000, 99000]) == 5

def test_specialFilter_numbers_with_zeros():
    assert specialFilter([10, 30, 50, 70, 90]) == 0

def test_specialFilter_single_number():
    assert specialFilter([15]) == 1
    assert specialFilter([16]) == 0

def test_specialFilter_edge_case_1():
    assert specialFilter([11, 12, 13, 14, 15]) == 1

def test_specialFilter_edge_case_2():
    assert specialFilter([101, 102, 103, 104, 105]) == 1