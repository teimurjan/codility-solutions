import math


def solution(x, y, d):
    """
    Args:
        x (int): position X
        y (int): position Y
        d (int): distance

    Returns:
        int: minimal number of jumps to exceed Y
    """
    return math.ceil((y - x) / d)


assert solution(10, 85, 30) == 3
