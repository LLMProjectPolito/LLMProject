import pytest

def test_string_xor_equal_length():
    assert string_xor('010', '110') == '100'

def test_string_xor_unequal_length():
    with pytest.raises(ValueError):
        string_xor('010', '11')

def test_string_xor_invalid_input():
    with pytest.raises(ValueError):
        string_xor('012', '110')

def test_string_xor_empty_string():
    with pytest.raises(ValueError):
        string_xor('', '110')

def test_string_xor_both_empty():
    with pytest.raises(ValueError):
        string_xor('', '')

def test_string_xor_single_character():
    assert string_xor('0', '1') == '1'

def test_string_xor_long_strings():
    assert string_xor('10101010', '11001100') == '01100110'

def test_string_xor_same_strings():
    assert string_xor('1010', '1010') == '0000'

def test_string_xor_all_zeros():
    assert string_xor('0000', '0000') == '0000'

def test_string_xor_all_ones():
    assert string_xor('1111', '1111') == '0000'