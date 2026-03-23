import pytest

def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    
    Example:
    * eat(5, 6, 10) -> [11, 4]
    * eat(4, 8, 9) -> [12, 1]
    * eat(1, 10, 10) -> [11, 0]
    * eat(2, 11, 5) -> [7, 0]
    
    Variables:
    @number : integer
        the number of carrots that you have eaten.
    @need : integer
        the number of carrots that you need to eat.
    @remaining : integer
        the number of remaining carrots thet exist in stock
    
    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    Have fun :)
    """
    eaten = min(need, remaining)
    total_eaten = number + eaten
    left = remaining - eaten
    return [total_eaten, left]

@pytest.mark.parametrize("number, need, remaining, expected", [
    (5, 6, 10, [11, 4]),
    (4, 8, 9, [12, 1]),
    (1, 10, 10, [11, 0]),
    (2, 11, 5, [7, 0]),
    (5, 2, 10, [7, 8]),
    (5, 6, 5, [10, 0]),
    (0, 5, 10, [5, 5]),
    (5, 0, 10, [5, 10]),
    (1000, 1000, 1000, [2000, 0]),
    (1, 1, 1, [2, 0]),
    (1, 2, 1, [2, 0]),
    (2, 1, 1, [3, 0]),
    (0, 0, 0, [0, 0]),
    (10, 5, 0, [10, 0]),
    (10, 0, 0, [10, 0]),
])
def test_eat(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected

def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_not_enough_carrots():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_exactly_enough_carrots():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_zero_remaining_carrots():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_zero_need():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_zero_number():
    assert eat(0, 5, 10) == [5, 5]

def test_eat_max_values():
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_eat_edge_cases():
    assert eat(1, 1, 1) == [2, 0]
    assert eat(1, 2, 1) == [2, 0]
    assert eat(2, 1, 1) == [3, 0]

def test_eat_large_need_small_remaining():
    assert eat(10, 100, 5) == [15, 0]

def test_eat_large_remaining_small_need():
    assert eat(10, 5, 100) == [15, 95]