from collections import deque


def find_leader(arr):
    """
    Args:
        arr (list): List of integers

    Returns:
        int: leader of arr
    """
    stack = deque()
    for i, arr_i in enumerate(arr):

        if len(stack) == 0:
            stack.appendleft(arr_i)
        elif stack[0] != arr_i:
            stack.popleft()
        else:
            stack.appendleft(arr_i)

    if len(stack) == 0:
        return None

    candidate = stack[0]
    count = 0
    for i in arr:
        if candidate == i:
            count += 1

    return None if count < len(arr) // 2 else candidate


def solution(arr):
    """
    Args:
        arr (list): List of integers

    Returns:
        int: -1 if there is no leader else any leader index
    """
    leader = find_leader(arr)
    return -1 if leader is None else arr.index(leader)


assert solution([3, 2, 3, 4, 3, 3, 3 - 1]) == 0
assert solution([3, 2, 3, 4, 3, 3, 3 - 1]) == 0
assert solution([]) == -1
assert solution([1]) == 0
assert solution([5, 5, 5, 5, 5]) == 0
assert solution([5, 5, 5, 5, 5, 3, 3, 3, 3, 3]) == -1
assert solution([5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3]) == 5
assert solution([*([2] * 10), *([7] * 11)]) == 10
