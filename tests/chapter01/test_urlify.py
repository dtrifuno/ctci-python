from typing import Tuple

import pytest
from ctci_python.chapter01.urlify import urlify


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (("Donbas", 6), "Donbas"),
        (("Mr. John Smith", 18), "Mr.%20John%20Smith"),
        (("Debit card", 12), "Debit%20card"),
        (("Hm, fjord waltz", 19), "Hm,%20fjord%20waltz"),
    ],
)
def test_is_permutation(test_input: Tuple[str, int], expected: str):
    assert urlify(*test_input) == expected
