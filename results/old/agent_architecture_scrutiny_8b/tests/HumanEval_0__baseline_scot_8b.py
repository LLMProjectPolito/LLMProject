import pytest

def test_has_close_elements_empty_list():
    assert has_close_elements([], 0.5) == False

def test_has_close_elements_single_element_list():
    assert has_close_elements([1.0], 0.5) == False

def test_has_close_elements_no_close_elements():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False

def test_has_close_elements_close_elements():
    assert has_close_elements([1.0, 1.1, 3.0], 0.5) == True

def test_has_close_elements_close_elements_at_start():
    assert has_close_elements([1.0, 1.1, 3.0, 4.0], 0.5) == True

def test_has_close_elements_close_elements_at_end():
    assert has_close_elements([1.0, 2.0, 3.0, 3.1], 0.5) == True

def test_has_close_elements_close_elements_in_middle():
    assert has_close_elements([1.0, 2.0, 2.1, 3.0], 0.5) == True

def test_has_close_elements_duplicate_elements():
    assert has_close_elements([1.0, 1.0, 3.0], 0.5) == True

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

def test_has_close_elements_large_list():
    large_list = [i for i in range(1000)]
    assert has_close_elements(large_list, 1.0) == False