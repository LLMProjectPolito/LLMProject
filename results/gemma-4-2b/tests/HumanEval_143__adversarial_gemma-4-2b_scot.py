
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """

**STEP 1: REASONING**

The function `words_in_sentence` aims to extract words from a sentence whose lengths are prime numbers.  We need to consider various scenarios:

*   **Empty sentence:**  The input sentence should be empty.
*   **Single word:** The sentence should contain only one word.
*   **Multiple words:** The sentence should contain multiple words.
*   **Words with different lengths:**  Test with words of varying lengths, including those that are prime and those that are not.
*   **Prime number check:**  Verify that the prime number check is accurate.
*   **Order preservation:** Ensure the order of the selected words is maintained.
*   **Edge cases:** Test with sentences containing only spaces or special characters (although the problem statement specifies only letters).

**STEP 2: PLAN**


1.  `test_empty_sentence`: Test with an empty string.
2.  `test_single_word`: Test with a sentence containing a single word.
3.  `test_multiple_words_prime`: Test with multiple words where all lengths are prime.
4.  `test_multiple_words_non_prime`: Test with multiple words where some lengths are not prime.
5.  `test_mixed_words`: Test with a mix of prime and non-prime length words.
6.  `test_long_sentence`: Test with a longer sentence to check for performance and correctness.
7.  `test_sentence_with_spaces`: Test with a sentence containing spaces.
8.  `test_sentence_with_special_characters`: Test with a sentence containing special characters (although the problem statement specifies only letters).

**STEP 3: CODE**

```python
import pytest
from typing import List

def is_prime(n: int) -> bool:
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def words_in_sentence(sentence: str) -> str:
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    words = sentence.split()
    result = ""
    for word in words:
        if is_prime(len(word)):
            result += word + " "
    return result.strip()


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("", ""),
        ("a", "a"),
        ("This is a test", "is"),
        ("lets go for swimming", "go for"),
        ("This is a test sentence", "is"),
        ("a b c d e", "a"),
        ("a b c d e f", "a"),
        ("a b c d e f g", "a"),
        ("a b c d e f g h", "a"),
        ("a b c d e f g h i", "a"),
        ("a b c d e f g h i j", "a"),
        ("a b c d e f g h i j k", "a"),
        ("a b c d e f g h i j k l", "a"),
        ("a b c d e f g h i j k l m", "a"),
        ("a b c d e f g h i j k l m n", "a"),
        ("a b c d e f g h i j k l m n o", "a"),
        ("a b c d e f g h i j k l m n o p", "a"),
        ("a b c d e f g h i j k l m n o p q", "a"),
        ("a b c d e f g h i j k l m n o p q r", "a"),
        ("a b c d e f g h i j k l m n o p q r s", "a"),
        ("a b c d e f g h i j k l m n o p q r s t", "a"),
        ("a b c d e f g h i j k l m n o p q r s t u", "a"),
        ("a b c d e f g h i j k l m n o p q r s t u v", "a"),
        ("a b c d e f g h i j k l m n o p q r s t u v w", "a"),
        ("a b c d e f g h i j k l m n o p q r s t u v w x", "a"),
        ("a b c d e f g h i j k l m n o p q r s t u v w x y", "a"),
        ("a b c d e f g h i j k l m n o p q r s t u v w x y z", "a"),
        ("This is a very long sentence with many words", "is"),
        ("a b c d e f g h i j k l m n o p q r s t u v w x y z a", "a"),
        ("a b c d e f g h i j k l m n o p q r s t u v w x y z a b", "a"),
        ("a b c d e f g h i j k l m n o p q r s t u v w x y z a b c", "a"),
        ("a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d", "a"),
    ],
)
def test_words_in_sentence(sentence: str, expected: str):
    assert words_in_sentence(sentence) == expected

@pytest.mark.parametrize(
    "sentence, expected",
    [
        "This is a test sentence with spaces",
        "is",
    ],
)
def test_sentence_with_spaces(sentence: str, expected: str):
    assert words_in_sentence(sentence) == expected

@pytest.mark.parametrize(
    "sentence, expected",
    [
        "a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x y z a b c d e f g h i j k l m n o p q r s t u v w x