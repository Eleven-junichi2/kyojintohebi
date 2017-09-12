import random

def dice(repeat = 1):
    """

    Args:
        repeat(int):

    Returns:
        value(int):
    """
    value = 0
    for i in range(repeat):
        value = value + random.randint(1, 6)
    return value