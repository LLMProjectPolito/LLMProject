def test_even_odd_count_positive():
    assert even_odd_count(123) == (1, 2)

def test_even_odd_count_negative():
    assert even_odd_count(-12) == (1, 1)

def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)

def test_even_odd_count_single_even():
    assert even_odd_count(2) == (1, 0)

def test_even_odd_count_single_odd():
    assert even_odd_count(1) == (0, 1)

def test_even_odd_count_all_even():
    assert even_odd_count(2468) == (4, 0)

def test_even_odd_count_all_odd():
    assert even_odd_count(13579) == (0, 5)