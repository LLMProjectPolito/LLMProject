import pytest

@pytest.mark.parametrize("n, expected", [
    (0, '0'),
    (1, '0 1'),
    (5, '0 1 2 3 4 5'),
    (10, '0 1 2 3 4 5 6 7 8 9 10')
])
def test_string_sequence(n, expected):
    assert string_sequence(n) == expected

def test_string_sequence_negative():
    with pytest.raises(ValueError):
        string_sequence(-1)

def test_string_sequence_non_integer():
    with pytest.raises(TypeError):
        string_sequence('a')

def test_string_sequence_float():
    with pytest.raises(TypeError):
        string_sequence(5.5)

def test_string_sequence_zero():
    assert string_sequence(0) == '0'

def test_string_sequence_one():
    assert string_sequence(1) == '0 1'

def test_string_sequence_five():
    assert string_sequence(5) == '0 1 2 3 4 5'

def test_string_sequence_ten():
    assert string_sequence(10) == '0 1 2 3 4 5 6 7 8 9 10'