from collections import deque


def solution(arr):
    """
    Args:
        arr (list): A list where indexes are walls' positions and values are their heights

    Returns:
        int: Minimal quantity of blocks needed to build such a wall
    """

    blocks_count = 0

    stack = deque()
    for i, curr in enumerate(arr):
        if i == 0:
            stack.appendleft(curr)
            blocks_count += 1
        else:
            prev = arr[i - 1]
            if curr > prev:
                stack.appendleft(curr)
                blocks_count += 1
            elif curr < prev:
                while len(stack) > 0:
                    if stack[0] <= curr:
                        break
                    else:
                        stack.popleft()

                if len(stack) == 0 or stack[0] != curr:
                    blocks_count += 1
                    stack.appendleft(curr)
    return blocks_count


assert solution([8, 8, 5, 7, 9, 8, 7, 4, 8]) == 7
assert solution([3, 2, 1]) == 3
assert solution([1, 2, 3, 3, 2, 1]) == 3
assert solution([2, 5, 1, 4, 6, 7, 9, 10, 1]) == 8
assert solution([1]) == 1
