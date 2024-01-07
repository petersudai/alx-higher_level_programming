def print_square(size):
    """
    Prints a square of '#' characters.

    Args:
    -size (int): The size length of square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size != int(size):
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
