"""Test, For EX05 List Utility Functions."""


__author__ = 730238845


from utils import only_evens, sub, concat


# Only_Evens
def test_only_evens_empty() -> None:
    """Edge: testing sub function with empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_even_and_odd() -> None:
    """Use: testing function with even and odd numbers."""
    xs: list[int] = [2, 3, 4, 5]
    assert only_evens(xs) == [2, 4]


def test_only_evens_odds() -> None:
    """Use: testing function with odd numbers."""
    xs: list[int] = [1, 3, 5, 9]
    assert only_evens(xs) == []


def test_only_evens_evens() -> None:
    """Use: testing function with even numbers."""
    xs: list[int] = [2, 4, 6, 8]
    assert only_evens(xs) == [2, 4, 6, 8]


# Sub
def test_sub_empty() -> None:
    """Edge: testing sub function with empty list."""
    original_list: list[int] = []
    start: int = 0
    end: int = 0
    assert sub(original_list, start, end) == []


def test_sub_one() -> None:
    """Use: testing sub function with a working list."""
    original_list: list[int] = [12, 13, 14, 15]
    start: int = 0
    end: int = 3
    assert sub(original_list, start, end) == [12, 13, 14]


def test_sub_two() -> None:
    """Use: testing sub function."""
    original_list: list[int] = [20, 30, 40, 50]
    start: int = 0
    end: int = 3
    assert sub(original_list, start, end) == [20, 30, 40]


def test_sub_three() -> None:
    """Use: testing sub function."""
    original_list: list[int] = [21, 22, 23, 24]
    start: int = 0
    end: int = 2
    assert sub(original_list, start, end) == [21, 22]


# Concat
def test_concat_empty() -> None:
    """Edge: testing concat function with empty list."""
    list1: list[int] = []
    list2: list[int] = []
    assert concat(list1, list2) == []


def test_concat_one() -> None:
    """Use: testing concat function with a working list."""
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [4, 5, 6]
    assert concat(list1, list2) == [1, 2, 3, 4, 5, 6]


def test_concat_two() -> None:
    """Use: testing concat function with a working list."""
    list1: list[int] = [1, 2, 3]
    list2: list[int] = [1, 2, 3]
    assert concat(list1, list2) == [1, 2, 3, 1, 2, 3]


def test_concat_three() -> None:
    """Use: testing concat function with a working list."""
    list1: list[int] = [1]
    list2: list[int] = [3]
    assert concat(list1, list2) == [1, 3]