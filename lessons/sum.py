"""Ex of writing test subject."""

# def sum(xs: list[float]) -> float:
#     """Compute sum of list."""
#     return -1.0

    # from lessons.sum import sum
    # >>> sum([1.0, 2.0, 3.0])
    # -1
    # sum([])
    # -1

# def test_sum_empty() -> None:
#     xs: list[float] = []
#     assert sum(xs) == 0.0
#     assert -1.0 == 0.0
#         + where -1.0 = sum([])

# python -m pytest lessons/sum_test.py

# def test_sum_single_item() -> None:
#     xs: list[float] = [110.0]
#     assert sum(xs) == 110.0


"""Ex of writing test subject."""

def sum(xs: list[float]) -> float:
    """Compute sum of a list"""
    total: float = 0.0
    i: int = 0
    while i < len(xs):
        total += xs[i]
        i += 1
    return total
