import pytest
import math


# Focus: Boundary Values
def x_or_y(n, x, y):
    if n % 2 == 0:
        if x == n:
            return x
        else:
            return y
    else:
        return x

# Focus: Type Scenarios
def x_or_y(n, x, y):
    if n % 2 == 0:
        return x
    else:
        return y

# Focus: Logic Branches
def x_or_y(n, x, y):
    if n % 2 == 0:
        if x == n:
            return x
        else:
            return y
    else:
        return x