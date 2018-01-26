from sys import maxsize


def solution(n):
    """
    Args:
        n (list): List of integers

    Returns:
        int: absolute value of the difference between the sum of first and the second parts of n
    """
    max_sum = 0
    for i in n:
        max_sum += i

    min_difference = maxsize
    sub_sum = 0
    for i in range(0, len(n) - 1):
        sub_sum += n[i]
        difference = abs(max_sum - 2 * sub_sum)
        if difference < min_difference:
            min_difference = difference
    return min_difference


assert solution([3, 1, 2, 4, 3]) == 1
assert solution([3, 1]) == 2
