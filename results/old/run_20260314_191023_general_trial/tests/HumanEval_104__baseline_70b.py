import pytest

def test_unique_digits_empty_list():
    assert unique_digits([]) == []

def test_unique_digits_no_even_digits():
    assert unique_digits([1, 15, 33]) == [1, 15, 33]

def test_unique_digits_with_even_digits():
    assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33]

def test_unique_digits_all_even_digits():
    assert unique_digits([10, 20, 30]) == []

def test_unique_digits_single_element_no_even_digit():
    assert unique_digits([1]) == [1]

def test_unique_digits_single_element_even_digit():
    assert unique_digits([2]) == []

def test_unique_digits_duplicates():
    assert unique_digits([1, 1, 15, 15, 33]) == [1, 15, 33]

def test_unique_digits_negative_numbers():
    with pytest.raises(ValueError):
        unique_digits([-1, -2, -3])

def test_unique_digits_non_integer():
    with pytest.raises(TypeError):
        unique_digits([1, 2, '3'])

def test_unique_digits_floats():
    with pytest.raises(TypeError):
        unique_digits([1.0, 2.0, 3.0])

def test_unique_digits_sorted_output():
    assert unique_digits([33, 15, 1]) == [1, 15, 33]