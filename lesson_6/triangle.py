from collections import deque

from utils import check_time


@check_time
def solution(arr):
    """
    Args:
        arr (list): List of triangle edges' lengths

    Returns:
        int: 1 if there exists a triangular triplet for arr else 0.
    """
    n = len(arr)
    if n < 3:
        return 0

    arr.sort()
    ps, qs, rs = deque(), deque(), deque()
    for i, arr_i in enumerate(arr):
        if i + 1 < n and i + 2 < n:
            ps.append(arr_i)
            qs.append(arr[i + 1])
            rs.append(arr[i + 2])

    ps, qs, rs = list(ps), list(qs), list(rs)
    for i in range(len(ps)):
        if ps[i] + qs[i] > rs[i] and rs[i] + qs[i] > ps[i] and ps[i] + rs[i] > qs[i]:
            return 1

    return 0


assert solution([10, 2, 5, 1, 8, 20]) == 1
assert solution([10, 50, 5, 1]) == 0
assert solution([-10, -50, -5, -1]) == 0
assert solution([]) == 0
