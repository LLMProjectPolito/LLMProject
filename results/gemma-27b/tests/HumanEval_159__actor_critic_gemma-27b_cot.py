
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

def test_eat_normal_case( ):
    assert eat(5, 6, 10) == [11, 4]

@pytest.mark.parametrize("initial, need, remaining, expected_eaten, expected_remaining", [
    (4, 8, 9, 12, 1),
    (100, 200, 300, 300, 100),
    (100, 200, 50, 150, 0),
    (1000, 1000, 1000, 2000, 0),
    (0, 1000, 1000, 1000, 0),
    (1000, 0, 1000, 1000, 1000),
    (999, 999, 999, 1998, 0),
    (5, 3, 5, 8, 0),
])
def test_eat_parameterized(initial, need, remaining, expected_eaten, expected_remaining):
    assert eat(initial, need, remaining) == [expected_eaten, expected_remaining]

def test_eat_need_zero():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_initial_equals_need():
    assert eat(5, 5, 10) == [10, 5]

def test_eat_both_zero():
    assert eat(0, 0, 10) == [0, 10]

def test_eat_need_exceeds_initial_plus_remaining():
    assert eat(5, 8, 2) == [7, 0]

def test_eat_negative_initial():
    with pytest.raises(ValueError):
        eat(-1, 5, 10)

def test_eat_negative_need():
    with pytest.raises(ValueError):
        eat(5, -1, 10)

def test_eat_negative_remaining():
    with pytest.raises(ValueError):
        eat(5, 6, -1)