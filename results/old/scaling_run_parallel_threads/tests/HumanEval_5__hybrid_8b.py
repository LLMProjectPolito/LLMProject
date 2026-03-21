import pytest

@pytest.mark.parametrize("numbers, delimeter, expected", [
    ([], 4, []),
    ([1], 4, [1]),
    ([1, 2, 3], 4, [1, 4, 2, 4, 3]),
    ([1, 2, 3, 4, 5], 0, [1, 0, 2, 0, 3, 0, 4, 0, 5]),
    ([-1, -2, -3], 1, [-1, 1, -2, 1, -3]),
    ([1, 2], 4, [1, 4, 2]),
    ([1, 0, 3], 4, [1, 4, 0, 4, 3]),
    ([1], 0, [1]),
    ([-1, -2], 4, [-1, 4, -2]),
    ([], 0, []),
    ([-1, -2, -3], 4, [-1, 4, -2, 4, -3]),
])
def test_intersperse(numbers, delimeter, expected):
    assert intersperse(numbers, delimeter) == expected

def test_intersperse_empty_delimeter():
    with pytest.raises(TypeError):
        intersperse([1, 2, 3], None)

def test_intersperse_invalid_input():
    with pytest.raises(TypeError):
        intersperse("123", 4)

def test_intersperse_invalid_delimeter():
    with pytest.raises(TypeError):
        intersperse([1, 2, 3], "4")

def test_intersperse_with_negative_delimeter():
    assert intersperse([1, 2, 3], -4) == [1, -4, 2, -4, 3]

def test_intersperse_with_zero_delimeter():
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

def test_intersperse_with_single_element_list_and_zero_delimeter():
    assert intersperse([1], 0) == [1]

def test_intersperse_with_empty_list_and_zero_delimeter():
    assert intersperse([], 0) == []