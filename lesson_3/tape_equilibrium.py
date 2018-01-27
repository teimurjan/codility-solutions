from sys import maxsize


def solution(arr):
    """
    Args:
        arr (list): List of integers

    Returns:
        int: absolute value of the difference between the sum of first and the second parts of n
    """
    max_sum = 0
    for i in arr:
        max_sum += i

    min_difference = maxsize
    sub_sum = 0
    for i in range(0, len(arr) - 1):
        sub_sum += arr[i]
        difference = abs(max_sum - 2 * sub_sum)
        if difference < min_difference:
            min_difference = difference
    return min_difference


assert solution([3, 1, 2, 4, 3]) == 1
assert solution([3, 1]) == 2
