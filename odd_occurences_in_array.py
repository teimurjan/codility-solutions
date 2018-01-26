def solution(arr):
    """
    Args:
        arr (list): List of odd numbers

    Returns:
        int: The number occurs once in a list
    """
    result = 0
    for number in arr:
        result ^= number
    return result
