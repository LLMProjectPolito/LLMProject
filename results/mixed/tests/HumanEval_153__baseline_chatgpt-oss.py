import copy
import pytest

# Import the function under test.
# Adjust the import path if the implementation lives in a different module.
from solution import Strongest_Extension


@pytest.mark.parametrize(
    "class_name, extensions, expected",
    [
        # Example from the docstring
        (
            "Slices",
            ["SErviNGSliCes", "Cheese", "StuFfed"],
            "Slices.SErviNGSliCes",
        ),
        # Simple case – first element is strongest
        ("my_class", ["AA", "Be", "CC"], "my_class.AA"),
        # Tie on strength – first in list wins
        ("TieTest", ["Abc", "aBC"], "TieTest.AbC"),
        # All‑uppercase extension (max positive strength)
        ("Upper", ["XYZ", "ab"], "Upper.XYZ"),
        # All‑lowercase extension (max negative strength)
        ("Lower", ["abc", "XYZ"], "Lower.XYZ"),
        # Zero strength (CAP == SM) – should still be selected if it is the strongest
        ("Zero", ["Ab", "aB"], "Zero.Ab"),
        # Single extension – always chosen
        ("Solo", ["OnlyOne"], "Solo.OnlyOne"),
        # Empty string as an extension (strength 0)
        ("EmptyExt", ["", "A"], "EmptyExt.A"),
    ],
)
def test_strongest_extension_basic(class_name, extensions, expected):
    """
    Verify that Strongest_Extension returns the correct
    `<ClassName>.<StrongestExtension>` string for a variety of inputs.
    """
    # Keep a copy to ensure the function does not mutate the original list.
    original = copy.deepcopy(extensions)

    result = Strongest_Extension(class_name, extensions)

    assert result == expected
    # The input list must remain unchanged.
    assert extensions == original


def test_strength_calculation_directly():
    """
    Helper test that checks the internal strength calculation logic
    by calling the function with crafted inputs where the expected
    strength can be computed manually.
    """
    # Helper to compute strength manually
    def strength(name: str) -> int:
        caps = sum(1 for c in name if c.isupper())
        lows = sum(1 for c in name if c.islower())
        return caps - lows

    # Create a list where strengths are known and ordered descending.
    extensions = ["AAA", "AaA", "aAa", "aaa"]
    strengths = [strength(e) for e in extensions]
    # Verify that the strengths are indeed decreasing.
    assert strengths == sorted(strengths, reverse=True)

    # The strongest (first) should be returned.
    assert Strongest_Extension("Test", extensions) == "Test.AAA"


def test_invalid_inputs():
    """
    The function is expected to work with strings and a list of strings.
    Supplying a non‑list for `extensions` or non‑string elements should raise
    a TypeError. The exact exception type is not defined in the spec, but
    a TypeError is the most sensible default.
    """
    with pytest.raises(TypeError):
        Strongest_Extension("Cls", "not a list")  # type: ignore[arg-type]

    with pytest.raises(TypeError):
        Strongest_Extension("Cls", [123, "Valid"])  # type: ignore[arg-type]

    with pytest.raises(TypeError):
        Strongest_Extension(123, ["A"])  # type: ignore[arg-type]


def test_empty_extensions_list():
    """
    Behaviour for an empty extensions list is not defined in the original
    specification. The implementation should raise a ValueError (or a
    custom exception) rather than returning an invalid string.
    """
    with pytest.raises(ValueError):
        Strongest_Extension("Empty", [])