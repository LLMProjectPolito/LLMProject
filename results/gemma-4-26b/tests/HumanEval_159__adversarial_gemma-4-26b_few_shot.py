
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

# The function to be tested
def eat(number, need, remaining):
    """
    Implementation placeholder (The actual implementation would be provided)
    """
    # Logic: 
    # amount_to_eat = min(need, remaining)
    # total_eaten = number + amount_to_eat
    # carrots_left = remaining - amount_to_eat
    # return [total_eaten, carrots_left]
    pass

@pytest.mark.parametrize("number, need, remaining, expected", [
    # --- Provided Examples (Sanity Checks) ---
    (5, 6, 10, [11, 4]),
    (4, 8, 9, [12, 1]),
    (1, 10, 10, [11, 0]),
    (2, 11, 5, [7, 0]),

    # --- Boundary Case: Zero Values ---
    (0, 0, 0, [0, 0]),      # Everything is zero
    (0, 5, 0, [0, 0]),      # Need carrots, but none in stock
    (5, 0, 10, [5, 10]),    # Need nothing, stock remains untouched
    (0, 0, 10, [0, 10]),    # Already eaten 0, need 0, 10 left

    # --- Boundary Case: Exact Matches ---
    (5, 5, 5, [10, 0]),     # Need exactly what is in stock
    (5, 5, 10, [10, 5]),    # Need exactly what is in stock, but more exists
    (5, 10, 10, [15, 0]),   # Need exactly what is in stock (total eaten = 5+10)

    # --- Boundary Case: Insufficient Stock (The "Hungry" Logic) ---
    (10, 100, 1, [11, 0]),  # Need a lot, only 1 available
    (10, 100, 99, [109, 0]),# Need a lot, almost enough available
    (10, 1, 0, [10, 0]),    # Need 1, but 0 available

    # --- Boundary Case: Maximum Constraints (1000) ---
    (1000, 1000, 1000, [2000, 0]),
    (1000, 0, 1000, [1000, 1000]),
    (0, 1000, 1000, [1000, 0]),
    (1000, 1000, 0, [1000, 0]),
])
def test_eat_logic(number, need, remaining, expected):
    """
    Tests various scenarios including provided examples, zero boundaries, 
    exact stock matches, insufficient stock, and maximum constraints.
    """
    assert eat(number, need, remaining) == expected

def test_eat_type_safety():
    """
    Blue Team Note: While the prompt implies integers, a robust system 
    should be checked for unexpected types if not strictly enforced by a type checker.
    """
    with pytest.raises(TypeError):
        # This test assumes the implementation doesn't handle non-integers
        eat("5", 6, 10)

def test_eat_negative_values():
    """
    Blue Team Note: The constraints say 0 <= x <= 1000. 
    We test how the function behaves if constraints are violated.
    """
    # If the function is strictly following constraints, 
    # it might raise an error or handle it gracefully.
    # Here we test if it handles negative 'remaining' logically (though invalid per constraints)
    # This is to see if the developer used 'abs()' or if it breaks.
    result = eat(5, 5, -1)
    # A robust implementation should ideally not allow negative stock, 
    # but we check for logical consistency.
    assert result[1] >= 0