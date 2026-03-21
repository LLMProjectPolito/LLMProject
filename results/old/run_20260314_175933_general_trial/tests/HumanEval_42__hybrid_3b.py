import pytest

@pytest.mark.parametrize("input_list, expected_output", [
    ([1, 2, 3], [2, 3, 4]),
    ([5, 3, 5, 2, 3, 3, 9, 0, 123], [6, 4, 6, 3, 4, 4, 10, 1, 124]),
    ([-1, -2, -3], [0, -1, -2]),
    ([0, 0, 0], [1, 1, 1]),
    ([], []),
    ([100], [101]),
    ([-100], [-99]),
])
def test_incr_list(input_list, expected_output):
    assert incr_list(input_list) == expected_output

def test_incr_list_type_error():
    with pytest.raises(TypeError):
        incr_list("not a list")

def test_incr_list_element_type_error():
    with pytest.raises(TypeError):
        incr_list([1, "not an integer", 3])

def test_incr_list_empty_list():
    assert incr_list([]) == []

def test_incr_list_single_element_list():
    assert incr_list([1]) == [2]

def test_incr_list_negative_numbers():
    assert incr_list([-1, -2, -3]) == [0, -1, -2]

def test_incr_list_large_numbers():
    assert incr_list([1000]) == [1001]

def test_incr_list_floats():
    with pytest.raises(TypeError):
        incr_list([1.0, 2.0, 3.0])

def test_incr_list_non_numeric_values():
    with pytest.raises(TypeError):
        incr_list(['a', 'b', 'c'])