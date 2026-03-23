def test_even_odd_count_positive():
    assert even_odd_count(12345) == (2, 3)

def test_even_odd_count_negative():
    assert even_odd_count(-12) == (1, 1)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_all_even():
    assert even_odd_count(2468) == (4, 0)

def test_even_odd_count_all_odd():
    assert even_odd_count(13579) == (0, 5)

def test_even_odd_count_mixed():
    assert even_odd_count(1234567890) == (5, 5)

def test_even_odd_count_single_digit_even():
    assert even_odd_count(2) == (1, 0)

def test_even_odd_count_single_digit_odd():
    assert even_odd_count(1) == (0, 1)

def test_even_odd_count_large_number():
    assert even_odd_count(12345678901234567890) == (5, 10)