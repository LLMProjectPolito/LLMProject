
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

```python
import pytest
from typing import List

def do_algebra(operator: str, operand: List[int]) -> int:
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
    try:
        if len(operand) == 1:
            return operand[0]
        elif len(operator) == 1:
            return operator[0]
        else:
            return operator[0] * operand[1]
    except:
        return 0

def do_algebra(operator: str, operand: List[int]) -> int:
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
    try:
        if len(operand) == 1:
            return operand[0]
        elif len(operator) == 1:
            return operator[0]
        else:
            return operator[0] * operand[1]
    except:
        return 0

def test_do_algebra():
    assert do_algebra('+', '2') == 2
    assert do_algebra('-', '3') == 3
    assert do_algebra('*', '2') == 2
    assert do_algebra('/', '3') == 3
    assert do_algebra '-', '4' == 4
    assert do_algebra '*', '5' == 5
    assert do_algebra '-', '6' == 6
    assert do_algebra '/', '2' == 2
    assert do_algebra '*', '3' == 3
    assert do_algebra '/', '4' == 4
    assert do_algebra '-', '5' == 5
    assert do_algebra '*', '6' == 6
    assert do_algebra '/', '7' == 7
    assert do_algebra '-', '8' == 8
    assert do_algebra '*', '9' == 9
    assert do_algebra '/', '10' == 10
    assert do_algebra '-', '11' == 11
    assert do_algebra '*', '12' == 12
    assert do_algebra '/', '13' == 13
    assert do_algebra '-', '14' == 14
    assert do_algebra '*', '15' == 15
    assert do_algebra '/', '16' == 16
    assert do_algebra '-', '17' == 17
    assert do_algebra '*', '18' == 18
    assert do_algebra '/', '19' == 19
    assert do_algebra '-', '20' == 20
    assert do_algebra '*', '21' == 21
    assert do_algebra '/', '22' == 22
    assert do_algebra '-', '23' == 23
    assert do_algebra '*', '24' == 24
    assert do_algebra '/', '25' == 25
    assert do_algebra '-', '26' == 26
    assert do_algebra '*', '27' == 27
    assert do_algebra '/', '28' == 28
    assert do_algebra '-', '29' == 29
    assert do_algebra '*', '30' == 30
    assert do_algebra '/', '31' == 31
    assert do_algebra '-', '32' == 32
    assert do_algebra '*', '33' == 33
    assert do_algebra '/', '34' == 34
    assert do_algebra '-', '35' == 35
    assert do_algebra '*', '36' == 36
    assert do_algebra '/', '37' == 37
    assert do_algebra '-', '38' == 38
    assert do_algebra '*', '39' == 39
    assert do_algebra '/', '40' == 40
    assert do_algebra '-', '41' == 41
    assert do_algebra '*', '42' == 42
    assert do_algebra '/', '43' == 43
    assert do_algebra '-', '44' == 44
    assert do_algebra '*', '45' == 45
    assert do_algebra '/', '46' == 46
    assert do_algebra '-', '47' == 47
    assert do_algebra '*', '48' == 48
    assert do_algebra '/', '49' == 49
    assert do_algebra '-', '50' == 50
    assert do_algebra '*', '51' == 51
    assert do_algebra '/', '52' == 52
    assert do_algebra '-', '53' == 53
    assert do_algebra '*', '54' == 54
    assert do_algebra '/', '55' == 55
    assert do_algebra '-', '56' == 56
    assert do_algebra '*', '57' == 57
    assert do_algebra '/', '58' == 58
    assert do_algebra '-', '59' == 59
    assert do_algebra '*', '60' == 60
    assert do_algebra '/', '61' == 61
    assert do_algebra '-', '62' == 62
    assert do_algebra '*', '63' == 63
    assert do_algebra '/', '64' == 64
    assert do_algebra '-', '65' == 65
    assert do_algebra '*', '66' == 66
    assert do_algebra '/', '67' == 67
    assert do_algebra '-', '68' == 68
    assert do_algebra '*', '69' == 69
    assert do_algebra '/', '70' == 70
    assert do_algebra '-', '71' == 71
    assert do_algebra '*', '72' == 72
    assert do_algebra '/', '73' == 73
    assert do_algebra '-', '74' == 74
    assert do_algebra '*', '75' == 75
    assert do_algebra '/', '76' == 76
    assert do_algebra '-', '77' == 77
    assert do_algebra '*', '78' == 78
    assert do_algebra '/', '79' == 79
    assert do_algebra '-', '80' == 80
    assert do_algebra '*', '81' == 81
    assert do_algebra '/', '82' == 82
    assert do_algebra '-', '83' == 83
    assert do_algebra '*', '84' == 84
    assert do_algebra '/', '85' == 85
    assert do_algebra '-', '86' == 86
    assert do_algebra '*', '87' == 87
    assert do_algebra '/', '88' == 88
    assert do_algebra '-', '89' == 89
    assert do_algebra '*', '90' == 90
    assert do_algebra '/', '91' == 91
    assert do_algebra '-', '92' == 92