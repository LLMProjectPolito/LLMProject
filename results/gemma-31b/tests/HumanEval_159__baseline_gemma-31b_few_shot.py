
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

def test_eat_examples():
    """Tests the examples provided in the docstring"""
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]
    assert eat(2, 11, 5) == [7, 0]

def test_eat_sufficient_carrots():
    """Tests cases where there are more than enough carrots to satisfy the need"""
    # Rabbit needs 5, has 100 available
    assert eat(10, 5, 100) == [15, 95]
    # Rabbit needs 1, has 2 available
    assert eat(0, 1, 2) == [1, 1]

def test_eat_insufficient_carrots():
    """Tests cases where there are not enough carrots to satisfy the need"""
    # Rabbit needs 100, has 0 available
    assert eat(10, 100, 0) == [10, 0]
    # Rabbit needs 10, has 3 available
    assert eat(5, 10, 3) == [8, 0]

def test_eat_zero_values():
    """Tests edge cases involving zero"""
    # Everything is zero
    assert eat(0, 0, 0) == [0, 0]
    # Need is zero, should not eat any more
    assert eat(10, 0, 10) == [10, 10]
    # Already eaten zero, need some, none available
    assert eat(0, 5, 0) == [0, 0]

def test_eat_max_constraints():
    """Tests the upper boundary constraints (1000)"""
    # Max values: already eaten 1000, need 1000, 1000 available
    assert eat(1000, 1000, 1000) == [2000, 0]
    # Max need, but 0 available
    assert eat(1000, 1000, 0) == [1000, 0]
    # Max available, but 0 need
    assert eat(1000, 0, 1000) == [1000, 1000]