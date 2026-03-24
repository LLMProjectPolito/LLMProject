
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
    if not all(isinstance(arg, int) for arg in [number, need, remaining]):
        raise TypeError("Inputs must be integers.")
    if not (0 <= number <= 1000 and 0 <= need <= 1000 and 0 <= remaining <= 1000):
        raise ValueError("Inputs must be within the range 0-1000.")
    return [number + remaining, remaining - need] if remaining >= need else [number + remaining, 0]


def test_eat_enough_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_enough_but_some_left():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_exactly_enough_carrots():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_not_enough_carrots():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_zero_need():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_zero_remaining():
    assert eat(5, 6, 0) == [5, 0]

def test_eat_zero_eaten():
    assert eat(0, 6, 10) == [6, 4]

def test_eat_zero_eaten_zero_need():
    assert eat(0, 0, 10) == [0, 10]

def test_eat_large_numbers():
    assert eat(999, 999, 1000) == [1998, 1]

def test_eat_all_carrots_needed():
    assert eat(100, 100, 100) == [200, 0]

def test_eat_need_greater_than_remaining():
    assert eat(10, 20, 5) == [15, 0]

def test_eat_edge_case_max_values():
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_eat_edge_case_min_values():
    assert eat(0, 0, 0) == [0, 0]

def test_eat_number_greater_than_need():
    assert eat(10, 5, 10) == [20, 5]

def test_eat_negative_number():
    with pytest.raises(TypeError):
        eat(-1, 5, 10)

def test_eat_negative_need():
    with pytest.raises(TypeError):
        eat(5, -1, 10)

def test_eat_negative_remaining():
    with pytest.raises(TypeError):
        eat(5, 5, -1)

def test_eat_max_need():
    assert eat(0, 1000, 1000) == [2000, 0]

def test_eat_max_remaining():
    assert eat(0, 1000, 1000) == [2000, 0]

def test_eat_need_equals_remaining():
    assert eat(0, 500, 500) == [1000, 0]

def test_eat_number_equals_remaining():
    assert eat(500, 100, 500) == [1000, 0]