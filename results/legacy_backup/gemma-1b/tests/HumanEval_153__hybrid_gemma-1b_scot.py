import pytest
from typing import List

def Strongest_Extension(class_name: str, extensions: List[str]) -> str:
    """
    Finds the strongest extension from a list of extensions.

    Args:
        class_name: The name of the class.
        extensions: A list of extensions.

    Returns:
        The name of the strongest extension.
    """
    strongest_extension = None
    max_strength = -1

    for extension in extensions:
        uppercase_count = 0
        lowercase_count = 0
        for char in extension:
            if char.isupper():
                uppercase_count += 1
            else:
                lowercase_count += 1

        strength = uppercase_count - lowercase_count

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return strongest_extension