import pytest

def test_choose_num_typical_case():
    assert choose_num(12, 15) == 14

def test_choose_num_no_even_numbers():
    assert choose_num(13, 15) == 14

def test_choose_num_no_even_numbers_in_range():
    assert choose_num(13, 13) == -1

def test_choose_num_x_greater_than_y():
    assert choose_num(15, 12) == -1

def test_choose_num_x_equals_y_and_x_is_even():
    assert choose_num(12, 12) == 12

def test_choose_num_x_equals_y_and_x_is_odd():
    assert choose_num(13, 13) == -1

def test_choose_num_x_is_negative():
    with pytest.raises(ValueError):
        choose_num(-1, 12)

def test_choose_num_y_is_negative():
    with pytest.raises(ValueError):
        choose_num(12, -1)

def test_choose_num_x_is_zero():
    with pytest.raises(ValueError):
        choose_num(0, 12)

def test_choose_num_y_is_zero():
    with pytest.raises(ValueError):
        choose_num(12, 0)

def test_choose_num_x_is_not_integer():
    with pytest.raises(TypeError):
        choose_num(12.5, 12)

def test_choose_num_y_is_not_integer():
    with pytest.raises(TypeError):
        choose_num(12, 12.5)

def test_choose_num_x_is_string():
    with pytest.raises(TypeError):
        choose_num('a', 12)

def test_choose_num_y_is_string():
    with pytest.raises(TypeError):
        choose_num(12, 'a')