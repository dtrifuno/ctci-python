from typing import Tuple

import pytest
from ctci_python.chapter05.insertion import insertion


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ((0b1000_0000_0000, 0b_1_0011, 2, 6), 0b_1000_0100_1100),
        ((0b10_0111_1100_1111, 0b_1111, 4, 7), 0b10_0111_1111_1111),
        ((0, 0b_1001, 1, 4), 0b1_0010),
        ((0b_1111_1111, 0b0000, 2, 5), 0b1100_0011),
    ],
)
def test_insertion(test_input: Tuple[int, int, int, int], expected: bool):
    assert insertion(*test_input) == expected
