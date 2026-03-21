import pytest

def test_has_close_elements_empty_list():
    assert has_close_elements([], 0.5) == False

def test_has_close_elements_single_element_list():
    assert has_close_elements([1.0], 0.5) == False

def test_has_close_elements_no_close_elements():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False

def test_has_close_elements_close_elements():
    assert has_close_elements([1.0, 1.1], 0.5) == True

def test_has_close_elements_close_elements_in_list():
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True

def test_has_close_elements_large_threshold():
    assert has_close_elements([1.0, 2.0, 3.0], 10.0) == True

def test_has_close_elements_zero_threshold():
    assert has_close_elements([1.0, 2.0, 3.0], 0.0) == False

def test_has_close_elements_negative_threshold():
    with pytest.raises(ValueError):
        has_close_elements([1.0, 2.0, 3.0], -0.5)

def test_has_close_elements_non_numeric_threshold():
    with pytest.raises(TypeError):
        has_close_elements([1.0, 2.0, 3.0], 'a')

def test_has_close_elements_non_numeric_list():
    with pytest.raises(TypeError):
        has_close_elements(['a', 'b', 'c'], 0.5)