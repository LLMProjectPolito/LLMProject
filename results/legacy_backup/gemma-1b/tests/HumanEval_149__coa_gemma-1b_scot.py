import pytest
import math


# Focus: Boundary Values
import pytest

def list_sort(lst):
    """Sorts a list of strings based on their lengths, ensuring ascending order for shorter words and alphabetical order for longer words."""
    return sorted(lst, key=lambda x: (len(x), x))

# Focus: Type Scenarios
import pytest

def list_sort(lst):
    """Sorts a list of strings based on word length, ascending, and then alphabetically."""
    return sorted(lst, key=lambda x: (len(x), x))

# Focus: Logic Branches
import pytest

def list_sort(lst):
    """Sorts a list of strings based on length, then alphabetically."""
    return sorted(lst, key=lambda x: (len(x), x))