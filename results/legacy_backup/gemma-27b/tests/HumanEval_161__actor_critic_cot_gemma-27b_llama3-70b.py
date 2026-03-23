import pytest

@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("", ""),
        ("1234", "4321"),
        ("!@#$", "$#@!"),
        ("abc", "ABC"),
        ("ABC", "abc"),
        ("aBc", "AbC"),
        ("a1b2c", "A1B2C"),
        ("a!b@c#", "A!B@C#"),
        ("a1B!c2", "A1b!C2"),
        ("  abc  ", "  ABC  "),
        ("你好世界", "界世好你"),
        ("1你好2", "2好你1"),
        ("a", "A"),
        ("1", "1"),
        ("!", "!"),
        ("#a@C", "#A@c"),
        ("ß", "SS"),  # Test non-ASCII character
        ("\n", "\n"),  # Test newline character
        ("a\nb", "A\nB"), # Test newline with letters
        ("1\n2", "2\n1"), # Test newline with numbers
        ("a" * 1000, "A" * 1000),  # Test long string
        (None, None), # Test None input
        ([], ""), # Test empty list
        ((), ""), # Test empty tuple
        ({}, ""), # Test empty dictionary
        ("\t", "\t"), # Test tab character
        ("\r", "\r"), # Test carriage return character
        ("\b", "\b"), # Test backspace character
        ("\v", "\v"), # Test vertical tab character
        ("\f", "\f"), # Test form feed character
        ("\\", "\\"), # Test escape character
        ("\u0041", "\u0041"), # Test Unicode escape sequence
        ("a" * 10000, "A" * 10000), # Test very long string
        (b"abc", b"cba"), # Test bytes input
        (bytearray(b"abc"), b"cba"), # Test bytearray input
    ],
)
def test_reverse_and_swap_case(input_string, expected_output):
    """
    Tests the reverse_and_swap_case function with various inputs.
    """
    if input_string is None:
        assert solve(input_string) is None
    else:
        assert solve(input_string) == expected_output