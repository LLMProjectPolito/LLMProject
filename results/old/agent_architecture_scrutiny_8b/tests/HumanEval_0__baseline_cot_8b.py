import pytest

def test_has_close_elements_empty_list():
    assert has_close_elements([], 0.5) == False

def test_has_close_elements_single_element_list():
    assert has_close_elements([1.0], 0.5) == False

def test_has_close_elements_two_elements_list_not_close():
    assert has_close_elements([1.0, 2.0], 0.5) == False

def test_has_close_elements_two_elements_list_close():
    assert has_close_elements([1.0, 1.1], 0.5) == True

def test_has_close_elements_multiple_elements_list_not_close():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False

def test_has_close_elements_multiple_elements_list_close():
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True

def test_has_close_elements_list_with_duplicates():
    assert has_close_elements([1.0, 1.0, 2.0], 0.5) == True

def test_has_close_elements_list_with_negative_numbers():
    assert has_close_elements([-1.0, -1.1, 2.0], 0.5) == True

def test_has_close_elements_list_with_zero():
    assert has_close_elements([0.0, 0.1, 2.0], 0.5) == True

def test_has_close_elements_threshold_zero():
    assert has_close_elements([1.0, 2.0, 3.0], 0.0) == False

def test_has_close_elements_threshold_negative():
    with pytest.raises(ValueError):
        has_close_elements([1.0, 2.0, 3.0], -0.5)

def test_has_close_elements_threshold_non_numeric():
    with pytest.raises(TypeError):
        has_close_elements([1.0, 2.0, 3.0], 'a')