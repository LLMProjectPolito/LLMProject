import pytest

@pytest.mark.parametrize("numbers, delimeter, expected", [
    ([], 4, []),
    ([1], 4, [1]),
    ([1, 2, 3], 4, [1, 4, 2, 4, 3]),
    ([5, 10, 15], 0, [5, 0, 10, 0, 15]),
    ([-1, -2, -3], 1, [-1, 1, -2, 1, -3]),
    ([1, 1, 1], 4, [1, 4, 1, 4, 1]),
    ([], 5, []),
    ([1], 5, [1]),
    ([-1, -2, -3], 5, [-1, 5, -2, 5, -3]),
    ([1, 1, 1], 5, [1, 5, 1, 5, 1]),
    ([-1, -2, -3], 4, [-1, 4, -2, 4, -3]),
    ([1, 1, 1], 4, [1, 4, 1, 4, 1]),
])
def test_intersperse(numbers, delimeter, expected):
    assert intersperse(numbers, delimeter) == expected

def test_intersperse_empty_list_with_delimeter():
    assert intersperse([], 5) == []

def test_intersperse_single_element_list_with_delimeter():
    assert intersperse([10], 5) == [10]

def test_intersperse_large_list_with_delimeter():
    numbers = list(range(10))
    delimeter = 5
    expected = [0, 5, 1, 5, 2, 5, 3, 5, 4, 5, 5, 5, 6, 5, 7, 5, 8, 5, 9]
    assert intersperse(numbers, delimeter) == expected

def test_intersperse_empty_strings():
    assert intersperse([], 4) == []

def test_intersperse_single_element_list():
    assert intersperse([1], 4) == [1]

def test_intersperse_large_list():
    large_list = list(range(100))
    expected = [x for i, x in enumerate(large_list) if i == 0 or (i > 0 and i % 2 == 1)]
    expected = [x for pair in zip(large_list, [4]*len(large_list)) for i, x in enumerate(pair) if i == 0 or (i > 0 and i % 2 == 0)]
    assert intersperse(large_list, 4) == expected

def test_intersperse_negative_numbers():
    assert intersperse([-1, -2, -3], 4) == [-1, 4, -2, 4, -3]