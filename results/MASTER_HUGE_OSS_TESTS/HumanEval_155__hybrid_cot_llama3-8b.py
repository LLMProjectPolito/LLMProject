import pytest

def test_even_odd_count_signature():
    assert even_odd_count.__name__ == 'even_odd_count'
    assert even_odd_count.__annotations__['return'] == 'tuple'
    assert even_odd_count.__annotations__['num'] == 'int'

def test_even_odd_count_happy_path():
    assert even_odd_count(123) == (1, 2)

def test_even_odd_count_negative_number():
    assert even_odd_count(-12) == (1, 1)
    assert even_odd_count(-123) == (2, 1)

def test_even_odd_count_single_digit():
    assert even_odd_count(5) == (0, 1)
    assert even_odd_count(-5) == (0, 1)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)
    assert even_odd_count(-0) == (1, 0)

def test_even_odd_count_negative_single_digit():
    pytest.raises(TypeError, even_odd_count, '-')

def test_even_odd_count_non_integer_input():
    with pytest.raises(TypeError):
        even_odd_count('123')

def test_even_odd_count_large_integer():
    assert even_odd_count(12345678901234567890) == (10, 10)
    assert even_odd_count(-12345678901234567890) == (10, 9)

def test_even_odd_count_multiples_of_10():
    assert even_odd_count(10) == (1, 0)
    assert even_odd_count(20) == (2, 0)

def test_even_odd_count_duplicate_counts():
    assert even_odd_count(121212) == (5, 5)
    assert even_odd_count(1234343) == (4, 4)

def test_even_odd_count_single_digit_even():
    assert even_odd_count(2) == (1, 0)
    assert even_odd_count(4) == (1, 0)
    assert even_odd_count(6) == (1, 0)

def test_even_odd_count_single_digit_odd():
    assert even_odd_count(1) == (0, 1)
    assert even_odd_count(3) == (0, 1)
    assert even_odd_count(5) == (0, 1)