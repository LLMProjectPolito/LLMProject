
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

@pytest.mark.parametrize("number, need, remaining, expected", [
    # Examples provided in the docstring
    (5, 6, 10, [11, 4]),
    (4, 8, 9, [12, 1]),
    (1, 10, 10, [11, 0]),
    (2, 11, 5, [7, 0]),
])
def test_eat_docstring_examples(number, need, remaining, expected):
    """Tests the specific examples provided in the problem description."""
    assert eat(number, need, remaining) == expected

@pytest.mark.parametrize("number, need, remaining, expected", [
    # Sufficient stock: need <= remaining
    (0, 5, 5, [5, 0]),      # need == remaining
    (10, 2, 10, [12, 8]),   # need < remaining
    (0, 0, 10, [0, 10]),    # need == 0
    (100, 50, 100, [150, 50]),
])
def test_eat_sufficient_stock(number, need, remaining, expected):
    """Tests scenarios where there are enough carrots in stock to satisfy the need."""
    assert eat(number, need, remaining) == expected

@pytest.mark.parametrize("number, need, remaining, expected", [
    # Insufficient stock: need > remaining
    (0, 10, 5, [5, 0]),     # need > remaining, starting from 0
    (10, 20, 5, [15, 0]),   # need > remaining, starting from 10
    (5, 5, 2, [7, 0]),      # need > remaining
    (0, 1, 0, [0, 0]),      # need > 0, but 0 remaining
])
def test_eat_insufficient_stock(number, need, remaining, expected):
    """Tests scenarios where the rabbit cannot satisfy the full need due to low stock."""
    assert eat(number, need, remaining) == expected

@pytest.mark.parametrize("number, need, remaining, expected", [
    # Boundary conditions and constraints
    (0, 0, 0, [0, 0]),              # All zeros
    (1000, 1000, 1000, [2000, 0]),  # Maximum constraints (sufficient)
    (1000, 1000, 0, [1000, 0]),     # Maximum constraints (insufficient)
    (0, 1000, 1000, [1000, 0]),     # Max need and remaining
    (1000, 0, 1000, [1000, 1000]),  # Max number and remaining, 0 need
])
def test_eat_boundary_conditions(number, need, remaining, expected):
    """Tests the edges of the defined constraints (0 and 1000)."""
    assert eat(number, need, remaining) == expected