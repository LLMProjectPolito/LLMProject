import pytest

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
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '//':
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
    return result
### SCoT Steps:
### STEP 1: REASONING
### The function `do_algebra` takes a list of operators and a list of operands and evaluates a mathematical expression.
### The expression is built by applying the operators to the operands in sequence.
### The tests should cover various operator combinations, operand values, and edge cases.
### We need to test addition, subtraction, multiplication, floor division, and exponentiation.
### We also need to test cases with different operand lengths and operator lengths.
### STEP 2: PLAN
### Test cases:
### 1. Basic addition
### 2. Basic subtraction
### 3. Basic multiplication
### 4. Basic floor division
### 5. Basic exponentiation
### 6. Combination of operators
### 7. Edge cases: operand and operator lists of length 2
### 8. Edge cases: operand and operator lists of length 3
### 9. Edge cases: operand list with a single element
### 10. Edge cases: operator list with a single element
### STEP 3: CODE
###