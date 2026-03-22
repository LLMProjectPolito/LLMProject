import pytest
import math

def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you're eating carrots.
    You have eaten a certain number of carrots, and you need to eat more carrots to complete the day's meals.
    You should return an array of [ total number of eaten carrots after your meals,
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
    * @need : integer
        the number of carrots that you need to eat.
    * @remaining : integer
        the number of remaining carrots thet exist in stock
    
    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    Have fun :)
    """
    eaten = number
    remaining = remaining - need
    if remaining <= 0:
        return [eaten, 0]
    else:
        return [eaten, remaining]

def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you're eating carrots.
    You have eaten a certain number of carrots, and you need to eat more carrots to complete the day's meals.
    You should return an array of [ total number of eaten carrots after your meals,
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
    * @need : integer
        the number of carrots that you need to eat.
    * @remaining : integer
        the number of remaining carrots thet exist in stock
    
    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    Have fun :)
    """
    eaten = number
    remaining = remaining - need
    if remaining <= 0:
        return [eaten, 0]
    else:
        return [eaten, remaining]

def test_eat():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]
    assert eat(2, 11, 5) == [7, 0]
    assert eat(0, 5, 10) == [0, 0]
    assert eat(10, 0, 10) == [10, 0]
    assert eat(1000, 1000, 1000) == [1000, 0]
    assert eat(5, 0, 10) == [5, 0]
    assert eat(0, 0, 10) == [0, 0]
    print("All tests passed!")

if __name__ == "__main__":
    test_eat()