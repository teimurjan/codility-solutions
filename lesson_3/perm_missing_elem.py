def solution(arr):
    """
    Args:
        arr (list): List of consecutive integer with one miss

    Returns:
        int: Missed integer
    """
    n = len(arr) + 1
    return int((n * (n + 1)) / 2 - sum(arr))


assert solution([2, 3, 1, 5]) == 4
