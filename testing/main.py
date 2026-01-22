def add(x: int, y: int) -> int:
    """Adds together to integers."""
    if not all(isinstance(val, int) for val in [x, y]):
        raise TypeError

    return x+y
