
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

# The function 'eat' is assumed to be imported from the source module.

@pytest.mark.parametrize("number, need, remaining, expected", [
    (5, 6, 10, [11, 4]),
    (4, 8, 9, [12, 1]),
    (1, 10, 10, [11, 0]),
    (2, 11, 5, [7, 0]),
])
def test_eat_provided_examples(number, need, remaining, expected):
    """Tests the specific examples provided in the problem description."""
    assert eat(number, need, remaining) == expected

@pytest.mark.parametrize("number, need, remaining, expected", [
    # Exact boundaries
    (0, 0, 0, [0, 0]),
    (1000, 1000, 1000, [2000, 0]),
    # Just inside boundaries (BVA)
    (999, 1, 1, [1000, 0]),
    (1, 999, 1000, [1000, 1]),
    # Zero-value logic
    (10, 0, 5, [10, 5]),    # Zero need
    (10, 5, 0, [10, 0]),    # Zero remaining
    (0, 5, 10, [5, 5]),     # Zero already eaten
])
def test_eat_boundary_values(number, need, remaining, expected):
    """Tests the boundary constraints (0 and 1000) and inclusive limits."""
    assert eat(number, need, remaining) == expected

@pytest.mark.parametrize("number, need, remaining", [
    # Below lower boundary
    (-1, 5, 10),
    (5, -1, 10),
    (5, 5, -1),
    (-100, -100, -100),
    # Above upper boundary
    (1001, 5, 10),
    (5, 1001, 10),
    (5, 5, 1001),
    (1001, 1001, 1001),
])
def test_eat_out_of_range_raises_error(number, need, remaining):
    """Verifies that inputs outside the 0-1000 range raise a ValueError."""
    with pytest.raises(ValueError):
        eat(number, need, remaining)

@pytest.mark.parametrize("number, need, remaining", [
    (5.5, 6, 10),
    (5, 6.0, 10),
    (5, 6, 10.5),
    ("5", 6, 10),
    (5, None, 10),
])
def test_eat_non_integer_inputs(number, need, remaining):
    """Verifies that non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        eat(number, need, remaining)