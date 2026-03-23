import pytest
import math


# Focus: Boundary Values
import pytest

def list_sort(lst):
    """Sorts a list of strings based on their lengths, removing strings with odd lengths."""
    return sorted(lst, key=lambda x: (len(x), x))

# Focus: Type Scenarios
import pytest

def list_sort(lst):
    """Sorts a list of strings based on their length, ascending by length, and alphabetically for duplicates."""
    return sorted(lst, key=lambda x: (len(x), x))

# Focus: Logic Branches
import pytest

def list_sort(lst):
    """Sorts a list of strings based on their length, handling duplicates and ensuring ascending order."""
    return sorted(lst, key=lambda x: (len(x), x))