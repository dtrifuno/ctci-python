import pytest
from ctci_python.chapter01.palindrome_permutation import is_palindrome_permutation


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("Tact Coa", True),
        ("A man, a plan, a canal - Panama!", True),
        ("Batman", False),
        ("Palindrome", False),
    ],
)
def test_is_palindrome_permutation(test_input: str, expected: bool):
    assert is_palindrome_permutation(test_input) == expected
