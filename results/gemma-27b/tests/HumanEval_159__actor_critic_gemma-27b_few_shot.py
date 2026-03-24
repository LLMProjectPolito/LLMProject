
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
    
    eaten = min(need, remaining)
    total_eaten = number + eaten
    remaining -= eaten
    return [total_eaten, remaining]

@pytest.mark.parametrize(
    "number, need, remaining, expected",
    [
        (5, 6, 10, [11, 4]),
        (4, 8, 9, [12, 1]),
        (1, 10, 10, [11, 0]),
        (2, 11, 5, [7, 0]),
    ],
    ids=["basic_1", "basic_2", "basic_3", "basic_4"],
)
def test_eat_basic(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected

def test_eat_no_need():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_no_remaining():
    assert eat(5, 6, 0) == [5, 0]

def test_eat_exact_need():
    assert eat(5, 5, 5) == [10, 0]

def test_eat_large_need():
    assert eat(100, 500, 200) == [300, 0]

def test_eat_large_remaining():
    assert eat(100, 50, 500) == [150, 450]

@pytest.mark.parametrize(
    "number, need, remaining, expected",
    [
        (0, 5, 10, [5, 5]),
        (10, 0, 5, [10, 5]),
        (10, 5, 0, [10, 0]),
    ],
    ids=["zero_initial", "zero_need", "zero_remaining"],
)
def test_eat_zero_values(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected

def test_eat_max_values():
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_eat_edge_case_equal():
    assert eat(500, 500, 500) == [1000, 0]

def test_eat_edge_case_all_zero():
    assert eat(0, 0, 0) == [0, 0]

def test_eat_need_greater_than_remaining():
    assert eat(500, 600, 100) == [600, 0]

def test_eat_large_values():
    assert eat(900, 900, 900) == [1800, 0]

def test_eat_type_error_number():
    with pytest.raises(TypeError, match="Inputs must be integers."):
        eat(10.5, 5, 10)

def test_eat_type_error_need():
    with pytest.raises(TypeError, match="Inputs must be integers."):
        eat(10, 5.2, 10)

def test_eat_type_error_remaining():
    with pytest.raises(TypeError, match="Inputs must be integers."):
        eat(10, 5, 10.8)

def test_eat_value_error_negative_remaining():
    with pytest.raises(ValueError, match="Inputs must be between 0 and 1000."):
        eat(10, 5, -1)

def test_eat_value_error_negative_need():
    with pytest.raises(ValueError, match="Inputs must be between 0 and 1000."):
        eat(10, -5, 10)

def test_eat_value_error_negative_number():
    with pytest.raises(ValueError, match="Inputs must be between 0 and 1000."):
        eat(-10, 5, 10)

def test_eat_value_error_number_too_large():
    with pytest.raises(ValueError, match="Inputs must be between 0 and 1000."):
        eat(1001, 5, 10)

def test_eat_value_error_need_too_large():
    with pytest.raises(ValueError, match="Inputs must be between 0 and 1000."):
        eat(10, 1001, 10)

def test_eat_value_error_remaining_too_large():
    with pytest.raises(ValueError, match="Inputs must be between 0 and 1000."):
        eat(10, 5, 1001)