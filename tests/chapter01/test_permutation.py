from typing import Tuple

import pytest
from ctci_python.chapter01.permutation import is_permutation


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (("Banana", "ananab"), False),
        (("astronomer", "moonstarer"), True),
        (("debit card", "bad credit"), True),
        (("Hm, fjord waltz", "Hmfjordwaltz, "), False),
    ],
)
def test_is_permutation(test_input: Tuple[str, str], expected: bool):
    assert is_permutation(*test_input) == expected
