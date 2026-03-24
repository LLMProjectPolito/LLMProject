
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
        raise ValueError("Inputs must be between 0 and 1000.")

    total_eaten = number
    remaining_carrots = remaining
    
    if remaining >= need:
        total_eaten += need
        remaining_carrots -= need
    else:
        total_eaten += remaining
        remaining_carrots = 0
    
    return [total_eaten, remaining_carrots]

@pytest.mark.parametrize("number, need, remaining, expected", [
    (5, 6, 10, [11, 4]),  # Basic case: need > remaining
    (4, 8, 9, [12, 1]),  # Basic case: need > remaining
    (1, 10, 10, [11, 0]), # Basic case: need > remaining
    (2, 11, 5, [7, 0]),  # Basic case: need > remaining
    (0, 0, 0, [0, 0]),   # All zeros
    (0, 5, 10, [5, 5]),  # Initial eaten is zero
    (1000, 1000, 1000, [2000, 0]), # Max values
    (0, 1000, 0, [0, 0]), # Need is max, remaining is zero
    (1000, 0, 1000, [1000, 1000]), # Need is zero
    (500, 500, 500, [1000, 0]), # Need and remaining equal
    (100, 200, 100, [200, 0]), # Need is double remaining
    (200, 100, 100, [300, 0]), # Remaining is double need
    (0, 1, 1, [1, 0]),   # Small values
    (1, 0, 1, [1, 1]),   # Need is zero, small values
    (1000, 1, 1, [1001, 0]), # Max eaten, small need/remaining
    (1, 1000, 1, [1001, 0]), # Small eaten, max need/remaining
    (5, 5, 5, [10, 0]), # need and remaining equal
    (10, 5, 10, [15, 5]), # need less than remaining
    (5, 10, 5, [15, 0]), # need greater than remaining
    (0, 10, 5, [10, 0]), # initial eaten is zero, need greater than remaining
])
def test_eat(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected

def test_negative_inputs():
    with pytest.raises(TypeError):
        eat(-1, 5, 10)
    with pytest.raises(TypeError):
        eat(5, -1, 10)
    with pytest.raises(TypeError):
        eat(5, 5, -1)

def test_invalid_input_type():
    with pytest.raises(TypeError):
        eat(5.5, 5, 10)
    with pytest.raises(TypeError):
        eat(5, 5.5, 10)
    with pytest.raises(TypeError):
        eat(5, 5, 10.5)

def test_input_out_of_range():
    with pytest.raises(ValueError):
        eat(1001, 5, 10)
    with pytest.raises(ValueError):
        eat(5, 1001, 10)
    with pytest.raises(ValueError):
        eat(5, 5, 1001)

def test_need_is_zero():
    assert eat(100, 0, 100) == [100, 100]