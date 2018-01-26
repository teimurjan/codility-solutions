def solution(n):
    """
    Args:
        n (list): List of odd numbers

    Returns:
        int: The number occurs once in a list
    """
    result = 0
    for number in n:
        result ^= number
    return result
