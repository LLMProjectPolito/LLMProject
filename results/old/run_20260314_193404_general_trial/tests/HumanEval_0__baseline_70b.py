import pytest

def test_has_close_elements_no_close_numbers():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False

def test_has_close_elements_with_close_numbers():
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True

def test_has_close_elements_empty_list():
    assert has_close_elements([], 0.5) == False

def test_has_close_elements_single_element_list():
    assert has_close_elements([1.0], 0.5) == False

def test_has_close_elements_two_elements_list_no_close_numbers():
    assert has_close_elements([1.0, 2.0], 0.5) == False

def test_has_close_elements_two_elements_list_with_close_numbers():
    assert has_close_elements([1.0, 1.1], 0.5) == False
    assert has_close_elements([1.0, 1.1], 0.2) == True

def test_has_close_elements_negative_threshold():
    with pytest.raises(ValueError):
        has_close_elements([1.0, 2.0], -0.5)

def test_has_close_elements_zero_threshold():
    assert has_close_elements([1.0, 2.0], 0.0) == False

def test_has_close_elements_large_threshold():
    assert has_close_elements([1.0, 2.0], 10.0) == True