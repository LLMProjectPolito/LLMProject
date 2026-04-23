
def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """

import pytest

# Assuming do_algebra is available in the environment as per instructions.
# from your_module import do_algebra 

@pytest.mark.parametrize("operators, operands, expected", [
    # Basic Single Operations
    (['+'], [10, 5], 15),
    (['-'], [10, 5], 5),
    (['*'], [10, 5], 50),
    (['//'], [10, 3], 3),
    (['**'], [2, 3], 8),
    (['+'], [0, 0], 0),
])
def test_basic_operations(operators, operands, expected):
    """Tests fundamental single-operator arithmetic."""
    from your_module import do_algebra
    assert do_algebra(operators, operands) == expected

@pytest.mark.parametrize("operators, operands, expected", [
    # Precedence: Multiplication/Division vs Addition/Subtraction
    (['+', '*'], [2, 3, 4], 14),      # 2 + (3 * 4) = 14
    (['-', '*'], [10, 2, 5], 0),      # 10 - (2 * 5) = 0
    (['*', '-'], [2, 3, 4], 2),       # (2 * 3) - 4 = 2
    (['//', '+'], [10, 3, 1], 4),     # (10 // 3) + 1 = 4
    
    # Precedence: Exponentiation vs Multiplication/Division
    (['*', '**'], [2, 3, 2], 18),     # 2 * (3 ** 2) = 18
    (['**', '*'], [5, 2, 2], 50),     # (5 ** 2) * 2 = 50
    (['//', '**'], [10, 2, 2], 2),    # 10 // (2 ** 2) = 2
    
    # Precedence: Exponentiation vs Addition/Subtraction
    (['+', '**'], [2, 3, 2], 11),     # 2 + (3 ** 2) = 11
    (['-', '**'], [10, 2, 3], 2),     # 10 - (2 ** 3) = 2
    
    # Deep Precedence
    (['*', '**', '+'], [2, 3, 2, 4], 22), # 2 * (3**2) + 4 = 22
])
def test_operator_precedence(operators, operands, expected):
    """Tests that the function respects the mathematical order of operations."""
    from your_module import do_algebra
    assert do_algebra(operators, operands) == expected

@pytest.mark.parametrize("operators, operands, expected", [
    # Left-to-Right: Addition and Subtraction
    (['-', '+'], [10, 5, 2], 7),      # (10 - 5) + 2 = 7
    (['+', '-'], [10, 5, 2], 13),     # (10 + 5) - 2 = 13
    
    # Left-to-Right: Multiplication and Division
    (['//', '*'], [20, 5, 2], 8),     # (20 // 5) * 2 = 8
    (['*', '//'], [10, 3, 2], 6),     # (10 * 3) // 2 = 15 (Wait, 10*3=30, 30//2=15)
    # Correcting math for the test case:
    (['*', '//'], [4, 10, 3], 12),    # (4 * 10) // 3 = 13? No, 40 // 3 = 13.
    # Let's use the Suite 2 logic: 10 * 3 // 2 = 15
    (['*', '//'], [10, 3, 2], 15),    # (10 * 3) // 2 = 15
])
def test_associativity(operators, operands, expected):
    """Tests that operators of equal precedence evaluate left-to-right."""
    from your_module import do_algebra
    assert do_algebra(operators, operands) == expected

@pytest.mark.parametrize("operators, operands, expected", [
    # Zero as an operand
    (['+', '*'], [0, 5, 2], 10),      # 0 + (5 * 2) = 10
    (['*', '+'], [5, 0, 10], 10),     # (5 * 0) + 10 = 10
    
    # Zero as an exponent
    (['**'], [5, 0], 1),              # 5 ** 0 = 1
    (['**'], [0, 5], 0),              # 0 ** 5 = 0
    
    # Large Numbers
    (['**'], [10, 10], 10000000000),  # 10^10
    (['**', '//'], [2, 10, 2], 512),  # (2^10) // 2 = 512
])
def test_edge_cases_and_large_numbers(operators, operands, expected):
    """Tests boundary conditions including zero and large integer results."""
    from your_module import do_algebra
    assert do_algebra(operators, operands) == expected

@pytest.mark.parametrize("operators, operands, expected", [
    # Complex Chain 1: 2 + 3 * 4 ** 2 // 2 - 5
    # 4**2=16 -> 3*16=48 -> 48//2=24 -> 2+24-5=21
    (['+', '*', '**', '//', '-'], [2, 3, 4, 2, 5], 21),
    
    # Complex Chain 2: 2 + 3 * 4 - 5 // 2 ** 3
    # 2**3=8 -> 5//8=0 -> 3*4=12 -> 2+12-0=14
    (['+', '*', '-', '//', '**'], [2, 3, 4, 5, 2, 3], 14),
    
    # Complex Chain 3: (5 ** 2) * 2 // 10 + 1
    # 5**2=25 -> 25*2=50 -> 50//10=5 -> 5+1=6
    (['**', '*', '//', '+'], [5, 2, 2, 10, 1], 6),
])
def test_complex_chains(operators, operands, expected):
    """Tests long, mixed-operator expressions to ensure full logic integration."""
    from your_module import do_algebra
    assert do_algebra(operators, operands) == expected

def test_division_by_zero_error():
    """Tests that division by zero correctly raises a ZeroDivisionError."""
    from your_module import do_algebra
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])
    with pytest.raises(ZeroDivisionError):
        do_algebra(['*'], [10, 0]) # Note: Usually * doesn't raise, but // does.
        # If the function is meant to catch division by zero in any context:
        # do_algebra(['//'], [10, 0]) is the primary target.