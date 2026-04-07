
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

def test_eat_normal_case():
    # Tests a normal case where enough carrots are available
    assert eat(5, 6, 10) == [11, 4]

def test_eat_exact_match():
    # Tests the case where the remaining carrots exactly match the need
    assert eat(1, 10, 10) == [11, 0]

def test_eat_not_enough_carrots():
    # Tests the case where there are not enough remaining carrots
    assert eat(2, 11, 5) == [7, 0]

def test_eat_no_carrots_needed():
    # Tests the case where no more carrots are needed
    assert eat(5, 0, 10) == [5, 10]

def test_eat_zero_initial_carrots():
    # Tests the case where the initial number of carrots is zero
    assert eat(0, 5, 10) == [5, 5]

def test_eat_zero_need():
    # Tests the case where no carrots are needed
    assert eat(5, 0, 0) == [5, 0]

def test_eat_large_numbers():
    # Tests the function with large numbers
    assert eat(100, 200, 300) == [300, 100]

def test_eat_large_numbers_not_enough():
    # Tests the function with large numbers and not enough carrots
    assert eat(100, 200, 50) == [150, 0]

def test_eat_max_values():
    # Tests the function with maximum values
    assert eat(1000, 1000, 1000) == [2000, 0]

def test_eat_max_values_not_enough():
    # Tests the function with maximum values and not enough carrots
    assert eat(1000, 1000, 500) == [1500, 0]

def test_eat_edge_case():
    # Tests the case where all inputs are zero
    assert eat(0, 0, 0) == [0, 0]

def test_eat_edge_case_2():
    # Tests the case where all inputs are one
    assert eat(1, 1, 1) == [2, 0]

def test_eat_invalid_input_type_number():
    with pytest.raises(TypeError):
        eat("5", 6, 10)

def test_eat_invalid_input_type_need():
    with pytest.raises(TypeError):
        eat(5, "6", 10)

def test_eat_invalid_input_type_remaining():
    with pytest.raises(TypeError):
        eat(5, 6, "10")

def test_eat_negative_need():
    # Tests the case where need is negative - should raise ValueError
    with pytest.raises(ValueError):
        eat(5, -6, 10)

def test_eat_negative_remaining():
    # Tests the case where remaining is negative - should raise ValueError
    with pytest.raises(ValueError):
        eat(5, 6, -10)

def test_eat_negative_all():
    # Tests the case where all inputs are negative - should raise ValueError
    with pytest.raises(ValueError):
        eat(-5, -6, -10)

def test_eat_overflow():
    # Tests the case where the sum of initial and remaining overflows
    assert eat(999, 999, 1000) == [1998, 0]

def test_eat_underflow():
    # Tests the case where the sum of initial and remaining underflows
    assert eat(999, 1, -1000) == [0, 0]