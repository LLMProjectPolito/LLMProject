import pytest

def test_empty_list():
    assert has_close_elements([], 0.5) == False

def test_single_element_list():
    assert has_close_elements([1.0], 0.5) == False

def test_two_elements_list_not_close():
    assert has_close_elements([1.0, 2.0], 0.5) == False

def test_two_elements_list_close():
    assert has_close_elements([1.0, 1.1], 0.5) == True

def test_multiple_elements_list_not_close():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False

def test_multiple_elements_list_close():
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True

def test_threshold_zero():
    assert has_close_elements([1.0, 2.0, 3.0], 0) == False

def test_threshold_negative():
    with pytest.raises(ValueError):
        has_close_elements([1.0, 2.0, 3.0], -0.5)

def test_non_numeric_list():
    with pytest.raises(TypeError):
        has_close_elements(['a', 'b', 'c'], 0.5)

def test_non_numeric_threshold():
    with pytest.raises(TypeError):
        has_close_elements([1.0, 2.0, 3.0], 'a')