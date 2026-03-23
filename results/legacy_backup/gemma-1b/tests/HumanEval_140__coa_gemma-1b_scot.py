import pytest
import math


# Focus: Boundary Values
import pytest

def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    """
    while "  " in text:
        text = text.replace("  ", "-")
    while "  " in text:
        text = text.replace("  ", "-")
    return text

# Focus: Type Scenarios
import pytest

def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    """
    while "  " in text:
        text = text.replace("  ", "-")
    while "  " in text:
        text = text.replace("  ", "-")
    return text

# Focus: Logic Branches
import pytest

def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    """
    while "  " in text:
        text = text.replace("  ", "_")
    while "  " in text:
        text = text.replace("  ", "-")
    return text