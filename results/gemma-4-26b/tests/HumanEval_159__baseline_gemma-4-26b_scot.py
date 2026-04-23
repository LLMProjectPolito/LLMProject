
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
    (5, 6, 10, [11, 4]),
    (4, 8, 9, [12, 1]),
    (1, 10, 10, [11, 0]),
    (2, 11, 5, [7, 0]),
])
def test_docstring_examples(number, need, remaining, expected):
    """Validates the examples provided in the function documentation."""
    assert eat(number, need, remaining) == expected

@pytest.mark.parametrize("number, need, remaining, expected", [
    (10, 5, 20, [15, 15]),
    (0, 1, 100, [1, 99]),
    (500, 100, 500, [600, 400]),
])
def test_sufficient_stock(number, need, remaining, expected):
    """Tests cases where there are more carrots in stock than the rabbit needs."""
    assert eat(number, need, remaining) == expected

@pytest.mark.parametrize("number, need, remaining, expected", [
    (10, 20, 5, [15, 0]),
    (0, 10, 2, [2, 0]),
    (100, 50, 10, [110, 0]),
])
def test_insufficient_stock(number, need, remaining, expected):
    """Tests cases where the rabbit wants more than what is available in stock."""
    assert eat(number, need, remaining) == expected

@pytest.mark.parametrize("number, need, remaining, expected", [
    (5, 10, 10, [15, 0]),
    (0, 0, 5, [0, 5]),
    (10, 0, 10, [10, 10]),
])
def test_exact_stock_and_zero_need(number, need, remaining, expected):
    """Tests cases where need equals remaining, or need is zero."""
    assert eat(number, need, remaining) == expected

@pytest.mark.parametrize("number, need, remaining, expected", [
    (0, 0, 0, [0, 0]),
    (10, 10, 0, [10, 0]),
    (0, 10, 0, [0, 0]),
    (5, 0, 0, [5, 0]),
])
def test_zero_scenarios(number, need, remaining, expected):
    """Tests edge cases involving zero values for various parameters."""
    assert eat(number, need, remaining) == expected

@pytest.mark.parametrize("number, need, remaining, expected", [
    (1000, 1000, 1000, [2000, 0]),
    (1000, 0, 1000, [1000, 1000]),
    (0, 1000, 1000, [1000, 0]),
    (1000, 1000, 0, [1000, 0]),
])
def test_max_constraints(number, need, remaining, expected):
    """Tests the upper boundary constraints of the function."""
    assert eat(number, need, remaining) == expected