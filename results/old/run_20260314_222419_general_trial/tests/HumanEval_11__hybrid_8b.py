import pytest

@pytest.mark.parametrize("a, b, expected", [
    ('010', '110', '100'),
    ('1010', '0010', '1000'),
    ('1111', '0000', '1111'),
    ('0000', '1111', '1111'),
    ('', '', ''),
    ('1', '1', '0'),
    ('1', '0', '1'),
    ('0', '1', '1'),
    ('0', '0', '0'),
    ('0', '0', '0'),
    ('0', '1', '1'),
    ('1', '0', '1'),
    ('1', '1', '0'),
    ('010', '110', '100'),
    ('1010', '1100', '0110'),
    ('1111', '1111', '0000'),
    ('0000', '0000', '0000'),
    ('1001', '0110', '1111'),
])
def test_string_xor(a: str, b: str, expected: str):
    assert string_xor(a, b) == expected

def test_string_xor_invalid_input():
    with pytest.raises(ValueError):
        string_xor('0102', '110')

def test_string_xor_unequal_length():
    assert string_xor('1010', '10') == '1110'

def test_string_xor_empty_string():
    assert string_xor('', '1010') == '1010'

def test_string_xor_length_mismatch():
    with pytest.raises(ValueError):
        string_xor('10', '100')

def test_string_xor_invalid_input():
    with pytest.raises(ValueError):
        string_xor('10a', '100')

def test_string_xor_empty_strings():
    assert string_xor('', '') == ''

def test_string_xor_single_character():
    assert string_xor('0', '0') == '0'
    assert string_xor('1', '1') == '0'
    assert string_xor('1', '0') == '1'

def test_string_xor_long_input():
    a = '1' * 100
    b = '0' * 100
    assert string_xor(a, b) == '1' * 100