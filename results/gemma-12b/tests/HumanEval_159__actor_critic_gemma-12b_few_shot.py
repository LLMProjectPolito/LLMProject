
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
    total_eaten = number
    left = remaining
    
    if remaining >= need:
        total_eaten += need
        left -= need
    else:
        total_eaten += remaining
        left = 0
        
    return [total_eaten, left]


def test_eat_basic():
    assert eat(5, 6, 10) == [11, 4]

def test_eat_need_exceeds_remaining():
    assert eat(4, 8, 9) == [12, 1]

def test_eat_exact_need():
    assert eat(1, 10, 10) == [11, 0]

def test_eat_remaining_less_than_need():
    assert eat(2, 11, 5) == [7, 0]

def test_eat_no_remaining():
    assert eat(3, 5, 0) == [3, 0]

def test_eat_zero_need():
    assert eat(7, 0, 12) == [7, 12]

def test_eat_zero_initial_eaten():
    assert eat(0, 5, 10) == [5, 5]

def test_eat_zero_remaining():
    assert eat(5, 6, 0) == [5, 0]

def test_eat_all_zeros():
    assert eat(0, 0, 0) == [0, 0]

def test_eat_large_numbers():
    assert eat(999, 999, 999) == [1998, 0]

def test_eat_large_numbers_need_greater():
    assert eat(100, 500, 400) == [600, 0]

def test_eat_need_much_greater():
    assert eat(999, 1000, 1) == [1000, 0]

def test_eat_number_equals_need():
    assert eat(5, 5, 10) == [10, 5]

def test_eat_need_significantly_greater():
    assert eat(100, 1000, 1000) == [2000, 0]

def test_eat_negative_remaining():
    assert eat(5, 6, -1) == [4, -1]  # Or raise an exception, depending on desired behavior

def test_eat_need_is_zero():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_need_equals_remaining_plus_one():
    assert eat(2, 5, 4) == [6, 0]

def test_eat_number_greater_than_need():
    assert eat(6, 5, 10) == [11, 5]