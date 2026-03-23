import pytest
import math

def strongest_extension():
    """
    Determines the extension with the highest strength.
    """
    rules = [
        "Output ONLY valid code. Ensure necessary imports (pytest, math) are at the top.",
        "DO NOT RE-DEFINE the function under test.",
        "DO NOT use placeholder imports. Assume function is in scope.",
    ]
    extensions = [
        "abc",
        "def",
        "ghi",
        "jkl",
        "mno",
        "pqr",
        "stu",
        "vwx",
        "yz",
    ]

    for extension in extensions:
        uppercase_count = 0
        lowercase_count = 0
        for char in extension:
            if 'A' <= char <= 'Z':
                uppercase_count += 1
            elif 'a' <= char <= 'z':
                lowercase_count += 1

        strength = uppercase_count - lowercase_count
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return strongest_extension

def test_strongest_extension():
    assert strongest_extension() == "ghi"