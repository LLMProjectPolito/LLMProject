import pytest

def test_string_sequence_zero():
    assert string_sequence(0) == '0'

def test_string_sequence_positive():
    assert string_sequence(5) == '0 1 2 3 4 5'

def test_string_sequence_negative():
    with pytest.raises(ValueError):
        string_sequence(-1)

def test_string_sequence_non_integer():
    with pytest.raises(TypeError):
        string_sequence('a')

def test_string_sequence_large_input():
    result = string_sequence(100)
    numbers = result.split()
    assert len(numbers) == 101
    for i in range(101):
        assert numbers[i] == str(i)

def test_string_sequence_edge_case():
    assert string_sequence(1) == '0 1'