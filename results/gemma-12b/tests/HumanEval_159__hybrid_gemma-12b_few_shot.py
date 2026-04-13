
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
    total_eaten = number
    left = remaining
    
    if remaining >= need:
        total_eaten += need
        left -= need
    else:
        total_eaten += remaining
        left = 0
        
    return [total_eaten, left]

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


@pytest.mark.parametrize(
    "number, need, remaining, expected",
    [
        (5, 6, 10, [11, 4]),
        (4, 8, 9, [12, 1]),
        (1, 10, 10, [11, 0]),
        (2, 11, 5, [7, 0]),
        (0, 5, 5, [5, 0]),
        (0, 5, 0, [0, 0]),
        (1000, 1000, 1000, [2000, 0]),
        (0, 0, 0, [0, 0]),
        (1000, 0, 1000, [1000, 1000]),
        (0, 1000, 0, [0, 0]),
        (500, 501, 500, [1001, 0]),
        (1, 1, 1, [2, 0]),
        (1, 2, 1, [2, 0]),
        (2, 1, 1, [3, 0]),
        (999, 999, 999, [1998, 0]),
        (500, 500, 500, [1000, 0]),
    ],
)
def test_eat_various_scenarios(number, need, remaining, expected):
    assert eat(number, need, remaining) == expected

def test_eat_edge_cases():
    assert eat(1000, 1000, 1000) == [2000, 0]
    assert eat(0, 0, 0) == [0, 0]
    assert eat(1000, 0, 1000) == [1000, 1000]
    assert eat(0, 1000, 0) == [0, 0]

def test_eat_zero_need():
    assert eat(5, 0, 10) == [5, 10]

def test_eat_zero_remaining():
    assert eat(5, 6, 0) == [5, 0]


def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None