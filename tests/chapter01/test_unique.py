import pytest
from ctci_python.chapter01.unique import is_unique_v1, is_unique_v2


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("Jocknymphswaqfdrugvexblitz", True),
        ("Bandobur", True),
        ("banana", False),
        ("Hm, fjord waltz", False),
    ],
)
def test_is_unique_v1(test_input: str, expected: bool):
    assert is_unique_v1(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("Jocknymphswaqfdrugvexblitz", True),
        ("Bandobur", True),
        ("banana", False),
        ("Hm, fjord waltz", False),
    ],
)
def test_is_unique_v2(test_input: str, expected: bool):
    assert is_unique_v2(test_input) == expected
