import pytest

@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3, 2, 3, 4, 2], [1, 2, 3, 3, 3, 4, 4]),
    ([5, 4, 3, 2, 1], [5, 5, 5, 5, 5]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
    ([], []),
    ([5], [5]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([10], [10]),
    ([-1, -2, -3], [-1, -1, -1]),
    ([0, 0, 0], [0, 0, 0]),
])
def test_rolling_max(numbers, expected):
    assert rolling_max(numbers) == expected

def test_rolling_max_empty_list():
    assert rolling_max([]) == []

def test_rolling_max_single_element_list():
    assert rolling_max([10]) == [10]

def test_rolling_max_large_list():
    large_list = list(range(1000))
    expected = list(range(1000))
    assert rolling_max(large_list) == expected

def test_rolling_max_negative_numbers():
    numbers = [-1, -2, -3, -4, -5]
    expected = [-1, -1, -1, -1, -1]
    assert rolling_max(numbers) == expected

def test_rolling_max_large_numbers():
    numbers = [1000, 2000, 3000, 4000, 5000]
    expected = [1000, 2000, 3000, 4000, 5000]
    assert rolling_max(numbers) == expected

def test_rolling_max_zeros():
    assert rolling_max([0, 0, 0]) == [0, 0, 0]