
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

def test_eat_provided_examples():
    """Tests the examples provided in the docstring to ensure basic functionality."""
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]
    assert eat(2, 11, 5) == [7, 0]

@pytest.mark.parametrize("number, need, remaining, expected", [
    # Case: Sufficient carrots (remaining > need)
    (10, 5, 10, [15, 5]),
    # Case: Exact carrots (remaining == need)
    (10, 5, 5, [15, 0]),
    # Case: Insufficient carrots (remaining < need)
    (10, 5, 2, [12, 0]),
    # Case: No carrots remaining in stock
    (10, 5, 0, [10, 0]),
    # Case: No carrots needed
    (10, 0, 10, [10, 10]),
    # Case: No carrots already eaten
    (0, 5, 10, [5, 5]),
    # Case: Everything is zero
    (0, 0, 0, [0, 0]),
])
def test_eat_edge_cases(number, need, remaining, expected):
    """Tests various edge cases including zeros and boundary conditions."""
    assert eat(number, need, remaining) == expected

@pytest.mark.parametrize("number, need, remaining, expected", [
    # Max constraints: 1000, 1000, 1000
    (1000, 1000, 1000, [2000, 0]),
    (1000, 1000, 0, [1000, 0]),
    (0, 1000, 1000, [1000, 0]),
    (1000, 0, 1000, [1000, 1000]),
])
def test_eat_boundaries(number, need, remaining, expected):
    """Tests the upper boundary constraints (1000)."""
    assert eat(number, need, remaining) == expected

def test_eat_return_type():
    """Ensures the function returns a list of integers as specified."""
    result = eat(1, 1, 1)
    assert isinstance(result, list), "The function should return a list"
    assert len(result) == 2, "The list should contain exactly two elements"
    assert all(isinstance(x, int) for x in result), "All elements in the list should be integers"