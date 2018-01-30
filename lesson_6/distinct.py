def solution(arr):
    """
    Args:
        arr (list): List of integers

    Returns:
        int: Number of distinct values in arr
    """
    return len(set(arr))


assert solution([2, 2, 1, 3, 1]) == 3
