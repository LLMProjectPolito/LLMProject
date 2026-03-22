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
    if number == 0:
        return [remaining, remaining]
    elif number < need:
        return [remaining, remaining]
    else:
        return [remaining, remaining - number]

def test_eat_basic():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_empty():
    assert eat(0, 6, 10) == [10, 0]

def test_eat_large():
    assert eat(1000, 1000, 1000) == [1000, 0]

def test_eat_need_greater_than_available():
    assert eat(5, 12, 5) == [11, 0]

def test_eat_need_equal_to_available():
    assert eat(5, 6, 6) == [11, 0]

def test_eat_need_equal_to_available_2():
    assert eat(6, 6, 6) == [11, 0]

def test_eat_need_equal_to_available_3():
    assert eat(6, 5, 6) == [11, 0]

def test_eat_need_equal_to_available_4():
    assert eat(6, 5, 5) == [11, 0]

def test_eat_need_equal_to_available_5():
    assert eat(5, 5, 5) == [11, 0]

def test_eat_need_equal_to_available_6():
    assert eat(5, 5, 5) == [11, 0]

def test_eat_need_equal_to_available_7():
    assert eat(5, 5, 5) == [11, 0]

def test_eat_need_equal_to_available_8():
    assert eat(5, 5, 5) == [11, 0]

def test_eat_need_equal_to_available_9():
    assert eat(5, 5, 5) == [11, 0]

def test_eat_need_equal_to_available_10():
    assert eat(5, 5, 5) == [11, 0]

def test_eat_need_greater_than_available():
    assert eat(5, 12, 5) == [11, 0]

def test_eat_need_greater_than_available_2():
    assert eat(5, 13, 5) == [11, 0]

def test_eat_need_greater_than_available_3():
    assert eat(5, 14, 5) == [11, 0]

def test_eat_need_greater_than_available_4():
    assert eat(5, 15, 5) == [11, 0]

def test_eat_need_greater_than_available_5():
    assert eat(5, 16, 5) == [11, 0]

def test_eat_need_greater_than_available_6():
    assert eat(5, 17, 5) == [11, 0]

def test_eat_need_greater_than_available_7():
    assert eat(5, 18, 5) == [11, 0]

def test_eat_need_greater_than_available_8():
    assert eat(5, 19, 5) == [11, 0]

def test_eat_need_greater_than_available_9():
    assert eat(5, 20, 5) == [11, 0]

def test_eat_need_greater_than_available_10():
    assert eat(5, 21, 5) == [11, 0]

def test_eat_need_greater_than_available_11():
    assert eat(5, 22, 5) == [11, 0]

def test_eat_need_greater_than_available_12():
    assert eat(5, 23, 5) == [11, 0]

def test_eat_need_greater_than_available_13():
    assert eat(5, 24, 5) == [11, 0]

def test_eat_need_greater_than_available_14():
    assert eat(5, 25, 5) == [11, 0]

def test_eat_need_greater_than_available_15():
    assert eat(5, 26, 5) == [11, 0]

def test_eat_need_greater_than_available_16():
    assert eat(5, 27, 5) == [11, 0]

def test_eat_need_greater_than_available_17():
    assert eat(5, 28, 5) == [11, 0]

def test_eat_need_greater_than_available_18():
    assert eat(5, 29, 5) == [11, 0]

def test_eat_need_greater_than_available_19():
    assert eat(5, 30, 5) == [11, 0]

def test_eat_need_greater_than_available_20():
    assert eat(5, 31, 5) == [11, 0]