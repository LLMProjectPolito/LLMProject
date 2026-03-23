import pytest
import math


# Focus: Boundary Values
import pytest

def list_sort(lst):
    """Sorts a list of strings based on length, with duplicates handled."""
    return sorted(lst, key=lambda x: (len(x), x))

# Focus: Type Scenarios
def list_sort(lst):
    """Sorts a list of strings based on length, then alphabetically."""
    return sorted(lst, key=lambda x: (len(x), x))

# Focus: Logic Branches
def list_sort(lst):
    """Sorts a list of strings based on length, then alphabetically."""
    return sorted(lst, key=lambda x: (len(x), x))