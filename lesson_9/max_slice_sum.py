def solution(arr):
    """
    Args:
        arr (list): List of integers

    Returns:
        int: Max slice sum
    """

    max_ending = max_slice = None
    for i in arr:
        max_ending = max(max_ending + i, i) if max_ending else i
        max_slice = max(max_slice, max_ending) if max_slice else max_ending
    return max_slice


assert solution([10]) == 10
assert solution([-10]) == -10
assert solution([5, 10]) == 15
assert solution([5, -10]) == 5
assert solution([10, -10]) == 10
assert solution([3, 2, -6, 4, 0]) == 5
assert solution([-2, 1]) == 1
assert solution([3, -2, 3]) == 4
assert solution([3, -1, 4, 1]) == 7
