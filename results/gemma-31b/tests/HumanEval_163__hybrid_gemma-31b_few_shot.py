
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

def generate_integers(a: int, b: int) -> list[int]:
    """ 
    Returns a list of even single-digit integers (2, 4, 6, 8) that fall 
    within the inclusive range between a and b, sorted in ascending order.
    """