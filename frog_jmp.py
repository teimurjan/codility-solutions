import math


def solution(x, y, D):
    """
    Args:
        x (int): position X
        y (int): position Y
        D (int): distance

    Returns:
        int: minimal number of jumps to exceed Y
    """
    return math.ceil((y - x) / D)


assert solution(10, 85, 30) == 3
