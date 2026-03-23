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
    remaining_carrots = remaining - eaten
    return [total_eaten, remaining_carrots]

def test_eat_zero_remaining():
    """
    Test case for when there are no remaining carrots.
    This is an edge case because the rabbit will eat 0 carrots from the remaining stock,
    and the function should handle this gracefully.
    """
    assert eat(5, 6, 0) == [5, 0]

def test_eat_sufficient_remaining():
    """Test case when there are enough remaining carrots to satisfy the need."""
    assert eat(5, 6, 10) == [11, 4]

def test_eat_limited_remaining():
    """Test case when there are not enough remaining carrots."""
    assert eat(4, 8, 9) == [12, 1]

def test_eat_exact_remaining():
    """Test case when remaining carrots exactly match the need."""
    assert eat(1, 10, 10) == [11, 0]

def test_eat_all_remaining():
    """Test case when the need is greater than the remaining carrots."""
    assert eat(2, 11, 5) == [7, 0]