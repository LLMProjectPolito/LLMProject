import pytest

def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10:
            num_str = str(abs(num))
            if len(num_str) > 0:
                first_digit = int(num_str[0])
                last_digit = int(num_str[-1])
                if first_digit % 2 != 0 and last_digit % 2 != 0:
                    count += 1
    return count

@pytest.fixture
def nums():
    return []

@pytest.fixture
def nums2():
    return [2, 4, 6, 8, 10]

@pytest.fixture
def nums3():
    return [15]

@pytest.fixture
def nums4():
    return [33, -2, -3, 45, 21, 109]

@pytest.fixture
def nums5():
    return [-73]

@pytest.fixture
def nums6():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

@pytest.fixture
def nums7():
    return [11, 12, 13, 14, 15]

@pytest.fixture
def nums8():
    return [15, -73, 14, -15]

@pytest.fixture
def nums9():
    return [12345]

def test_empty_list(nums):
    assert specialFilter(nums) == 0

def test_no_special_numbers(nums2):
    assert specialFilter(nums2) == 0

def test_single_special_number(nums3):
    assert specialFilter(nums3) == 1

def test_multiple_special_numbers(nums4):
    assert specialFilter(nums4) == 2

def test_negative_numbers(nums5):
    assert specialFilter(nums5) == 1

def test_numbers_less_than_or_equal_to_10(nums6):
    assert specialFilter(nums6) == 0

def test_single_digit_numbers(nums6):
    assert specialFilter(nums6) == 0

def test_mixed_numbers(nums7):
    assert specialFilter(nums7) == 1

def test_large_numbers(nums9):
    assert specialFilter(nums9) == 1

def test_mixed_numbers2(nums8):
    assert specialFilter(nums8) == 1