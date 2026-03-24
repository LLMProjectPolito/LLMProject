
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
    if not (0 <= number <= 1000 and 0 <= need <= 1000 and 0 <= remaining <= 1000):
        raise ValueError("Inputs must be between 0 and 1000")

    if need < 0:
        raise ValueError("Need cannot be negative")
    if remaining < 0:
        raise ValueError("Remaining cannot be negative")

    total_eaten = number
    remaining_after_eating = remaining
    if remaining >= need:
        total_eaten += need
        remaining_after_eating -= need
    else:
        total_eaten += remaining
        remaining_after_eating = 0
    return [total_eaten, remaining_after_eating]

def test_enough_remaining_carrots():
    assert eat(5, 6, 10) == [11, 4]

def test_insufficient_remaining_carrots():
    assert eat(4, 8, 9) == [12, 1]

def test_zero_remaining_carrots():
    assert eat(1, 10, 0) == [1, 0]

def test_zero_need_carrots():
    assert eat(5, 0, 10) == [5, 10]

def test_zero_eaten_carrots():
    assert eat(0, 10, 10) == [10, 0]

def test_edge_case_max_values():
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_edge_case_min_values():
    assert eat(0, 0, 0) == [0, 0]

def test_need_equals_remaining_carrots():
    assert eat(2, 5, 5) == [7, 0]

def test_large_numbers():
    assert eat(500, 600, 700) == [1200, 100]

def test_need_significantly_greater_than_remaining():
    assert eat(1, 100, 2) == [3, 0]

def test_input_validation_number_too_large():
    with pytest.raises(ValueError) as excinfo:
        eat(1001, 6, 10)
    assert str(excinfo.value) == "Inputs must be between 0 and 1000"

def test_input_validation_need_too_large():
    with pytest.raises(ValueError) as excinfo:
        eat(5, 1001, 10)
    assert str(excinfo.value) == "Inputs must be between 0 and 1000"

def test_input_validation_remaining_too_large():
    with pytest.raises(ValueError) as excinfo:
        eat(5, 6, 1001)
    assert str(excinfo.value) == "Inputs must be between 0 and 1000"

def test_negative_need_raises_error():
    with pytest.raises(ValueError) as excinfo:
        eat(5, -1, 10)
    assert str(excinfo.value) == "Need cannot be negative"

def test_negative_remaining_raises_error():
    with pytest.raises(ValueError) as excinfo:
        eat(5, 6, -1)
    assert str(excinfo.value) == "Remaining cannot be negative"

def test_negative_number_raises_error():
    with pytest.raises(ValueError) as excinfo:
        eat(-1, 6, 10)
    assert str(excinfo.value) == "Inputs must be between 0 and 1000"