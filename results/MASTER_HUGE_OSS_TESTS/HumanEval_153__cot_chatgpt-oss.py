import pytest

# The function under test is assumed to be imported:
# from your_module import Strongest_Extension

def _strength(ext: str) -> int:
    """Helper to compute the expected strength (CAP - SM) for an extension."""
    caps = sum(1 for ch in ext if ch.isupper())
    lows = sum(1 for ch in ext if ch.islower())
    return caps - lows


@pytest.mark.parametrize(
    "class_name, extensions, expected",
    [
        # Basic example from the description
        (
            "Slices",
            ["SErviNGSliCes", "Cheese", "StuFfed"],
            "Slices.SErviNGSliCes",
        ),
        # Simple tie – first in list should win
        (
            "my_class",
            ["AA", "Be", "CC"],  # AA (2-0=2), Be (1-1=0), CC (2-0=2) -> tie AA vs CC, AA first
            "my_class.AA",
        ),
        # All lower case extensions (strength negative)
        (
            "lower",
            ["abc", "defg", "h"],
            "lower.abc",  # all have strength -len, abc is first
        ),
        # All upper case extensions (strength positive)
        (
            "UPPER",
            ["XYZ", "AB", "CDEFG"],
            "UPPER.CDEFG",  # CDEFG has highest strength 5
        ),
        # Mixed case with non‑alphabetic characters (they should be ignored)
        (
            "Mixed123",
            ["A1b2C3", "!!@@##", "Zz!"],
            "Mixed123.A1b2C3",  # strengths: A1b2C3 -> 2-2=0, !!@@## ->0, Zz! ->1-1=0; first wins
        ),
        # Single extension in list
        (
            "Solo",
            ["OnlyOne"],
            "Solo.OnlyOne",
        ),
        # Empty string extension (strength 0)
        (
            "EmptyExt",
            ["", "A", "b"],
            "EmptyExt.A",  # strengths: ""=0, "A"=1, "b"=-1 -> A strongest
        ),
        # Extensions with equal strength but later one has more characters (should still pick first)
        (
            "EqualStrength",
            ["Abc", "XyZ"],  # both have strength 0 (1 upper,2 lower vs 2 upper,1 lower)
            "EqualStrength.Abc",
        ),
    ],
)
def test_strongest_extension_basic(class_name, extensions, expected):
    """Test typical and edge‑case scenarios for Strongest_Extension."""
    assert Strongest_Extension(class_name, extensions) == expected


def test_strength_computation_matches_helper():
    """Cross‑validate that the function's chosen extension indeed has maximal strength."""
    class_name = "Validate"
    extensions = ["AaBb", "CCCC", "ddEE", "fG"]
    # Compute strengths using the helper
    strengths = [_strength(ext) for ext in extensions]
    max_strength = max(strengths)
    # Expected index is first occurrence of max_strength
    expected_index = strengths.index(max_strength)
    expected = f"{class_name}.{extensions[expected_index]}"
    assert Strongest_Extension(class_name, extensions) == expected


def test_tie_breaker_respects_original_order():
    """When multiple extensions share the highest strength, the first should be selected."""
    class_name = "TieBreaker"
    extensions = ["ABc", "Aab", "ABc"]  # strengths: 1, -1, 1 -> tie between first and last
    result = Strongest_Extension(class_name, extensions)
    assert result == "TieBreaker.ABc"  # first occurrence wins


def test_non_string_elements_raise_type_error():
    """Function should raise a TypeError if an extension is not a string."""
    class_name = "BadInput"
    extensions = ["Good", 123, "AlsoGood"]
    with pytest.raises(TypeError):
        Strongest_Extension(class_name, extensions)


def test_empty_extensions_list_behaviour():
    """Define expected behaviour when the extensions list is empty."""
    class_name = "NoExt"
    extensions = []
    # The specification does not define this case; we assume it returns just the class name.
    # Adjust the assertion if the actual implementation differs (e.g., raises an error).
    assert Strongest_Extension(class_name, extensions) == class_name