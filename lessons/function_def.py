"""Ex of Function Definition."""

def my_max(a: int, b: int) -> int:
    """Returns largest argument. """
    if a>= b:
        return a
    else: 
        return b
print(my_max(10 + 1, 10))
print(my_max(-50, 100))
