import pytest

def test_incr_list_empty():
    assert incr_list([]) == []

def test_incr_list_single_element():
    assert incr_list([1]) == [2]

def test_incr_list_multiple_elements():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

def test_incr_list_large_list():
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

def test_incr_list_negative_numbers():
    assert incr_list([-1, -2, -3]) == [0, -1, -2]

def test_incr_list_zero():
    assert incr_list([0, 0, 0]) == [1, 1, 1]

def test_incr_list_floats():
    with pytest.raises(TypeError):
        incr_list([1.0, 2.0, 3.0])

def test_incr_list_non_numeric_values():
    with pytest.raises(TypeError):
        incr_list(['a', 'b', 'c'])

def test_incr_list_mixed_types():
    with pytest.raises(TypeError):
        incr_list([1, 'a', 3.0])

def test_incr_list_none():
    with pytest.raises(TypeError):
        incr_list([None, None, None])